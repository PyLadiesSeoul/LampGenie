#-*- coding: utf-8 -*-
import requests
import BeautifulSoup
import sys

def aladin_shoplist():
    result = []
    mobile_site_url = "http://www.aladin.co.kr"
    response = requests.get(mobile_site_url + '/m/off/gate.aspx?')
    content = response.content
    shop_list = BeautifulSoup.BeautifulSoup(content).findAll('td')
    for x in shop_list:
        url = x.find('a')
        if url:
            result.append((x.text, url['href']))
    return result

shop_list = aladin_shoplist()
for x in shop_list:
    print x[0], x[1]

