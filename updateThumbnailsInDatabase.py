import sqlite3

conn = sqlite3.connect('./database/test.db')
cursor = conn.cursor()

for i in range(1, 1537):
    
    try:
        with open('./public/images/game_images/game_image_' + str(i) + '.jpg', "r") as outfile:
            sqlite_select_query = f"""UPDATE Game SET COVER = "game_image_{i}.jpg" WHERE id = {i}"""
            cursor.execute(sqlite_select_query)
            conn.commit()
    except Exception as e:
        print(f"found {i}")
        continue