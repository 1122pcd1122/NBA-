import bs4
import pandas as pd
import requests as re
from pyecharts.charts import Line, Timeline
import pyecharts.options as opts
from pyecharts.globals import ThemeType

import db.mysql as db
from spite.player import convertTable, playerJsonToCsv


# 生成球队所有球员的生涯数据图表
def playerOfTeam(referred):
    player = pd.read_csv('../player.csv')
    df = pd.DataFrame(player)
    teamPlayers = df[df['Tm'] == referred]
    player = teamPlayers.loc[:, 'Player']

    timeLine = Timeline()
    for data in player:
        name = data.split('*')[0]
        link = data.split('*')[1]
        print(name + "  " + link)
        playerCsv = pd.read_csv('players/'+referred + '/csv/' + name + '.csv')
        playerCsv = pd.DataFrame(playerCsv)
        pAttribute = playerCsv.loc[:, ['Season', '3P%', '2P%', 'eFG%', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'PTS']]
        listSeason = pAttribute.loc[:, 'Season']
        listThreePercentage = pAttribute.loc[:, '3P%']
        listTwoPercentage = pAttribute.loc[:, '2P%']
        listEfficiencyPercentage = pAttribute.loc[:, 'eFG%']
        listFreeThrowPercentage = pAttribute.loc[:, 'FT%']
        listOffensiveRebound = pAttribute.loc[:, 'ORB']
        listDefensiveRebound = pAttribute.loc[:, 'DRB']
        listTotalRebound = pAttribute.loc[:, 'TRB']
        listAssist = pAttribute.loc[:, 'AST']
        listPoints = pAttribute.loc[:, 'PTS']

        line = Line(init_opts=opts.InitOpts())
        line.add_xaxis(list(listSeason))
        line.add_yaxis(series_name='三分命中率', y_axis=list(listThreePercentage))
        line.add_yaxis(series_name='两分命中率', y_axis=list(listTwoPercentage))
        line.add_yaxis(series_name='有效命中率', y_axis=list(listEfficiencyPercentage))
        line.add_yaxis(series_name='罚球命中率', y_axis=list(listFreeThrowPercentage))
        line.add_yaxis(series_name='场均进攻篮板', y_axis=list(listOffensiveRebound))
        line.add_yaxis(series_name='场均防守篮板', y_axis=list(listDefensiveRebound))
        line.add_yaxis(series_name='场均篮板', y_axis=list(listTotalRebound))
        line.add_yaxis(series_name='场均助攻', y_axis=list(listAssist))
        line.add_yaxis(series_name='场均得分', y_axis=list(listPoints))
        line.set_global_opts(
            title_opts=opts.TitleOpts(title=name + "生涯数据", pos_left='center', pos_top='25'),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        )
        timeLine.add(line, name)
        timeLine.add_schema(label_opts=opts.LabelOpts(is_show=False))

    timeLine.render('players/render.html')
    return timeLine


# 球员生涯数据
def playerInfo(link, name, referred):
    result = re.get('http://www.basketball-reference.com' + link, headers={'Connection': 'close'})
    print(result.url)
    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    table = soup.table
    tableStr = convertTable(table, False)
    playerJsonToCsv(tableStr=tableStr, playerName=name, teamName=referred)


# 更新球队球员生涯数据
def updatePlayerInfo(referred):
    player = pd.read_csv('player.csv')
    df = pd.DataFrame(player)
    teamPlayers = df[df['Tm'] == referred]
    player = teamPlayers.loc[:, 'Player']
    for data in player:
        name = data.split('*')[0]
        link = data.split('*')[1]
        print(name + "  " + link)
        playerInfo(link, name, referred)


# 更新所有球队球员生涯数据
def updateAllPlayerCareerInfo():
    teams = db.queryAllTeams()
    for team in teams:
        updatePlayerInfo(team.referred)


if __name__ == '__main__':
    updateAllPlayerCareerInfo()
