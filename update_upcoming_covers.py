import requests
import sqlite3
import json
import urllib.request
import time
import os
import setting as setting


def get_twitch_access_token():
    try:
        r = requests.post('https://id.twitch.tv/oauth2/token?client_id=' + setting.client_id + '&client_secret=' + setting.client_secret + '&grant_type=client_credentials')
        json_str = json.loads(r.content)
        return json_str['access_token']
    except Exception as e:
        print(e)
        return None

def get_all_games_from_db():
    games_tmp = []
    conn = sqlite3.connect('C:/Users/vinze/Documents/Programming/Repositories/symfony_vue_project/database/test.db')
    cursor = conn.cursor()
    sqlite_select_query = """SELECT * from Upcoming"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        game = {
            "id": row[0],
            "game_name": row[1]
        }
        games_tmp.append(game)
    return games_tmp

def search_game_cover(game_id):
    try:
        headers = {
            'Client-ID': setting.client_id,
            'Authorization': f'Bearer {setting.access_token}',
            'Accept': 'application/json',
        }
        r = requests.post('https://api.igdb.com/v4/covers', data='fields *; where game = ' + str(game_id) + ';', headers=headers)
        if(r.status_code != 200): 
            raise Exception(f'Exception thrown in search_game_cover. Code: {r.status_code}')
        json_str = json.loads(r.content)
        if(len(json_str) > 0):
            cover_url = json_str[0]['url']
            cover_url = cover_url.replace('t_thumb', 't_cover_big')
            return cover_url
        else: 
            print(f"Could not find any game on that id: {game_id}")
            return None
    except Exception as e:
        print(e)
        return None
    


def search_game_id(search_string):
    try:
        headers = {
            'Client-ID': setting.client_id,
            'Authorization': f'Bearer {setting.access_token}',
            'Accept': 'application/json',
        }
        r = requests.post('https://api.igdb.com/v4/games', data=f'search "{search_string}"; fields *;', headers=headers)
        if(r.status_code != 200): 
            raise Exception(f'Exception thrown in search_game_id. Code: {r.status_code}')
        json_str = json.loads(r.content)
        if(len(json_str) > 0):
            game_id = json_str[0]['id']
            return game_id
        else: 
            print(f"Could not find any game on that string: {search_string}")
            return None
    except Exception as e:
        print(e)
        return None

def save_image_local(url, id):
    try:
        r = requests.get('https:' + url)
        if(r.status_code != 200): 
            raise Exception(f'Exception thrown in save_image_local. Code: {r.status_code}')
        with open('./public/images/upcoming_images/game_image_upcoming_' + str(id) + '.jpg', 'wb') as outfile:
            outfile.write(r.content)
            print('Saved image: ' + 'game_image_upcoming_' + str(id) + '.jpg')
    except Exception as e:
        print(e)
        return None

# We need an access_token from Twitch for api calls on igdb.com
setting.access_token = get_twitch_access_token()

if setting.access_token is None:
    exit()

# Using igdb.com api to fetch cover images for every game in the database
games = get_all_games_from_db()
for game in games:
    game_id = search_game_id(game['game_name'])
    if(game_id is not None):
        cover_url = search_game_cover(game_id)
        if(cover_url is not None):
            save_image_local(cover_url, game['id'])

# Updates all covers in the database by id
conn = sqlite3.connect('./database/test.db')
cursor = conn.cursor()
for i in range(1, len(games)+1):
    try:
        with open('./public/images/upcoming_images/game_image_upcoming_' + str(i) + '.jpg', "r") as outfile:
            sqlite_select_query = f"""UPDATE Upcoming SET COVER = "game_image_upcoming_{i}.jpg" WHERE id = {i}"""
            cursor.execute(sqlite_select_query)
            conn.commit()
            print(f"Wrote id:{i} in database cover column")
    except Exception as e:
        print(f"Did not find image with id:{i}")
        continue
