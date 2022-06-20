import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('2GJT-directory.csv', 'w'))
f.writerow(['Links','Company Name','Address','Telephone','Mobile','Description','Tags'])
#dash = "https://www.jtdirectory.com/browse/listing/" + number +"/G"
number = 2
while number <= 544:
 try:
  url = "https://www.jtdirectory.com/browse/listing/" + str(number) +"/G"
  r = requests.get(url)		# r variable has all the HTML code
  soup = BeautifulSoup(r.content, 'html.parser')
  lists = soup.select('div[class="listing-result row"] > div[class="col-sm-3"] p > a')
  for list in lists:
    companyurl = "https://www.jtdirectory.com"+list.get("href")
    rr = requests.get(companyurl)		# r variable has all the HTML code
    soups = BeautifulSoup(rr.content, 'html.parser')
    jtdata = soups.select('div[class="listing-full-map"]')
    for jit in jtdata:
        for companyname in jit.select('div[class="block-title"] > h3'):
            companyname = companyname.text.strip()
        print(companyname)
        adds = ''
        for add in jit.select('span[itemprop="address"]'):
            if(add.text != ''):
                 adds = add.text.strip()
        telephones = ''
        for telephone in jit.findChildren("i" , {'class': "fa fa-phone-alt"}):
            if(telephone.parent.text != ''):
                telephones = telephone.parent.text.strip()
        mobs = ''
        for mob in jit.findChildren("i" , {'class': "fa fa-mobile"}):
            if(mob.parent.text != ''):
                 mobs = mob.parent.text.strip()
        for description in jit.select('div[class="panel-body"] > div[class="description"]'):
            description = description.text.strip()
        for tags in jit.select('span[class="main-tags"]'):
            tags = tags.text.strip()
            info = [companyurl,companyname,adds,telephones,mobs,description,tags]
            print(info)
            f.writerow(info)
 except Exception as e:
        print("Failed to parse", e)
        pass