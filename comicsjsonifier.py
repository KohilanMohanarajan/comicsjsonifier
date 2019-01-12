import requests
import json
from datetime import datetime, timedelta

# To be run on the sunday of each week
date = datetime.now()
future = timedelta(days=3)
new_date = date + future
day = str(new_date.day)
month = str(new_date.month)
year = str(new_date.year)

url = 'https://www.previewsworld.com/NewReleases/Export?format=txt&releaseDate=' + month + '/' + day + '/' + year
r = requests.get(url, allow_redirects=True)
open('weekscomics.txt', 'wb').write(r.content)

f = open('weekscomics.txt', 'r')

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
	if (line == "DYNAMITE"):
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
open('comicsweek_thisWeek.json', 'w').close()
outfile = open('comicsweek_thisWeek.json', 'w')

# Dump dictionary into JSON file
json.dump(weeksTitles, outfile)

# Close json file
outfile.close()