import requests as request
from lxml import etree


# 东部
def parseEastStr(html):
    eastStr = html.xpath('//*[@id="confs_standings_E"]/thead/tr/th[1]/text()')
    print(eastStr[0])
    return eastStr[0]


# 西部
def parseWestStr(html):
    westStr = html.xpath('//*[@id="confs_standings_W"]/thead/tr/th[1]/text()')
    print(westStr[0])
    return westStr[0]


# 记录
class Record:
    division: str = ''
    referred: str = ''
    won: int = 0
    lost: int = 0
    divisionRank: int = 0
    winRate: float = 0.0

    def __init__(self, division: str, referred, won, lost, divisionRank, winRate):
        self.division = division
        self.referred = referred
        self.won = won
        self.lost = lost
        self.winRate = winRate
        self.divisionRank = divisionRank


def parseEastScored():
    re = request.get('https://www.basketball-reference.com/')
    content = re.text
    html = etree.HTML(content)

    listScored = []
    for index in range(15):
        # 球队名称
        namePath = "//*[@id='confs_standings_E']/tbody/tr[" + str(index + 1) + "]/th/a/text()"
        name = html.xpath(namePath)
        print(name[0])

        # 分区排名
        divisionRankPath = "//*[@id='confs_standings_E']/tbody/tr[" + str(index + 1) + "]/th/span/text()"
        divisionRankStr = html.xpath(divisionRankPath)[0].split("\\")[0]
        divisionRank = divisionRankStr[1:len(divisionRankStr) - 2]
        print(divisionRank)

        # 胜场数
        wonPath = "//*[@id='confs_standings_E']/tbody/tr[" + str(index + 1) + "]/td[3]/text()"
        wonStr = html.xpath(wonPath)
        print(wonStr[0])

        # 败场数
        lostPath = "//*[@id='confs_standings_E']/tbody/tr[" + str(index + 1) + "]/td[4]/text()"
        lostStr = html.xpath(lostPath)
        print(lostStr[0])

        # 胜率
        winRate = round(float(wonStr[0]) / (float(wonStr[0]) + float(lostStr[0])), 2)
        print(winRate)

        record = Record(division='east', referred=name[0], won=wonStr[0], lost=lostStr[0],
                        divisionRank=divisionRank, winRate=winRate)
        listScored.append(record)
    return listScored


def parseWestScored():
    re = request.get('https://www.basketball-reference.com/')
    content = re.text
    html = etree.HTML(content)

    listScored = []
    for index in range(15):
        # 球队名称
        namePath = "//*[@id='confs_standings_W']/tbody/tr[" + str(index + 1) + "]/th/a/text()"
        name = html.xpath(namePath)
        print(name[0])

        # 分区排名

        divisionRankPath = "//*[@id='confs_standings_W']/tbody/tr[" + str(index + 1) + "]/th/span/text()"
        divisionRankStr = html.xpath(divisionRankPath)[0].split("\\")[0]
        divisionRank = divisionRankStr[1:len(divisionRankStr) - 2]
        print(divisionRank)

        # 胜场数
        wonPath = "//*[@id='confs_standings_W']/tbody/tr[" + str(index + 1) + "]/td[3]/text()"
        wonStr = html.xpath(wonPath)
        print(wonStr[0])

        # 败场数
        lostPath = "//*[@id='confs_standings_W']/tbody/tr[" + str(index + 1) + "]/td[4]/text()"
        lostStr = html.xpath(lostPath)
        print(lostStr[0])

        # 胜率
        winRate = round(float(wonStr[0]) / (float(wonStr[0]) + float(lostStr[0])), 2)
        print(winRate)

        record = Record(division='west', referred=name[0], won=wonStr[0], lost=lostStr[0],
                        divisionRank=divisionRank, winRate=winRate)
        listScored.append(record)
    return listScored
