# Craigslist City Scraper
# By Marshall Ehlinger
# For sp2015 Systems Analysis and Design

from bs4 import BeautifulSoup
import re

fh = open("sites.htm", "r")
soup = BeautifulSoup(fh, "html.parser")

for columnDiv in soup.h1.next_sibling.next_sibling:
	for state in columnDiv:
		for city in state:
			print(city)

#print(soup.text)
print("\n----Done----\n\n")
