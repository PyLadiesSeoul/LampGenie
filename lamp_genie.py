#-*- coding: utf-8 -*-
import requests
import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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

def search_aladin(search_txt, location):
    return result

mobile_site_url = "http://www.aladin.co.kr"
search_url = "http://off.aladin.co.kr/usedstore/wsearchresult.aspx?SearchWord=%s&x=0&y=0"
book_url = "http://off.aladin.co.kr/usedstore/wproduct.aspx?ISBN=%d"

search_text = requests.utils.quote(raw_input("검색할 책 제목이나 글쓴이 : ").encode('cp949'))
shop_list = aladin_shoplist()

s = requests.Session()
for x in shop_list:
    print "=" * 50
    try:
        shop_location = x[0]
        response = s.get(mobile_site_url + x[1])
        url = search_url % search_text
        response = s.get(url)
        content = response.content
        result = BeautifulSoup.BeautifulSoup(content).find('div', {'id':'Search3_Result'})
        try:
            result_list = set()
            for x in result.findAll('a'):
                search_code = str(x).split('ISBN=')
                if search_code.__len__() > 1:
                    isbn = search_code[1].split('"')[0]
                    result_list.add(isbn)
            print shop_location, result_list
        except:
            print set()
    except Exception as e:
        pass


