# Code for project 2 for UC Davis bootcamp
# written by George Bigham

from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from splinter.exceptions import ElementDoesNotExist
import requests
import time

# executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
# browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    # scrapes several sites and returns free stuff from 

    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

    # Go to sacramento cl and navigate to 1st item of free stuff

    url = "https://sacramento.craigslist.org/d/free-stuff/search/zip"
    browser.visit(url)
    browser.click_link_by_partial_href('https://sacramento.craigslist.org')
    time.sleep(2)

    # Using Splinter to scrape cl and store data in dict stuff (or pandas df)

    #stuff = pd.DataFrame(columns=['title','age', 'location'])
    stuff = {}
    stuff["title"] = []
    stuff["age"] = []
    stuff["coord"] = [] 

    for x in range(1, 4):
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find(id="titletextonly").text
        age = soup.find('time', class_="date timeago")["datetime"]
        loc = soup.find(id='map')
        coord = [loc["data-latitude"], loc["data-longitude"]]
        # condit = soup.find('p', class_="attrgroup")
        # cond = ''
        # if (condit and condit.b.text): cond = condit.b.text
    
        # stuff.loc[x] = [title, age, coord]
        stuff["title"].append(title)
        stuff["age"].append(age)
        stuff["coord"].append(coord)

        time.sleep(2)
        browser.click_link_by_partial_text('next')

    return stuff