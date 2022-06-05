import requests
import sqlite3
import json
import urllib.request
import time
import os.path
import setting as setting


def get_twitch_access_token():
    r = requests.post('https://id.twitch.tv/oauth2/token?client_id=' + setting.client_id + '&client_secret=' + setting.client_secret + '&grant_type=client_credentials')
    json_str = json.loads(r.content)
    return json_str['access_token']

access_token = get_twitch_access_token()


def get_all_games_from_db():
    games_tmp = []
    conn = sqlite3.connect('C:/Users/vinze/Documents/Programming/Repositories/symfony_vue_project/database/test.db')
    cursor = conn.cursor()
    sqlite_select_query = """SELECT * from Game"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        game = {
            "id": row[0],
            "console_name": row[1],
            "game_name": row[2]
        }
        games_tmp.append(game)
    return games_tmp

def search_game_cover(game_id):
    try:
        headers = {
            'Client-ID': setting.client_id,
            'Authorization': f'Bearer {access_token}',
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
            'Authorization': f'Bearer {access_token}',
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
        if os.path.isfile('./public/images/game_images/game_image_' + str(id) + '.jpg'):
            print('Game with id: ' + str(id) + ' is already saved.')
            return None

        r = requests.get('https:' + url)
        if(r.status_code != 200): 
            raise Exception(f'Exception thrown in save_image_local. Code: {r.status_code}')
        with open('./public/images/game_images/game_image_' + str(id) + '.jpg', 'wb') as outfile:
            outfile.write(r.content)
            print('Saved image: ' + 'game_image_' + str(id) + '.jpg')
    except Exception as e:
        print(e)
        return None


games = get_all_games_from_db()

for game in games:
    game_id = search_game_id(game['game_name'])
    if(game_id is not None):
        cover_url = search_game_cover(game_id)
        if(cover_url is not None):
            save_image_local(cover_url, game['id'])



