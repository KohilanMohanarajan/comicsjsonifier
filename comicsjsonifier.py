import requests
import json
from datetime import datetime, timedelta

# To be run on the sunday of each week
date = datetime.now()
todayWeekday = date.weekday()
future = timedelta(days=0)
print(todayWeekday)
if (todayWeekday < 2):
	span = 2-todayWeekday
	future = timedelta(days=span)
elif (todayWeekday == 6):
	span = 3
	future = timedelta(days=span)
elif (todayWeekday > 2):
	span = (todayWeekday - 2) *(-1)
	future = timedelta(days=span)

new_date = date + future
print(new_date)
day = str(new_date.day)
month = str(new_date.month)
year = str(new_date.year)

nextweek = timedelta(days=10)
next_date = date + nextweek
nextDay = str(next_date.day)
nextMonth = str(next_date.month)
nextYear = str(next_date.year)


urls = ['https://www.previewsworld.com/NewReleases/Export?format=txt&releaseDate=' + month + '/' + day + '/' + year, 
		'https://www.previewsworld.com/shipping/releasestwoweeks.txt']

files = ['weekscomics.txt', 'nextweekscomics.txt']

jsons = ['comicsweek_thisWeek.json', 'comicsweek_nextWeek.json']

for i in range(0, len(urls)):
	url = urls[i]
	r = requests.get(url, allow_redirects=True)
	open(files[i], 'wb').write(r.content)

	f = open(files[i], 'r')
	print("Reading " + files[i] + "...")

	readBoom = False
	boomTitles = []
	readDark = False
	darkTitles = []
	readDC = False
	DCTitles = []
	readDynamite = False
	dynamiteTitles = []
	readIDW = False
	IDWTitles = []
	readImage = False
	imageTitles = []
	readMarvel = False
	marvelTitles = []

	weeksTitles = {}

	for line in f:
		line = line.rstrip()
		if (line == "BOOM! STUDIOS"):
			readBoom = True
		if (line == "DARK HORSE COMICS"):
			readDark = True
			readBoom = False
		if (line == "DC COMICS"):
			readDC = True
			readDark = False
		if (line == "DC COMICS/DC COLLECTIBLES"):
			readDC = False
		if (line == "DC COLLECTIBLES"):
			readDC = False
		if (line == "DYNAMITE" or line == "DYNAMITE ENTERTAINMENT"):
			readDynamite = True
			readDC = False
		if (line == "IDW PUBLISHING"):
			readIDW = True
			readDynamite = False
		if (line == "IMAGE COMICS"):
			readImage = True
			readIDW = False
		if (line == "MARVEL COMICS"):
			readMarvel = True
			readImage = False
		if (line == "DIAMOND SELECT TOYS LLC"):
			readMarvel = False
		if (line == "COMICS & GRAPHIC NOVELS"):
			readMarvel = False

		if (readBoom == True and line != ""):
			boomTitles.append(line)
		if (readDark == True and line != ""):
			darkTitles.append(line)
		if (readDC == True and line != ""):
			DCTitles.append(line)
		if (readDynamite == True and line != ""):
			dynamiteTitles.append(line)
		if (readIDW == True and line != ""):
			IDWTitles.append(line)
		if (readImage == True and line != ""):
			imageTitles.append(line)
		if (readMarvel == True and line != ""):
			marvelTitles.append(line)

	if (len(boomTitles) > 0):
		del boomTitles[0]
		itemcomps = {}
		for item in boomTitles:
			titlecomps = {}
			comps = item.split("\t")
			titlecomps["price"] = comps[2]
			titlecomps["title"] = comps[1]
			itemcomps[comps[0]] = titlecomps
		weeksTitles["BOOM! STUDIOS"] = itemcomps

	del darkTitles[0]
	itemcomps = {}
	for item in darkTitles:
		titlecomps = {}
		comps = item.split("\t")
		titlecomps["price"] = comps[2]
		titlecomps["title"] = comps[1]
		itemcomps[comps[0]] = titlecomps
	weeksTitles["DARK HORSE COMICS"] = itemcomps

	del DCTitles[0]
	itemcomps = {}
	for item in DCTitles:
		titlecomps = {}
		comps = item.split("\t")
		titlecomps["price"] = comps[2]
		titlecomps["title"] = comps[1]
		itemcomps[comps[0]] = titlecomps
	weeksTitles["DC COMICS"] = itemcomps

	del dynamiteTitles[0]
	itemcomps = {}
	for item in dynamiteTitles:
		titlecomps = {}
		comps = item.split("\t")
		titlecomps["price"] = comps[2]
		titlecomps["title"] = comps[1]
		itemcomps[comps[0]] = titlecomps
	weeksTitles["DYNAMITE COMICS"] = itemcomps

	del IDWTitles[0]
	itemcomps = {}
	for item in IDWTitles:
		titlecomps = {}
		comps = item.split("\t")
		titlecomps["price"] = comps[2]
		titlecomps["title"] = comps[1]
		itemcomps[comps[0]] = titlecomps
	weeksTitles["IDW COMICS"] = itemcomps

	del imageTitles[0]
	itemcomps = {}
	for item in imageTitles:
		titlecomps = {}
		comps = item.split("\t")
		titlecomps["price"] = comps[2]
		titlecomps["title"] = comps[1]
		itemcomps[comps[0]] = titlecomps
	weeksTitles["IMAGE COMICS"] = itemcomps

	del marvelTitles[0]
	itemcomps = {}
	for item in marvelTitles:
		titlecomps = {}
		comps = item.split("\t")
		titlecomps["price"] = comps[2]
		titlecomps["title"] = comps[1]
		itemcomps[comps[0]] = titlecomps
	weeksTitles["MARVEL COMICS"] = itemcomps

	# Open json file to store data for writing
	open(jsons[i], 'w').close()
	outfile = open(jsons[i], 'w')

	# Dump dictionary into JSON file
	json.dump(weeksTitles, outfile)

	# Close json file
	outfile.close()