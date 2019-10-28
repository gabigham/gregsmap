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

    # Using Splinter to scrape cl and store data in dataframe stuff (clean up condition)

    stuff = pd.DataFrame(columns=['lat', 'long','age', 'title'])

    for x in range(1, 4):
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find(id="titletextonly").text
        age = soup.find('time', class_="date timeago")["datetime"]
        loc = soup.find(id='map')
        lat = loc["data-latitude"]
        long = loc["data-longitude"]
    
        stuff.loc[x] = [lat, long, age, title]
        time.sleep(2)
        browser.click_link_by_partial_text('next')

    return stuff

    