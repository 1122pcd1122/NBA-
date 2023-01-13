import random

from pyecharts.charts import Tab, Line, Grid
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
from pyecharts.options import global_options as opts
from db import mysql
import pandas as pd


# 两份排行榜
def twoRankTable():
    player = pd.read_csv('../player.csv')

    # 首先根据三分投中数排名
    playerByPTS = player.sort_values('2P', ascending=False).iloc[0:20]
    print(playerByPTS)
    # 再根据命中率排名
    playerByPTS = playerByPTS.sort_values('2P%', ascending=False)

    # 两分数据
    playerMaxTwenty_two = playerByPTS.iloc[0:20, [1, 14, 15, 16]]

    # 名字
    playerMaxTwoName = playerMaxTwenty_two.iloc[0:20, 0]

    # 投中数
    playerMaxTwoPoint = playerMaxTwenty_two.iloc[0:20, 1]

    # 出手数
    playerManTwoAttempt = playerMaxTwenty_two.iloc[0:20, 2]

    # 命中率
    playerMaxTwoPercentage = playerMaxTwenty_two.iloc[0:20, 3]

    listPercentage = []
    for data in playerMaxTwoPercentage:
        listPercentage.append(format(float(data), '.0%'))

    listPoint = list(playerMaxTwoPoint)
    listAttempt = list(playerManTwoAttempt)

    listPlayerName = []
    for data in playerMaxTwoName:
        listPlayerName.append(data.split('.')[0])

    listName = []
    for data in listPlayerName:
        name = data.split("*")[0]
        listName.append(name)

    listThree = []
    for i in range(20):
        row = [listName[i], listPoint[i], listAttempt[i], listPercentage[i]]
        listThree.append(row)

    header = ['球员', '命中数', '出手数', '命中率']

    table = Table()

    table.add(header, listThree)
    table.set_global_opts(title_opts=ComponentTitleOpts(title='两分排名前二十名'))
    table.render('html/twoRankTable.html')


if __name__ == '__main__':
    twoRankTable()
