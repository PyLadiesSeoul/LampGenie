import requests
from bs4 import BeautifulSoup

domain = "https://weworkremotely.com"
urls = []
content = requests.get(domain).content
categories = BeautifulSoup(content).findAll('h2')
for category in categories:
    url = category.find('a')
    urls.append(domain+url['href'].replace('#intro',''))

for url in urls:
    print "="*10 + url + "="*10
    content = requests.get(url).content

    jobs = BeautifulSoup(content).findAll('li')

    for job in jobs:
        try:
            url = job.find('a')
            if url:
                company = job.find('span', {'class':"company"}).text
                title = job.find('span', {'class':"title"}).text
                date = job.find('span', {'class':"date"}).text
                print '-'*50
                print 'company :', company
                print 'title :', title
                print 'date:', date
                print domain+url['href']
        except Exception as e:
            print e
