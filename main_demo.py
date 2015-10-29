# Craigslist Scrape n' Search
# Command-Line Demonstration Version

import scrapeSites, getSearchString, urlCombine, checkPage, saveToDatabase

citiesWithHits= []

# Uncomment this line to get the full list of cities from cragslist's sites.htm
# as saved to the same directory as this script
#regionUrls = getCities() 

# Uncomment the below line to use three arbitrary sites to avoid IP-banning
regionUrls = {"Lincoln" : 'http://lincoln.craigslist.org', "SF Bay" : 'http://sfbay.craigslist.org', "Fart Collins" : 'http://fortcollins.craigslist.org'}

searchString = getSearchString.getSearchString()
regionSearchStringUrls = urlCombine.combine(regionUrls, searchString)

for key, value in regionSearchStringUrls.items():
	if checkPage.thereAreResults(value):
		citiesWithHits.append(key)

print("The following cities had at least one match\nfor the search term " + searchString + ":")
for city in citiesWithHits:
	print(city)
saveToDatabase.saveCityNamesToDatabase(citiesWithHits)
