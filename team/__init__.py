import requests as re
from lxml import etree
from bs4 import BeautifulSoup
import csv
import pandas
import numpy
from pyecharts.charts import Bar, Line, Page
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import players
import db.mysql as db


def create_csv(teamPath):
    path = 'team/csv/' + teamPath + '.csv'
    with open(path, 'a', newline='') as f:
        csv_writer = csv.writer(f)
        head = ['id', 'timeAndLoc', 'beat', 'scored']
        csv_writer.writerow(head)


def write_csv(teamPath, row):
    path = 'team/csv/' + teamPath + '.csv'
    with open(path, 'a+', newline='') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(row)


# 球队战绩
def teamRecord(referred):
    result = re.get(url="http://www.basketball-reference.com/teams/" + referred + "/2022.html",
                    headers={'Connection': 'close'})
    create_csv(referred)
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all(name='li', attrs={'class': 'result'})
    for recordPer in results:
        perRow = []
        tip = recordPer.find(name='span')['tip']
        # print(tip)
        tipRows = tip.split(',')
        idAndTimeAndLoc = tipRows[0].split('.')
        perRow.append(idAndTimeAndLoc[0])
        perRow.append(idAndTimeAndLoc[1])
        perRow.append(tipRows[1])
        perRow.append(tipRows[2])
        write_csv(referred, perRow)


# 更新所有球队战绩
def updateAllRecord():
    allTeam = db.queryAllTeams()
    for theTeam in allTeam:
        print(theTeam.referred)
        teamRecord(theTeam.referred)


# 生成所有球队图表
def createAllCharts():
    teams = db.queryAllTeams()
    for dataTeam in teams:
        team = pandas.read_csv('csv/' + dataTeam.referred + '.csv')
        scoredList = numpy.array(team.loc[:, 'scored']).tolist()
        y_data = []
        scoredDictList = []
        perGScoredList = []
        for data in scoredList:
            record = data.split('-')
            scoredDictList.append({'比分': record})
            y_data.append(int(record[0]) - int(record[1]))
            perGScoredList.append(record[0])

        homeList = numpy.array(team.loc[:, 'timeAndLoc']).tolist()
        x_data = []

        for data in homeList:
            homeStr = data.split('@')
            if len(homeStr) >= 2:
                x_data.append('客场: ' + homeStr[1])

            else:
                x_data.append('主场: ' + dataTeam.referred)

        bar = Bar(init_opts=opts.InitOpts(width='1000px'))
        bar.add_xaxis(xaxis_data=x_data)
        bar.add_yaxis(series_name="胜负分", y_axis=y_data)

        bar.set_global_opts(
            title_opts=opts.TitleOpts(title=dataTeam.name + "场均胜负分"),
            datazoom_opts=opts.DataZoomOpts(),
            xaxis_opts=opts.AxisOpts(name="主客场", axislabel_opts={"rotate": 45}, name_gap=10),
            yaxis_opts=opts.AxisOpts(name="胜分")
        )

        # bar.render('html/' + dataTeam.referred + ".html")

        intPerGScoredList = []
        for data in perGScoredList:
            intPerGScoredList.append(int(data))

        lists = sorted(intPerGScoredList, reverse=True)

        scoredBar = Bar()
        scoredBar.add_xaxis(x_data)
        scoredBar.add_yaxis(series_name='得分', y_axis=perGScoredList, )
        scoredBar.set_global_opts(
            title_opts=opts.TitleOpts(title='每场得分'),
            datazoom_opts=opts.DataZoomOpts(),
            yaxis_opts=opts.AxisOpts(max_=int(lists[0]) + 5, min_=int(lists[len(lists) - 1]) - 5),
            xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45}, name_location='center')
        )

        table = Table()
        teamName = db.queryNameByReferred(dataTeam.referred)
        theData = db.queryTeamReocrdByReferred(dataTeam.referred)
        row = [teamName, theData.won, theData.lost, theData.winRate]
        rows = [row]
        table.add(headers=['球队名', '胜场', '败场', '胜率'], rows=rows)
        table.set_global_opts(title_opts=ComponentTitleOpts(title='球队战绩'))

        print(dataTeam.referred)
        line = players.playerOfTeam(dataTeam.referred)
        Page(layout=Page.SimplePageLayout, interval=10) \
            .add(table, bar, scoredBar, line) \
            .render('html/' + dataTeam.referred + ".html")


if __name__ == '__main__':
    createAllCharts()
