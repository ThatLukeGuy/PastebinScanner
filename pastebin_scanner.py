import requests
import re
import time
import os



while 1 == 1:



	print('   ___          _       _     _             __                                 ')
	print('  / _ \\__ _ ___| |_ ___| |__ (_)_ __       / _\\ ___ __ _ _ __  _ __   ___ _ __ ')
	print(' / /_)/ _` / __| __/ _ \\ \'_ \\| | \'_ \\ _____\\ \\ / __/ _` | \'_ \\| \'_ \\ / _ \\ \'__|')
	print('/ ___/ (_| \\__ \\ ||  __/ |_) | | | | |_____|\\ \\ (_| (_| | | | | | | |  __/ |   ')
	print('\\/    \\__,_|___/\\__\\___|_.__/|_|_| |_|     \\__/\\___\\__,_|_| |_|_| |_|\\___|_|   ')
	print('\n\n')             
	print('===============================================================================')                                                                
	print('========================== Written by Luke Cowan ==============================')
	print('===============================================================================\n\n')
	print('Checking keywords against new pastes...\n')



	### Gets paste_keys and formats them down to the list 'raw_keys'
	data =requests.get('https://www.pastebin.com')
	temp = re.findall(r'a href="/[A-Za-z0-9]{8}"', data.text)
	temp = temp[2:10]
	raw_keys = []
	for i in temp:
		raw_keys.append(i[9:-1])


	### Gets keys to ignore from ignore_keys.txt and puts them in list 'ignore_keys'
	x = open('ignore_keys.txt', 'r+')
	ignore_keys = []
	for i in x.read().split('\n'):
		ignore_keys.append(i)


	### Take raw_keys and sees if they are in ignore_keys. If so, nothing happens
	### If not they are loaded into list 'paste_keys'
	paste_keys = []
	for i in raw_keys:
		if i in ignore_keys:
			pass
		else:
			paste_keys.append(i)

	### Takes list 'paste_keys' and appends them to ignore_keys.txt
	for i in paste_keys:
		q = open('ignore_keys.txt', 'a+')
		q.write(i + '\n')
		q.close()


	### Loads keywords to list 'keywords' from keywords.txt
	x = open('keywords.txt', 'r+')
	keywords = []
	for i in x.read().split('\n'):
		keywords.append(i)

	
	for i in paste_keys:
		print(f'New paste key: {i}')
		time.sleep(.5)

	trigger = 0	
	for key in paste_keys:
		paste_data = requests.get(f'https://www.pastebin.com/raw/{key}')
		for word in keywords:
			if re.findall(f'{word}', paste_data.text):
				print(f'\nMatch! Found a match to the following pattern/word: {word}.')
				print(f'Creating text file with the paste information...')
				temp = paste_data.text
				x = open(f'{key}.txt', 'a+', encoding='utf-8')
				x.write(f'Matched the following: {word}\n\n\n\n')
				x.write(temp)
				x.close()
				print(f'Success! {key}.txt saved successfully!')
				trigger += 1
			else:
				pass


	if trigger == 0:
		print(f'\nNo matches. Checked {len(paste_keys)} paste(s).\nChecking again in fifty seconds.\n')
	else:
		print(f'\nMatched {trigger} paste(s). They have been saved.')
		print(f'Checking again in fifty seconds...')
	time.sleep(50)
	os.system('cls')










