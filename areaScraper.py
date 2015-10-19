#!/usr/bin/python3.4

# Craigslist City Scraper
# By Marshall Ehlinger
# For sp2015 Systems Analysis and Design

# Returns dictionary of 'city name string' : 'site url'
# for all American cities in states/territories @ CL

from bs4 import BeautifulSoup
import re

def getCities():

	fh = open("sites.htm", "r")
	soup = BeautifulSoup(fh, "html.parser")
	placesDict = {}

	for columnDiv in soup.h1.next_sibling.next_sibling:
		for state in columnDiv:
			for city in state:
				m = (re.search('<li><a href="(.+)">(.+)</a>', str(city)))
				if m:			
					placesDict[m.group(2)] = m.group(1)

	return(placesDict)

