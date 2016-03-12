# LampGenie
파이썬으로 알라딘 오프매장 책 검색 한번에 하기.

# 돌리는 법.
'''
    hinyeajis-MacBook-Pro:pyladies-lampgenie yeaji$ python3 lamp_genie.py
    검색할 책 제목이나 글쓴이 : 드래곤볼
    /usr/local/lib/python3.4/site-packages/bs4/__init__.py:166: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.
    
    To get rid of this warning, change this:
    
     BeautifulSoup([your markup])
    
    to this:
    
     BeautifulSoup([your markup], "html.parser")
    
      markup_type=markup_type))
    ==================================================
    알라딘 중고매장
    ==================================================
    강남점
    http://off.aladin.co.kr/usedstore/wproduct.aspx?ISBN=1421526646 Dragonball (Paperback, Reissue)
    ==================================================
    건대점
    set()
    ==================================================
    광주점
    http://off.aladin.co.kr/usedstore/wproduct.aspx?ISBN=8925242885 드래곤볼 에볼루션 1
    http://off.aladin.co.kr/usedstore/wproduct.aspx?ISBN=8994700927 드래곤 플라이트 히스터리 탐험대 2
'''
    
# 튜토리얼 따라가기.
1. Branch의 순서대로 따라가면 된다.
2. 일단 1_get_shop_list 을 열어서 따라가면 된다.
3. 이후로는 2_... 식으로 따라간다.
