import csv
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os



conn = sqlite3.connect('./database/test.db')
cursor = conn.cursor()
sqlite_query = f"""DELETE FROM Upcoming"""
cursor.execute(sqlite_query)
conn.commit()




Base = declarative_base()
class Game(Base):
    __tablename__ = "Upcoming"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    game_name = Column('game_name', String)

engine = create_engine('sqlite:///' + os.path.dirname(__file__) + '/database/test.db', echo=True, future=True)
if len(Base.metadata.tables) < 1: Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

offset = 5
with open(os.path.dirname(__file__) + '/assets/csv/upcoming_list.csv', encoding="utf8") as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    session = Session()
    for row in r:
        if r.line_num < offset: continue
        e = Game()
        if row[2]:
            e.game_name = row[2]
            session.add(e)
        else: break
    session.commit()
    session.close()





