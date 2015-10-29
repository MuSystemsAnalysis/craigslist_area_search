Craigslist Scraper
=================

What is this?
-----
This is a web-scraper that will take in a single string as an argument, search craigslist in all
American regions/cities as defined by craigslist's regional breakdown, then take a user defined
search string. It will then search each area for that string (as a for-sale listing) and add the
city to a results list if it has at least one hit. The list of cities with hits is then saved to
a local sqlite database named test.db.

This is a project for Fa2015 Systems Analysis and Design.


DEPENDENCIES
----
* Python3 3.4.3
* Beautiful Soup 4.4.1
* SQLite3.8.6

These requirements should be checked against requirements.txt for accuracy.

ALSO: use the included copy of sites.html in lieu of repeatedly scraping craigslist.
That is frowned upon, and they will ban me/you/us.
