import requests
import sqlite3
import json
import urllib.request
import time
import os
import setting as setting

# We need an access_token to access the api on igdb.com (Game Database)
def get_twitch_access_token():
    try:
        r = requests.post('https://id.twitch.tv/oauth2/token?client_id=' + setting.client_id + '&client_secret=' + setting.client_secret + '&grant_type=client_credentials')
        json_str = json.loads(r.content)
        return json_str['access_token']
    except Exception as e:
        print(e)
        return None

# We fetch all games that are saved in our database. game_name has to be the first column after id
def get_all_games_from_db(table:str):
    print("Getting all games saved in table: " + table)
    games_tmp = []
    conn = sqlite3.connect('./database/data.db') #TODO:
    cursor = conn.cursor()
    sqlite_select_query = f"""SELECT * from {table}"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        game = {
            "id": row[0],
            "game_name": row[1]
        }
        games_tmp.append(game)
    return games_tmp

# Via igdb.com api we fetch the game id based on a search_string we give for a game (Which is the game_name we saved in the db)
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
            print(f"Found game id based on string: " + search_string)
            game_id = json_str[0]['id']
            return game_id
        else: 
            print(f"Could not find any game on string: {search_string}")
            return None
    except Exception as e:
        print(e)
        return None

# Via igdb.com api we fetch a game cover based on the id we got before
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
            print(f"Found game cover on id: {game_id}")
            cover_url = json_str[0]['url']
            cover_url = cover_url.replace('t_thumb', 't_cover_big')
            return cover_url
        else: 
            print(f"Could not find any game cover on that id: {game_id}")
            return None
    except Exception as e:
        print(e)
        return None

# We save the image locally that we got from the igdb.com api
def save_image_local(url, id, base_name):
    try:
        if os.path.isfile(base_name + str(id) + '.jpg'):
            print('Game: ' + base_name + str(id) + ' is already saved.')
            return None

        r = requests.get('https:' + url)
        if(r.status_code != 200): 
            raise Exception(f'Exception thrown in save_image_local. Code: {r.status_code}')
        with open(base_name + str(id) + '.jpg', 'wb') as outfile:
            outfile.write(r.content)
            print('Saved image: ' + base_name + str(id) + '.jpg')
    except Exception as e:
        print(e)
        return None

# We update the cover column in the database which just stores the name of the image
def update_covers_in_db(games, column, name):
    conn = sqlite3.connect('./database/data.db')
    cursor = conn.cursor()
    for i in range(1, len(games)+1):
        try:
            # Here we check if the cover image exists locally. If true, set the value in the db (api doesn't always find an image)
            with open('./public/images/game_images/' + name + str(i) + '.jpg', "r") as outfile:
                sqlite_select_query = f"""UPDATE {column} SET COVER = "{name}{i}.jpg" WHERE id = {i}"""
                cursor.execute(sqlite_select_query)
                conn.commit()
                print("Saved " + name + str(i) + "to column: " + column)
        except Exception as e:
            print(e)
            continue

# Example arguments
# table_name: Game
# image_full_path: ./public/images/game_images/
# image_name: game_image_

def process(table_name, image_path, image_name):
    # First the table 'Game' in db
    print(f"Starting process for {table_name}")
    setting.access_token = get_twitch_access_token()
    if setting.access_token is None:
        print("access_token not set. Ending script.")
        exit()
    games = get_all_games_from_db(table_name)
    for game in games:
        game_id = search_game_id(game['game_name'])
        if(game_id is not None):
            cover_url = search_game_cover(game_id)
            if(cover_url is not None):
                save_image_local(cover_url, game['id'], image_path + image_name)
    update_covers_in_db(games, table_name, image_name)
    print(f"Process for {table_name} was successful")

