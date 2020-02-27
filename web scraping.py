# import the library used to query a website

import urllib.request
# specify the url
wiki= "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

# Query the website and return the html to the variable 'page'

page = urllib.request.urlopen(wiki)
print(page)
# import the BeautifulSoup functions to parse the data returned from the website
from bs4 import BeautifulSoup
# prase the html page in the 'page' variable, and store it in Beautiful Soup format
soup=BeautifulSoup(page)
print(soup)
