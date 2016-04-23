#-*- coding: utf-8 -*-
import requests
import bs4  as BeautifulSoup
import sys

mobile_site_url = "http://www.aladin.co.kr"
search_url = "http://off.aladin.co.kr/usedstore/wsearchresult.aspx?SearchWord=%s&x=0&y=0"

def get_shoplist():
    response = requests.get(mobile_site_url + '/m/off/gate.aspx?')
    content = response.content
    shop_list = BeautifulSoup.BeautifulSoup(content).findAll('td')
    return shop_list

def parse_book(isbn):
    book_url = "http://off.aladin.co.kr/usedstore/wproduct.aspx?ISBN=%d"
    url = book_url % int(isbn)
    response = requests.get(url, )
    content = response.text
    result = BeautifulSoup.BeautifulSoup(content).find('div', {'class':'us_prod_info'})
    title = result.find('a', {'class':"bo_title"}).text
    try:
        print(url, title)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    s = requests.Session()
    search_text = requests.utils.quote(input("검색할 책 제목이나 글쓴이 : ").encode('cp949'))
    shop_list = get_shoplist()
    for x in shop_list:
        print ("=" * 50)
        try:
            shop_location = x.text
            print(shop_location)
            url = x.find('a')
            response = s.get(mobile_site_url + url['href'])
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
                for result in result_list:
                    parse_book(result)
            except:
                print(set())
        except Exception as e:
            pass
