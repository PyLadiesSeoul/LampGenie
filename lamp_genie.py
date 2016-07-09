#-*- coding: utf-8 -*-
import requests
import bs4  as BeautifulSoup
import sys

mobile_site_url = "http://www.aladin.co.kr"
# [TODO] search all page. - consider api rule.
search_url = "http://off.aladin.co.kr/usedstore/wsearchresult.aspx?SearchWord=%s&x=0&y=0&page=1"

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
        return (str(title), url)
    except Exception as e:
        print(e)

def search(location_url, text):
    text = requests.utils.quote(text)
    s = requests.Session()
    response = s.get(location_url)
    url = search_url % text
    response = s.get(url)
    content = response.content
    result = BeautifulSoup.BeautifulSoup(content).find('div', {'id':'Search3_Result'})
    book_list = []
    try:
        result_list = set()
        for x in result.findAll('a'):
            search_code = str(x).split('ISBN=')
            if search_code.__len__() > 1:
                isbn = search_code[1].split('"')[0]
                result_list.add(isbn)
        for result in result_list:
            book_list.append(parse_book(result))
    except:
        pass
    return book_list

def search_from_all(text):
    shop_list = get_shoplist()
    book_list = {}
    for x in shop_list:
        try:
            shop_location = x.text
            url = x.find('a')
            book_list[shop_location] = search(mobile_site_url + url['href'], text)
        except Exception as e:
            pass
    return book_list

if __name__ == '__main__':
    input_txt = input("검색할 책 제목이나 글쓴이 : ").encode('cp949')
    for book in search_from_all(input_txt):
        print(book)
