import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium.webdriver.support.ui
import selenium.webdriver.chrome.options
import csv

f = csv.writer(open('all-business-data.csv', 'w'))
f.writerow(['Name','Description','Contact Details'])

option = webdriver.FirefoxOptions()
option.add_argument('headless')
driver = webdriver.Firefox()
# Making a GET request
driver.get('https://www.jerseyfinance.je/business-directory/accuro-trust-jersey-limited/')
html = driver.page_source
# check status code for response received
# success code - 200
#soup = BeautifulSoup(html)
# Parsing the HTML
soup = BeautifulSoup(html , features="lxml")
companysData = soup.select('div[class="c-grid__item c-business"]')
for company in companysData:
    for title in company.select('img[class="member-logo u-mb-20 "]'):
        title = title.text
        print(title)
