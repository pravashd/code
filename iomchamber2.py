import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('m-directory.csv', 'w'))
f.writerow(['links','Title','Address','Telephone/Fax','Feature-List','About-Us'])

dash = ["https://www.directory.im/"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class="azselect-home"] > ul > li > a')
 for company in companysData:
     links = 'https://www.directory.im'+company.get('href')
     companylist = requests.get(links)		# r variable has all the HTML code
     companySoup = BeautifulSoup(companylist.content, 'html.parser')
     companylinks = companySoup.select('div[class="azlist"] > ul > li > a')
     for companyinfo in companylinks:
      companylinks = 'https://www.directory.im'+companyinfo.get('href')
      companylinkss = requests.get(companylinks)		# r variable has all the HTML code
      companylinksSoup = BeautifulSoup(companylinkss.content, 'html.parser')
     for title in companylinksSoup.select('div[class="listing-left"] > h3 > a'):
        title = title.text
     for add in companylinksSoup.select('p[class="listing-add"]'):
        add = add.text
     for telephone in companylinksSoup.select('ul[class="listing-cont"] > li'):
        telephone = telephone.text
     for featurelist in companylinksSoup.select('ul[class="feature-list"] > li'):
        featurelist = featurelist.text
     for aboutus in companylinksSoup.select('div[class="more-about-us"] > p'):
        aboutus = aboutus.text
     info = [companylinksSoup,title, add, telephone,featurelist,aboutus]
     print(info)
     #f.writerow(info)