import datetime
import threading

import bs4
from spite.player import jsonToCsv, convertTable
import requests as re
from spite.divisionRecord import parseWestScored, parseEastScored
from spite.teamData import listTeamsData
import db.mysql as db
import players
import efficiency, threePoint, twoPoint, scored
import team


# 更新球员信息
def updateAllPlayerInfo():
    # 更新球员信息
    result = re.get('https://www.basketball-reference.com/leagues/NBA_2022_totals.html')
    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    table = soup.table
    tableStr = convertTable(table, True)
    jsonToCsv(tableStr=tableStr)


# 更新球队名次
def updateTeamRank():
    # 更新球队战绩
    listWest = parseWestScored()
    listEast = parseEastScored()
    db.deleteAllRecord()
    for east in listEast:
        db.insertRecord(east)
    for west in listWest:
        db.insertRecord(west)


# 更新球队信息
def updateTeamInfo():
    # 更新球队数据
    db.deleteAllTeamData()
    listTeamData = listTeamsData()
    for data in listTeamData:
        db.insertTeamData(data)


# 更新所有
def updateAll():
    updateTeamRank()
    updateTeamInfo()
    updateAllPlayerInfo()
    team.updateAllRecord()
    players.updateAllPlayerCareerInfo()
    scored.updateScored()
    twoPoint.updateTwoPoint()
    threePoint.updateThreePoint()
    efficiency.updateEfficiency()
    team.createAllCharts()


# 定时任务
def timingTask():
    # 获取现在时间
    now_time = datetime.datetime.now()
    # 获取明天时间
    next_time = now_time + datetime.timedelta(days=+1)
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day
    # 获取明天3点时间
    next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 18:00:00",
                                           "%Y-%m-%d %H:%M:%S")

    # 获取距离明天3点时间，单位为秒
    timer_start_time = (next_time - now_time).total_seconds()

    # 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
    timer = threading.Timer(timer_start_time, updateAll)
    timer.start()


# 定时任务开始
if __name__ == '__main__':
    team.createAllCharts()
