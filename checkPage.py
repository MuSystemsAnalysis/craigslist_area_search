#!/usr/bin/python
# coding: utf-8
import urllib.request
import re

def areThereResults( agghhh ):
	#Create the soup object from the HTML data
	page = urllib.request.urlopen(agghhh).read()
		
	if not re.findall(b'no results', page):
		print("There was something there.")
		return True
		
	if re.findall(b'no results', page):
		print("No results were found.")
		return False
if __name__=="__main__":		
	argh = 'http://elmira.craigslist.org/search/sss?sort=rel&query=gimp%20suits'

	areThereResults( argh )
