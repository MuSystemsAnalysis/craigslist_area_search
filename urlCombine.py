#!/usr/bin/python3.4
# By Chris Hume on 10/26/15

# Combine a dictionary of city:url with search string into a dictionary of
# City : Search url

# Marshall's initial dictionary & Keenan's search string.
initialDict = {'Scranton' : 'https://scranton.craigslist.org', 'Mansfield': 'https://mansfield.craigslist.org'} 
search = "iphone"

def combine(initialDict, search):	
	for key, value in initialDict.items():
		value  += "/search/sss?query=" + search + "&sort=rel"
		initialDict[key] = value
	return initialDict;

# Dictionary being passed to Jarrod.
finalDict = combine(initialDict, search)

for key, value in finalDict.items():
	print(key, ":", value)



