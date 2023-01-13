from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, Float
# 连接数据库
from sqlalchemy.engine import create
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from spite import divisionRecord as record


def createDB() -> create:
    return create_engine('mysql+pymysql://root:peichendong17@127.0.0.1:3306/nba', echo=False)


# 球队表
def createTableTeams():
    engine = createDB()
    metadata = MetaData(engine)
    teams = Table('csv', metadata,
                  Column('referred', String(5)),
                  Column('name', String(30)),
                  Column('division', String(5))
                  )
    metadata.create_all(engine)


# 创建战绩表
def createRecord():
    engine = createDB()
    metadata = MetaData(engine)
    Table('record', metadata,
          Column("referred", String(5), primary_key=True),
          Column("division", String(5), primary_key=True),
          Column("won", Integer),
          Column("lost", Integer),
          Column("division_rank", Integer),
          Column("winRate", Float),
          )
    metadata.create_all(engine)


# 创建球队数据表
def createTableTeamData():
    engine = createDB()
    metadata = MetaData(engine)
    teamData = Table('teamData', metadata,
                     Column('name', String(30), primary_key=True),
                     Column('season', String(15), primary_key=True),
                     Column('coach', String(30)),
                     Column('executive', String(30)),
                     Column('rank', Integer),
                     Column('pts', Float),
                     Column('pts_rank', Integer),
                     Column('opp_pts', Float),
                     Column('opp_pts_rank', Integer),
                     Column('srs', Float),
                     Column('srs_rank', Integer),
                     Column('pace', Float),
                     Column('pace_rank', Integer),
                     Column('off_rtg', Float),
                     Column('off_rtg_rank', Integer),
                     Column('def_rtg', Float),
                     Column('def_rtg_rank', Integer),
                     Column('arena', String(30)),
                     Column('attendance', String(30)),
                     Column('won', Integer),
                     Column('lost', Integer)
                     )

    metadata.create_all(engine)


# 球队数据数据类
class TeamData(declarative_base()):
    __tablename__ = 'teamdata'
    name = Column(String(30), primary_key=True)
    season = Column(String(15), primary_key=True)
    coach = Column(String(30))
    executive = Column(String(30))
    rank = Column(Integer)
    pts = Column(Float)
    pts_rank = Column(Integer)
    opp_pts = Column(Float)
    opp_pts_rank = Column(Integer)
    srs = Column(Float)
    srs_rank = Column(Integer)
    pace = Column(Float)
    pace_rank = Column(Integer)
    off_rtg = Column(Float)
    off_rtg_rank = Column(Integer)
    def_rtg = Column(Float)
    def_rtg_rank = Column(Integer)
    arena = Column(String(30))
    attendance = Column(String(30))
    won = Column(Integer)
    lost = Column(Integer)


def insertTeamData(teamData):
    engine = createDB()
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    team = TeamData(name=teamData.name, season=teamData.season, coach=teamData.coach, executive=teamData.executive
                    , rank=teamData.rank, pts=teamData.pts, pts_rank=teamData.pts_rank
                    , opp_pts=teamData.opp_pts, opp_pts_rank=teamData.opp_pts_rank, srs=teamData.srs
                    , srs_rank=teamData.srs_rank, pace=teamData.pace, pace_rank=teamData.pace_rank
                    , off_rtg=teamData.off_rtg, off_rtg_rank=teamData.off_rtg_rank, def_rtg=teamData.def_rtg
                    , def_rtg_rank=teamData.def_rtg_rank, arena=teamData.arena, attendance=teamData.attendance
                    , won=teamData.won, lost=teamData.lost)
    session.add(team)
    session.commit()


# 查询球队数据
def queryTeamDataByName(name):
    engine = createDB()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    teamData = session.query(TeamData).filter_by(name=name).first()
    return teamData


# 查询球队数据
def queryAllTeamData():
    engine = createDB()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    listTeamData = session.query(TeamData).all()
    return listTeamData


def deleteAllTeamData():
    engine = createDB()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    teamData = session.query(TeamData).all()
    for data in teamData:
        session.delete(data)
    session.commit()
    session.close()


# 球队名称类
class Teams(declarative_base()):
    __tablename__ = 'teams'
    referred = Column(String(5), primary_key=True)
    name = Column(String(30))
    division = Column(String(5))


# 查询球队简称及名称
def queryAllTeams():
    engine = createDB()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    listTeams = session.query(Teams).all()
    return listTeams


# 查询球队名通过referred
def queryNameByReferred(referred):
    engine = createDB()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    name = session.query(Teams).filter_by(referred=referred).first()
    return name.name


# 球队成绩类
class RecordData(declarative_base()):
    __tablename__ = 'record'
    referred = Column(String(5), primary_key=True)
    division = Column(String(5), primary_key=True)
    won = Column(Integer)
    lost = Column(Integer)
    division_rank = Column(Integer)
    winRate = Column(Float)


def queryTeamReocrdByReferred(referred):
    engine = createDB()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    recordData = session.query(RecordData).filter_by(referred=referred).first()
    return recordData


def insertRecord(recordData):
    engine = createDB()
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    re = RecordData(referred=recordData.referred, division=recordData.division, won=recordData.won,
                    lost=recordData.lost,
                    division_rank=recordData.divisionRank, winRate=recordData.winRate)
    session.add(re)
    session.commit()
    session.close()


def deleteAllRecord():
    engine = createDB()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    teamData = session.query(RecordData).all()
    for team in teamData:
        session.delete(team)
    session.commit()
    session.close()


def queryAllRecord():
    engine = createDB()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    listTeams = session.query(RecordData).order_by(RecordData.winRate.desc()).all()
    return listTeams


def queryEastRecord():
    engine = createDB()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    listEastRecord = session.query(RecordData).filter_by(division='east').order_by(RecordData.winRate.desc()).all()
    return listEastRecord


def deleteEastRecord():
    engine = createDB()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    listEastRecord = session.query(RecordData).filter_by(division='east').all()
    for east in listEastRecord:
        session.delete(east)
    session.commit()
    session.close()


def queryWestRecord():
    engine = createDB()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    listEastRecord = session.query(RecordData).filter_by(division='west').order_by(RecordData.winRate.desc()).all()
    return listEastRecord


def deleteWestRecord():
    engine = createDB()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    listWestRecord = session.query(RecordData).filter_by(division='west').order_by(RecordData.winRate.desc()).all()
    for west in listWestRecord:
        session.delete(west)
    session.commit()
    session.close()


if __name__ == '__main__':
    listEast = record.parseEastScored()
    liseWest = record.parseWestScored()
    for data in listEast:
        insertRecord(data)

    for data in liseWest:
        insertRecord(data)
