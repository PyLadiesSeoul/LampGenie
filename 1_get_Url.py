import requests
import BeautifulSoup

mobile_site_url = "http://www.aladin.co.kr/m/off/gate.aspx?"

response = requests.get(mobile_site_url)
content = response.content

shop_list = BeautifulSoup.BeautifulSoup(content).findAll('td')

for x in shop_list:
    print "=" * 50
    print x.text
