import db.mysql as db
import requests as request
from lxml import etree


# 获取对应球队的html网页
def getTeamHtml(url):
    requests = request.get(url=url)
    return requests.text


# 赛季
def parseSeason(htmlDocument):
    season = htmlDocument.xpath('//*[@id="meta"]/div[2]/h1/span[1]/text()')
    print("赛季:" + season[0])
    return season[0]


# 球队名称
def parseTeamName(htmlDocument):
    name = htmlDocument.xpath('//*[@id="meta"]/div[2]/h1/span[2]/text()')
    print("球队:" + name[0])
    return name[0]


# 教练
def parseCoach(htmlDocument):
    coach = htmlDocument.xpath('//*[@id="meta"]/div[2]/p[4]/a/text()')
    print("教练:" + coach[0])
    return coach[0]


# 总经理
def parseExecutive(htmlDocument):
    executive = htmlDocument.xpath('//*[@id="meta"]/div[2]/p[5]/a/text()')
    print("总经理:" + executive[0])
    return executive[0]


# 场均得分及对手得分
def parsePtsAndOppPts(htmlDocument):
    ptsAndOppPts = htmlDocument.xpath('//*[@id="meta"]/div[2]/p[6]/text()')
    # print("场均得分及对手得分:")
    # print(ptsAndOppPts)
    return ptsAndOppPts


# 场均得分及排名
def parsePtsAndRank(htmlDocument):
    ptsAndOppPts = parsePtsAndOppPts(htmlDocument)
    ptsResultStr = ptsAndOppPts[1].split("\n")[1].lstrip()
    # print("场均得分及排名:" + ptsResultStr)
    ptsResults = ptsResultStr.split(" ")
    return ptsResults


# 场均得分
def parsePts(htmlDocument):
    ptsResults = parsePtsAndRank(htmlDocument)
    pts = ptsResults[0]
    print("场均得分:" + pts)
    return pts


# 场均得分排名
def parsePtsRank(htmlDocument):
    ptsResults = parsePtsAndRank(htmlDocument)
    pts_rank = ptsResults[1]
    print("场均得分排名:" + pts_rank[1:2])
    return pts_rank[1:2]


# 场均对手得分及排名
def parseOffPtsAndRank(htmlDocument):
    ptsAndOppPts = parsePtsAndOppPts(htmlDocument)
    offPtsResultStr = ptsAndOppPts[2].split("\n")[1].lstrip()
    # print("对手场均得分及排名:" + offPtsResultStr)
    offPtsResults = offPtsResultStr.split(" ")
    return offPtsResults


# 场均对手得分
def parseOffPts(htmlDocument):
    offPtsResults = parseOffPtsAndRank(htmlDocument)
    off_pts = offPtsResults[0]
    print("场均对手得分:" + off_pts)
    return off_pts


# 场均对手得分排名
def parseOffPtsRank(htmlDocument):
    offPtsResults = parseOffPtsAndRank(htmlDocument)
    off_pts_rank = offPtsResults[1]
    print("场均对手得分排名:" + off_pts_rank[1:2])
    return off_pts_rank[1:2]


# 球队评价及场均回合数
def parseSrsAndPaceResultStr(htmlDocument):
    srsAndPace = htmlDocument.xpath('//*[@id="meta"]/div[2]/p[7]/text()')
    # print("球队评价及场均回合数:")
    # print(srsAndPace)
    return srsAndPace


# 球队评价及排名
def parseSrsAndRank(htmlDocument):
    srsAndPace = parseSrsAndPaceResultStr(htmlDocument)
    srsAndPaceResultStr = srsAndPace[1].split("\n")[0].lstrip()
    # print("球队评价及评价排名:" + srsAndPaceResultStr[1:len(srsAndPaceResultStr)])
    return srsAndPaceResultStr


# 球队评价
def parseSrs(htmlDocument):
    srsAndPaceResultStr = parseSrsAndRank(htmlDocument)
    srs = srsAndPaceResultStr.split(" ")[1]
    print("球队评价:" + srs)
    return srs


# 球队评价排名
def parseSrsRank(htmlDocument):
    srsAndPaceResultStr = parseSrsAndRank(htmlDocument)
    srs_rank = srsAndPaceResultStr.split(" ")[2]
    print("球队评价排名:" + srs_rank[1:len(srs_rank) - 2])
    return srs_rank[1:len(srs_rank) - 2]


# 场均回合数及排名
def parsePaceAndRank(htmlDocument):
    paceAndRank = parseSrsAndPaceResultStr(htmlDocument)
    paceAndRankStr = paceAndRank[2].split("\n")[0].lstrip()
    # print("场均回合数及评价排名:" + srsAndPaceResultStr[1:len(srsAndPaceResultStr)])
    return paceAndRankStr


# 场均回合数
def parsePace(htmlDocument):
    paceAndRankStr = parsePaceAndRank(htmlDocument)
    pace = paceAndRankStr.split(" ")[1]
    print("场均回合数:" + pace)
    return pace


# 场均回合数排名
def parsePaceRank(htmlDocument):
    paceAndRankStr = parsePaceAndRank(htmlDocument)
    pace_rank = paceAndRankStr.split(" ")[2]
    print("场均回合数排名:" + pace_rank[1:len(pace_rank) - 2])
    return pace_rank[1:len(pace_rank) - 2]


# 进攻效率 防守效率 场均净胜分
def parseOffDefNetRtg(htmlDocument):
    offDefNetRtg = htmlDocument.xpath('//*[@id="meta"]/div[2]/p[8]/text()')
    # print("进攻效率 防守效率 场均净胜分:")
    # print(offDefNetRtg)
    return offDefNetRtg


# 进攻效率及排名
def parseOffAndRank(htmlDocument):
    off_def_net_rtg = parseOffDefNetRtg(htmlDocument)
    netRtgStr = off_def_net_rtg[1].split("\n")[0].lstrip()
    netRtgS = netRtgStr.split(" ")
    return netRtgS


# 进攻效率
def parseOffRtg(htmlDocument):
    netRtgs = parseOffAndRank(htmlDocument)
    print("进攻效率:" + netRtgs[1])
    return netRtgs[1]


# 进攻效率排名
def parseOffRtgRank(htmlDocument):
    netRtgs = parseOffAndRank(htmlDocument)
    net_rtg_rank = netRtgs[2]
    print("进攻效率排名:" + net_rtg_rank[1:len(net_rtg_rank) - 2])
    return net_rtg_rank[1:len(net_rtg_rank) - 2]


# 防守效率及排名
def parseDefRtgAndRank(htmlDocument):
    offDefNetRtg = parseOffDefNetRtg(htmlDocument)
    defRtgStr = offDefNetRtg[2].split("\n")[0].lstrip()
    netRtgS = defRtgStr.split(" ")
    return netRtgS


# 防守效率
def parseDefRtg(htmlDocument):
    netRtgS = parseDefRtgAndRank(htmlDocument)
    print("防守效率:" + netRtgS[1])
    return netRtgS[1]


# 防守效率排名
def parseDefRtgRank(htmlDocument):
    netRtgS = parseDefRtgAndRank(htmlDocument)
    net_rtg_rank = netRtgS[2]
    print("防守效率排名:" + net_rtg_rank[1:len(net_rtg_rank) - 2])
    return net_rtg_rank[1:len(net_rtg_rank) - 2]


# 场均净胜分及排名
def netRtgAndRank(htmlDocument):
    off_def_net_rtg = parseOffDefNetRtg(htmlDocument)
    # 场均净胜分及排名
    netRtgStr = off_def_net_rtg[3].split("\n")[0].lstrip()
    netRtgS = netRtgStr.split(" ")
    return netRtgS


# 净胜分
def parseNetRtg(htmlDocument):
    netRtgS = netRtgAndRank(htmlDocument)
    print("净效率值:" + netRtgS[1])
    return netRtgS[1]


# 防守效率排名
def parseNetRtgRank(htmlDocument):
    netRtgS = netRtgAndRank(htmlDocument)
    net_rtg_rank = netRtgS[2]
    print("净效率值排名:" + net_rtg_rank[1:len(net_rtg_rank) - 2])
    return net_rtg_rank[1:len(net_rtg_rank) - 2]


# 球馆及访问人数
def parseArenaAndAttendance(htmlDocument):
    # 球馆及访问人数
    arenaAndAttendance = htmlDocument.xpath('//*[@id="meta"]/div[2]/p[11]/text()')
    # print(arenaAndAttendance)
    return arenaAndAttendance


# 球馆
def parseArena(htmlDocument):
    arenaAndAttendance = parseArenaAndAttendance(htmlDocument)
    areaStr = arenaAndAttendance[1].split("\n")
    area = areaStr[1].lstrip()
    print("球馆:" + area)
    return area


# 访问人数及排名
def parseAttendanceAndRank(htmlDocument):
    arenaAndAttendance = parseArenaAndAttendance(htmlDocument)
    if len(arenaAndAttendance) > 2:
        attendanceStr = arenaAndAttendance[2].split("\n")
    else:
        attendanceStr = arenaAndAttendance[1].split("\n")
    attendanceNumAndRankStr = attendanceStr[1].lstrip()
    attendanceNumRanks = attendanceNumAndRankStr.split(" ")
    return attendanceNumRanks


# 访问人次
def parseAttendance(htmlDocument):
    attendanceNumRanks = parseAttendanceAndRank(htmlDocument)
    print("访问人次:" + attendanceNumRanks[0])
    return attendanceNumRanks[0]


# 访问人次排名
def parseAttendanceRank(htmlDocument):
    attendanceNumRanks = parseAttendanceAndRank(htmlDocument)
    attendanceRank = attendanceNumRanks[1]
    print("访问人数排名:" + attendanceRank[1:len(attendanceRank) - 2])
    return attendanceRank[1:len(attendanceRank) - 2]


# 胜场和败场数
def parseWinAndLost(htmlDocument):
    record = htmlDocument.xpath('//*[@id="meta"]/div[2]/p[1]/text()')
    winAndLostStrs = record[1].split("\n")[2].lstrip()
    # print(winAndLostStrs)
    return winAndLostStrs


# 胜场数
def parseWon(htmlDocument):
    winAndLostStrs = parseWinAndLost(htmlDocument)
    winAndLost = winAndLostStrs.split(', ')[0]
    print("胜场数" + winAndLost.split('-')[0])
    return winAndLost.split('-')[0]


# 球队败场数
def parseLost(htmlDocument):
    winAndLostStrs = parseWinAndLost(htmlDocument)
    winAndLost = winAndLostStrs.split(', ')[0]
    print("败场数" + winAndLost.split('-')[1])
    return winAndLost.split('-')[1]


# 球队排名
def parseRank(htmlDocument):
    winAndLostStrs = parseWinAndLost(htmlDocument)
    winAndLost = winAndLostStrs.split(', ')[1]
    print("排名" + winAndLost[0:len(winAndLost) - 6])
    return winAndLost[0:len(winAndLost) - 6]


# 球队数据类
class TeamsData:
    # 球队名称
    name: str = ''
    # 赛季
    season: str = ''

    # 教练
    coach: str = ''

    # 总经理
    executive: str = ''

    # 排名
    rank: int = 0

    # 场均得分
    pts: float = 0.0
    # 场均得分排名
    pts_rank: int = 0

    # 场均对手得分
    opp_pts: float = 0.0
    # 场均对手得分排名
    opp_pts_rank: int = 0

    # 球队评价
    srs: float = 0.0
    # 球队评价排名
    srs_rank: int = 0

    # 场均回合数
    pace: float = 0.0
    # 场均回合数排名
    pace_rank: int = 0

    # 进攻效率值
    off_rtg: float = 0.0
    # 进攻效率排名
    off_rtg_rank: int = 0

    # 防守效率值
    def_rtg: float = 0.0

    # 防守效率值排名
    def_rtg_rank: int = 0

    # 球队净胜效率值
    net_rtg: float = 0.0
    # 球队净胜效率值排名
    net_rtg_rank: int = 0

    # 球馆
    arena: str = ''

    # 总进场观看人次
    attendance: str = ''

    # 获胜数
    won: int = 0

    # 失败数
    lost: int = 0

    @staticmethod
    class Builder:
        # 球队名称
        name: str = ''
        # 赛季
        season: str = ''

        # 教练
        coach: str = ''

        # 总经理
        executive: str = ''

        # 排名
        rank: int = 0

        # 场均得分
        pts: float = 0.0
        # 场均得分排名
        pts_rank: int = 0

        # 场均对手得分
        opp_pts: float = 0.0
        # 场均对手得分排名
        opp_pts_rank: int = 0

        # 球队评价
        srs: float = 0.0
        # 球队评价排名
        srs_rank: int = 0

        # 场均回合数
        pace: float = 0.0
        # 场均回合数排名
        pace_rank: int = 0

        # 进攻效率值
        off_rtg: float = 0.0
        # 进攻效率排名
        off_rtg_rank: int = 0

        # 防守效率值
        def_rtg: float = 0.0

        # 防守效率值排名
        def_rtg_rank: int = 0

        # 球队净胜效率值
        net_rtg: float = 0.0
        # 球队净胜效率值排名
        net_rtg_rank: int = 0

        # 球馆
        arena: str = ''

        # 总进场观看人次
        attendance: str = ''

        # 获胜数
        won: int = 0

        # 失败数
        lost: int = 0

        def __init__(self, theName: str, theSeason: str):
            self.name = theName
            self.season = theSeason

        def setCoach(self, theCoach: str):
            self.coach = theCoach
            return self

        def setExecutive(self, theExecutive: str):
            self.executive = theExecutive
            return self

        def setRank(self, rank: int):
            self.rank = rank
            return self

        def setPts(self, thePts: float):
            self.pts = thePts
            return self

        def setPtsRank(self, thePtsRank: int):
            self.pts_rank = thePtsRank
            return self

        def setOppPts(self, theOppPtS: float):
            self.opp_pts = theOppPtS
            return self

        def setOppPtsRank(self, theOppPtsRank: int):
            self.opp_pts_rank = theOppPtsRank
            return self

        def setSrs(self, theSrs: float):
            self.srs = theSrs
            return self

        def setSrsRank(self, theSrsRank: int):
            self.srs_rank = theSrsRank
            return self

        def setPace(self, thePace: float):
            self.pace = thePace
            return self

        def setPaceRank(self, thePaceRank: int):
            self.pace_rank = thePaceRank
            return self

        def setOffRtg(self, theOffRtg: float):
            self.off_rtg = theOffRtg
            return self

        def setOffRtgRank(self, theOffRtgRank: int):
            self.off_rtg_rank = theOffRtgRank
            return self

        def setDefRtg(self, theDefRtg: float):
            self.def_rtg = theDefRtg
            return self

        def setDefRtgRank(self, theDefRtgRank: int):
            self.def_rtg_rank = theDefRtgRank
            return self

        def setNetRtg(self, theNetRtg: float):
            self.net_rtg = theNetRtg
            return self

        def setNetRtgRank(self, theNetRtgRank: int):
            self.net_rtg_rank = theNetRtgRank
            return self

        def setArena(self, theArena: str):
            self.arena = theArena
            return self

        def setAttendance(self, theAttendance: str):
            self.attendance = theAttendance
            return self

        def setWon(self, theWon: int):
            self.won = theWon
            return self

        def setLost(self, theLost: int):
            self.lost = theLost
            return self

        def build(self):
            return TeamsData(self)

    def __init__(self, builder: Builder):
        self.name = builder.name
        self.season = builder.season
        self.coach = builder.coach
        self.executive = builder.executive
        self.rank = builder.rank
        self.pts = builder.pts
        self.pts_rank = builder.pts_rank
        self.opp_pts = builder.opp_pts
        self.opp_pts_rank = builder.opp_pts_rank
        self.srs = builder.srs
        self.srs_rank = builder.srs_rank
        self.pace = builder.pace
        self.pace_rank = builder.pace_rank
        self.off_rtg = builder.off_rtg
        self.off_rtg_rank = builder.off_rtg_rank
        self.def_rtg = builder.def_rtg
        self.def_rtg_rank = builder.def_rtg_rank
        self.net_rtg = builder.net_rtg
        self.net_rtg_rank = builder.net_rtg_rank
        self.arena = builder.arena
        self.attendance = builder.attendance
        self.won = builder.won
        self.lost = builder.lost


def deleteTeamData():
    db.deleteAllTeamData()


def listTeamsData():
    data = db.queryAllTeams()
    listTeamData = []

    # 2022赛季
    for team in data:
        print("球队:" + team.name)
        print("获取数据中!!!")
        result = request.get(url="https://www.basketball-reference.com/teams/" + team.referred + "/2022.html")
        print("数据获取完成!!!")
        content = result.text
        html = etree.HTML(content)

        teamData = TeamsData \
            .Builder(parseTeamName(html), parseSeason(html)) \
            .setCoach(parseCoach(html)) \
            .setExecutive(parseExecutive(html)) \
            .setRank(parseRank(html)) \
            .setPts(parsePts(html)) \
            .setPtsRank(parsePtsRank(html)) \
            .setOppPts(parseOffPts(html)) \
            .setOppPtsRank(parseOffPtsRank(html)) \
            .setSrs(parseSrs(html)) \
            .setSrsRank(parseSrsRank(html)) \
            .setPace(parsePace(html)) \
            .setPaceRank(parsePaceRank(html)) \
            .setOffRtg(parseOffRtg(html)) \
            .setOffRtgRank(parseOffPtsRank(html)) \
            .setDefRtg(parseDefRtg(html)) \
            .setDefRtgRank(parseDefRtgRank(html)) \
            .setNetRtg(parseNetRtg(html)) \
            .setNetRtgRank(parseNetRtgRank(html)) \
            .setArena(parseArena(html)) \
            .setAttendance(parseAttendance(html)) \
            .setWon(parseWon(html)) \
            .setLost(parseLost(html)).build()

        listTeamData.append(teamData)

    return listTeamData


# 测试
if __name__ == '__main__':
    # deleteTeamData()
   for data in listTeamsData():
       db.insertTeamData(data)

