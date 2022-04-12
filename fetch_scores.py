import requests
from pyquery import PyQuery as pq

import os
import re
from hashlib import sha256

game_parse_regex = r'(.+) \((\d+)\) @ (.+) \((\d+)\)'

season_to_get = '2021'
season_data_path = f'season_data{os.path.sep}' 
season_data_file_path = f'{season_data_path}{season_to_get}.csv'

url = f'https://www.baseball-reference.com/leagues/majors/{season_to_get}-schedule.shtml'
cache_path = 'cache' + os.path.sep

sha = sha256()
sha.update(url.encode("utf-8"))
digest = sha.hexdigest()

cache_file = f'{cache_path}{digest}'

try:
	with open(cache_file, 'r') as file:
		data = file.read()
except FileNotFoundError:	
	#cache miss
	with open(cache_file, 'w+') as file:
		r = requests.get(url)
		if r.status_code == 200:
			page_contents = r.text
			file.write(page_contents)
			data = page_contents
			
else:
	print("cache hit")


page = pq(data)

season_sections = page("div.section_wrapper")

regular_season = pq(season_sections[0])
post_season = pq(season_sections[1])

days = regular_season("div.section_content > div")

game_list = []

for day in days:
	
	pday = pq(day)
	
	game_date = pday("h3").text()
	
	games = pday("p")
	
	for game in games:
		
		game_text = pq(game).text()
		
		matches = re.match(game_parse_regex, game_text)
		
		if matches:
			away_team = matches.group(1)
			away_score = matches.group(2)
			home_team = matches.group(3)
			home_score = matches.group(4)
			
			game_list.append((f'"{game_date}"', away_team, away_score, home_team, home_score))
			

with open(season_data_file_path, 'w+') as season_data_file:
	for game in game_list:
		season_data_file.write(','.join(f'{elem.strip()}' for elem in game) + '\n')
	
	
	