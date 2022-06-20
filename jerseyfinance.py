import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv


driver = webdriver.Firefox()
# Making a GET request
#driver.get('https://www.jerseyfinance.je/business-directory/')
#html = driver.page_source
# check status code for response received
# success code - 200
#soup = BeautifulSoup(html, features='lxml')
# Parsing the HTML
#soup = BeautifulSoup(r.content, 'html.parser')
f = csv.writer(open('m-directory.csv', 'w'))
f.writerow(['Links','Title','Address','Telephone/Fax'])

dash = ['https://www.jerseyfinance.je/business-directory/']
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, features='lxml')
 print(soup)