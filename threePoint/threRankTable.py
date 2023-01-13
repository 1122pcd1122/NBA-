from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import pandas as pd


# 三分命中率排行榜
def threeRankTable():
    player = pd.read_csv('../player.csv')

    # 首先根据三分投中数排名
    playerByPTS = player.sort_values('3P', ascending=False).iloc[0:20]
    print(playerByPTS)
    # 再根据命中率排名
    playerByPTS = playerByPTS.sort_values('3P%', ascending=False)

    # 三分数据
    playerMaxTwenty = playerByPTS.iloc[0:20, [1, 11, 12, 13]]

    # 名字
    playerMaxThreeName = playerMaxTwenty.iloc[0:20, 0]

    # 投中数
    playerMaxThreePoint = playerMaxTwenty.iloc[0:20, 1]

    # 出手数
    playerManThreeAttempt = playerMaxTwenty.iloc[0:20, 2]

    # 命中率
    playerMaxThreePercentage = playerMaxTwenty.iloc[0:20, 3]

    listPercentage = []
    for data in playerMaxThreePercentage:
        listPercentage.append(format(float(data), '.0%'))

    listPlayerName = []

    for data in playerMaxThreeName:
        listPlayerName.append(data.split('.')[0])

    listPoint = list(playerMaxThreePoint)
    listAttempt = list(playerManThreeAttempt)

    listName = []
    for data in listPlayerName:
        name = data.split("*")[0]
        listName.append(name)

    listThree = []
    for i in range(20):
        row = [listName[i], listPoint[i], listAttempt[i], listPercentage[i]]
        listThree.append(row)

    header = ['球员', '出手数', '命中数', '命中率']

    table = Table()

    table.add(header, listThree)
    table.set_global_opts(title_opts=ComponentTitleOpts(title='三分排名前二十名'))
    table.render('html/threeRankTable.html')


if __name__ == '__main__':
    threeRankTable()
