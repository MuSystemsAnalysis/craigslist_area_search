# Craigslist City Scraper
# By Marshall Ehlinger
# For sp2015 Systems Analysis and Design

from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup(requests.get("http://www.craigslist.org/about/sites").text)

placesDict = {}

for state in soup.find_all("h4"):
	areaList = []
	stateStr = state.text
	for area in state.next_sibling.next_sibling:
		if area != '\n':
			areaList.append(area.string)
	placesDict[stateStr] = areaList

#print(placesDict)

print(placesDict['Alabama'])
print(placesDict['Oregon'])
print(placesDict['Texas'])

