# LampGenie
파이썬으로 알라딘 오프매장 책 검색 한번에 하기.
를 튜토리얼로 만듬.

# 돌리는 법 예시.

1. command line으로 실행하기.
  
    ```
    hinyeajis-MacBook-Pro:pyladies-lampgenie yeaji$ python3 lamp_genie.py
    검색할 책 제목이나 글쓴이 : 드래곤볼
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
    ```

2. web server api로 실행하기.

    ```
    root@ip-172-31-19-73:/home/ubuntu/LampGenie# python3 api_server.py
     * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)   
    ```
    
# 튜토리얼 따라가기.
1. Branch의 순서대로 따라가면 됩니다.
2. 일단 1_get_shop_list 을 열어서 따라갑니다.
3. 이후로는 2_... 식으로 따라갑니다. (번호순서)
4. 본 튜토리얼은 python3.5에서 작성되었습니다. 2에서 돌리려면 코드를 몇군데 수정해야 합니다.
