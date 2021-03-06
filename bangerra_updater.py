import requests
import sqlite3
import json
import urllib.request
import time
import os
import setting as setting
import csv
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import update_covers_in_db

Base = declarative_base()
class Game(Base):
    __tablename__ = "Game"

    id = Column('id', Integer, primary_key=True)

    game_name = Column('game_name', String)
    console_name = Column('console_name', String)
    collection_name = Column('collection_name', String)
    genre = Column('genre', String)
    time = Column('time', String)
    score = Column('score', Integer)
    video_url = Column('video_url', String)
    speedrun = Column('speedrun', Boolean)
    cover = Column('cover', String)

class Upcoming(Base):
    __tablename__ = "Upcoming"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    game_name = Column('game_name', String)

def write_csv_challenges_to_db():
    offset = 2
    with open(os.path.dirname(__file__) + '/assets/csv/challenge_list.csv', encoding="utf8") as csvfile:
        r = csv.reader(csvfile, delimiter=',')
        session = Session()
        for row in r:
            if r.line_num < offset: continue
            if not row[0]: continue

            e = Game()
            if row[0]:
                e.console_name = row[0]
            if row[1]:
                e.game_name = row[1]
            if row[2]:
                e.genre = row[2]
            if row[4]:
                e.time = row[4]
            if row[5]:
                e.time = row[5]
            if row[6]:
                e.score = row[6]
            if row[7]:
                e.video_url = row[7]
            if row[8]:
                e.speedrun = True
            e.cover = None
            if e.game_name:
                session.add(e)
        session.commit()
        session.close()
        print("Finished writing challenge_list.csv to database")

def delete_all_from_db(table):
    conn = sqlite3.connect('./database/data.db')
    cursor = conn.cursor()
    sqlite_query = f"""DELETE FROM {table}"""
    cursor.execute(sqlite_query)
    conn.commit()
    print("Deleted all records of table: " + table)

def write_csv_upcoming_to_db():
    offset = 5
    with open(os.path.dirname(__file__) + '/assets/csv/upcoming_list.csv', encoding="utf8") as csvfile:
        r = csv.reader(csvfile, delimiter=',')
        session = Session()
        for row in r:
            if r.line_num < offset: continue
            e = Upcoming()
            if row[2]:
                e.game_name = row[2]
                session.add(e)
            else: break
        session.commit()
        session.close()
        print("Finished writing upcoming_list.csv to database")

def download_csv(filename, download_url):
    r = requests.get(download_url, allow_redirects=True)
    if(r.status_code == 200):
        open(os.path.dirname(__file__) + f'/assets/csv/{filename}', 'wb').write(r.content)
        r.close()
    else:
        raise Exception(f"Request Status Code {r.status_code} when downloading {download_url}")

while True:
    
    time.sleep(604800) # 1 week
    engine = create_engine('sqlite:///' + os.path.dirname(__file__) + '/database/data.db', echo=True, future=True)
    if len(Base.metadata.tables) < 1: Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    try:
        download_csv('challenge_list.csv','https://docs.google.com/spreadsheets/d/1vUJektC3SB15tTF1rYKPmsAIzxVoHidl1wpNB18gQdc/export?format=csv&id=1vUJektC3SB15tTF1rYKPmsAIzxVoHidl1wpNB18gQdc&gid=0')
        download_csv('upcoming_list.csv', 'https://docs.google.com/spreadsheets/d/1vUJektC3SB15tTF1rYKPmsAIzxVoHidl1wpNB18gQdc/export?format=csv&id=1vUJektC3SB15tTF1rYKPmsAIzxVoHidl1wpNB18gQdc&gid=1535906847')
    except Exception as e:
        print(e)


    delete_all_from_db('Game')
    write_csv_challenges_to_db()
    delete_all_from_db('Upcoming')
    write_csv_upcoming_to_db()

    update_covers_in_db.process('Game', './public/images/game_images/', 'game_image')
    update_covers_in_db.process('Upcoming', './public/images/game_images/', 'game_image_upcoming_')