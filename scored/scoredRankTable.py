from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import pandas as pd


# 命中率排名
def scoredRank():
    player = pd.read_csv('player.csv')
    playerByPTS = player.sort_values('PTS', ascending=False).iloc[0:20]
    print(playerByPTS)
    # 再根据命中率排名
    playerByPTS = playerByPTS.sort_values('eFG%', ascending=False)
    # 两分数据
    playerMaxTwenty_scored = playerByPTS.iloc[0:20, [1, 8, 9, 17, 29]]
    # 名字
    playerMaxScoredName = playerMaxTwenty_scored.iloc[0:20, 0]
    # 投中数
    playerMaxScoredPoint = playerMaxTwenty_scored.iloc[0:20, 1]
    # 出手数
    playerManScoredAttempt = playerMaxTwenty_scored.iloc[0:20, 2]
    # 命中率
    playerMaxScoredPercentage = playerMaxTwenty_scored.iloc[0:20, 3]
    # 总得分
    playerMaxScored = playerMaxTwenty_scored.iloc[0:20, 4]
    listPercentage = []
    for data in playerMaxScoredPercentage:
        listPercentage.append(format(float(data), '.0%'))
    listPlayerName = list(playerMaxScoredName)
    listPoint = list(playerMaxScoredPoint)
    listAttempt = list(playerManScoredAttempt)
    listScored = list(playerMaxScored)
    listName = []
    for data in listPlayerName:
        name = data.split("*")[0]
        listName.append(name)

    listThree = []
    for i in range(20):
        row = [listName[i], listPoint[i], listAttempt[i], listPercentage[i], listScored[i]]
        listThree.append(row)
    header = ['球员', '出手数', '命中数', '命中率', '总得分']
    table = Table()
    table.add(header, listThree)
    table.set_global_opts(title_opts=ComponentTitleOpts(title='命中率排名前二十名'))
    table.render('scored/html/scoredRankTable.html')


if __name__ == '__main__':
    scoredRank()

