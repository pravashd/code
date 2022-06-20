from click import echo
import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('iom_commerc1233e.csv', 'w'))
f.writerow(['Links','Company Name','Description', 'Person Name', 'Phone Number', 'EmailAddress','Web Address'])

dash = ["https://www.iomchamber.org.im/members/"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysDatass = soup.select('nav[class*="pagination"] ul > li > a')
for company in companysDatass:
      links = "https://www.iomchamber.org.im/members/"+company.get('href')
      rr = requests.get(links)		# r variable has all the HTML code
      soups = BeautifulSoup(rr.content, 'html.parser')
      #print(links)
      for companyName in soups.select('div[class="member-content"] > h3'):
          companyName = companyName.text
      for description in soups.select('div[class="member-content"] > p'):
          description = description.text
      for person in soups.findChildren("i" , {'class': "fas fa-user"}):
          person = person.parent.text
      for telephone in soups.findChildren("i" , {'class': "fa fa-phone"}):
         telephone = telephone.parent.text
      for  email in soups.findChildren("i" , {'class': "fa fa-envelope"}):
          email = email.parent.text
      for webaddress in soups.findChildren("i" , {'class': "fa fa-desktop"}):
          webaddress = webaddress.parent.text
          info = [links,companyName,description, person, telephone,email,webaddress]
          print(info)
          break
         # f.writerow(info)
