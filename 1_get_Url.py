# -*- coding:utf-8 -*-
# import란?
import requests
import BeautifulSoup

# string을 저장.
mobile_site_url = "http://www.aladin.co.kr/m/off/gate.aspx?"

# requests 모듈 사용하기.
response = requests.get(mobile_site_url)
content = response.content

# BeautifulSoup 사용하기.
shop_list = BeautifulSoup.BeautifulSoup(content).findAll('td')

# for문과 print 하기.
for x in shop_list:
    print "=" * 50
    print x.text
