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

dash = ["https://www.directory.im/"]
for urls in dash:
    r = requests.get(urls ,verify=False)  # r variable has all the HTML code
    soup = BeautifulSoup(r.content, 'html.parser')
    companysData = soup.select('div[class="azselect-home"] > ul > li > a')
    for company in companysData:
        links = 'https://www.directory.im' + company.get('href')
        companylist = requests.get(links)  # r variable has all the HTML code
        companySoup = BeautifulSoup(companylist.content, 'html.parser')
        companylinks = companySoup.select('div[class="azlist"] > ul > li > a')
        for companyinfo in companylinks:
            companylinks = 'https://www.directory.im' + companyinfo.get('href')
            companylinkss = requests.get(companylinks)  # r variable has all the HTML code
            companylinksSoup = BeautifulSoup(companylinkss.content, 'html.parser')
            companylinksfile = companylinksSoup.select('div[class="listing-left"] > h3 > a')
            for companyfile in companylinksfile:
                compfile = 'https://www.directory.im' + companyfile.get('href')
                companyfilelist = requests.get(compfile)  # r variable has all the HTML code
                companyfieSoups = BeautifulSoup(companyfilelist.content, 'html.parser')
                for title in companyfieSoups.select('div[class="listing-left"] > h1'):
                    title = title.text.strip()
                for add in companyfieSoups.select('div[class="listing-left"] > p[class="listing-add"]'):
                    add = add.text.strip()
                telephones = []
                for telephone in companyfieSoups.select('ul[class="listing-cont"] > li'):
                    telephoness = telephone.text.strip()
                    telephones.append(telephoness)
                Categoryyy = []
                for categories in companyfieSoups.select('div[class="listing-category"]'):
                    Categoryyyss = categories.text.strip().replace("Categories: ", "").rstrip().replace("  ", "")
                    Categoryyy.append(Categoryyyss)
                    csvCategorydirc = ",".join(Categoryyy)
                    csvtelephones = ",".join(telephones)
                    info = [compfile, title, add, csvtelephones, csvCategorydirc]
                    print(info)
                    mycursor = cnx.cursor()
                    sql = "INSERT INTO directory_im (Links,Title,Address,Telephone,Category) VALUES (%s, %s, %s, %s, %s)"
                    val = (compfile, title, add, csvtelephones, csvCategorydirc)
                    mycursor.execute(sql, val)
                    cnx.commit()
                    break



