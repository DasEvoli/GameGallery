# Game Gallery
This project was created to get familiar with PHP 8.0, Symfony 6 and Vue3.js. The data I used is from Bangerra, a youtuber/twitch streamer who has his own challenge of playing all games he owns. He keeps track of them via a CSV file. I simply use this data from the CSV file and display it nicely.

The python scripts I provide do need to use the Schema of the database I use. Gamelist is the entire game list and 'Upcoming' is from another CSV file where certain games are mentioned that will be played next.
Also one script fetches all thumbnails for every game record by searching its name in the database provided by the api from https://www.igdb.com/
The script called 'bangerra' is basically useless because it is just for my case and fetches the data from the CSV he provides.

##  Database Schema:

Table: Game  
id (int), console_name (string), game_name(string), collection_name(string), genre(string), time(string), score(int), video_url(string), speedrun(bool) cover(string)

Table: Upcoming  
id (int), game_name (string), cover (string)

# Requirements
* PHP >= 8.0
* Python >= 3.0
* Symfony 6.0
* npm
* Composer >=2.1
* sqlite3 database in Database directory and update .env accordingly

## Authors
![Image of DasEvoli](https://i.imgur.com/xNcLWUT.png) DasEvoli (Vinzenz Wetzel)

## License
* This project is licensed under the Apache License 2.0.