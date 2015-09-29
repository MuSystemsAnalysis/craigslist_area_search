# Craigslist City Scraper
# By Marshall Ehlinger
# For sp2015 Systems Analysis and Design

from bs4 import BeautifulSoup
import requests
import re

soup = BeautifulSoup(requests.get("http://www.craigslist.org/about/sites").text, "html.parser")

for columnDiv in soup.h1.next_sibling.next_sibling:
	for state in columnDiv:
		for city in state:
			print(city)
print("\n----Done----\n\n")
