Craigslist Scraper
=================

What is this?
-----
This is a web-scraper that will take in a single string as an argument, search craigslist in all
American regions/cities as defined by craigslist's regional breakdown, and return the regions in
which the term appears in the title of a for sale posting. The data will then be returned as a
list.


DEPENDENCIES
----
* Python3 3.4.3
* Beautiful Soup 4.4.0
* Requests 2.7.0

The results of "pip freeze" inside of the virtualenv are available under requirements.txt


Issues and To-Do
----
* the areaScraper needs to return --only-- American (U.S.) cities/regions
* the areas need to be parsed so that they can be used to search craigslist.org efficiently
* a method needs to be written to take a string and search all the above ares for >= 1 match
* the results of the search should be stored in some sensible fashion
* this project is very vague.
