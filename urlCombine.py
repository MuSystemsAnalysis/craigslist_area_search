#!/usr/bin/python3.4
# By Chris Hume on 10/26/15

# Combine a dictionary of city:url with search string into a dictionary of
# City : Search url

def combine(initialDict, search):	
	for key, value in initialDict.items():
		value  += "/search/sss?query=" + search + "&sort=rel"
		initialDict[key] = value
	return initialDict;

