import requests
from bs4 import BeautifulSoup
import csv
import numpy as np
import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Demo@1234",
    database="DirectoryIm "
)

f = csv.writer(open('m2m-directory.csv', 'w'))
f.writerow(['Links', 'Title', 'Address', 'Telephone', 'Category'])

dash = ["https://www.directory.im/atoz-C.htm"]
for urls in dash:
 r = requests.get(urls ,verify=False)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class="azlist"] > ul > li > a')
 for company in companysData:
     links = 'https://www.directory.im'+company.get('href')
     rr1 = requests.get(links)		# r variable has all the HTML code
     soups = BeautifulSoup(rr1.content, 'html.parser')
     companysData123 = soups.select('div[class="listing-left"] > h3 > a')
     for company12345 in companysData123:
        links456 = 'https://www.directory.im'+company12345.get('href')
        rr123 = requests.get(links456)
        soups789 = BeautifulSoup(rr123.content, 'html.parser')
        for title in soups789.select('div[class="listing-left"] > h1'):
            title = title.text.strip()
        for add in soups789.select('div[class="listing-left"] > p[class="listing-add"]'):
            add = add.text.strip()
        telephones = []
        for telephone in soups789.select('ul[class="listing-cont"] > li'):
            telephoness = telephone.text.strip()
            telephones.append(telephoness)
        Categoryyy = []
        for categories in soups789.select('div[class="listing-category"]'):
             Categoryyyss = categories.text.strip().replace("Categories: ", "").rstrip().replace("  ", "")
             Categoryyy.append(Categoryyyss)
             csvCategorydirc = ",".join(Categoryyy)
             csvtelephones = ",".join(telephones)
             info = [links456, title, add, csvtelephones, csvCategorydirc]
             print(info)
             mycursor = cnx.cursor()
             sql = "INSERT INTO Imdirectory2 (Links,Title,Address,Telephone,Category) VALUES (%s, %s, %s, %s, %s)"
             val = (links456, title, add, csvtelephones, csvCategorydirc)
             mycursor.execute(sql, val)
             cnx.commit()
             break
