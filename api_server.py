from flask import Flask, jsonify
from pymongo import MongoClient
import lamp_genie
from datetime import datetime, timedelta
import json
app = Flask(__name__)
mongo = MongoClient('localhost', 27017)
mongodb = mongo.aladin

@app.route("/lampgenie", methods=['GET'])
def hello():
    desc = """
    <html>
    <head></head>
    <body>
    <h1>aladin used book search api</h1>
    <div>
    검색 방법.<br/>
    /lampgenie/search/검색어 로 검색한다. 한 2분쯤 걸리니 당황하지 않았으면 좋겠다....
    /lampgenie/shoplist 모든 상점<br/>
    /lampgenie/{location}/{검색어} 해당 상점의 검색결과. ex) /lampgenie/gangnam/건담 <br/>
    </div>
    </body>
    </html>
    """
    return desc

@app.route("/lampgenie/shoplist", methods=['GET'])
def shoplist():
    mongo_shoplist = mongodb.shoplist
    cache_shop = mongo_shoplist.find({'last_update':{'$exists': True}})
    for r in cache_shop:
        if datetime.now() - r['last_update'] <= timedelta(hours=1):
            r.pop("_id", None)
            return jsonify(r)
        else:
            cache_shop = {}
    try:
        shoplist = lamp_genie.get_shoplist()
        result = {}
        for shop in shoplist:
            s = str(shop).split("offcode=")
            if s.__len__() > 1:
                code = str(s[1]).split("\">")[0]
                result[shop.text] = code 
        result['last_update'] = datetime.now()
    except Exception as e:
        print(e)
    r.update(result)
    mongo_shoplist.save(r)
    return jsonify(result)

@app.route("/lampgenie/<shop>/<text>", methods=['GET', 'POST'])
def search_byshop(shop, text):
    base_url = "http://www.aladin.co.kr/m/off/main.aspx?offcode="+shop
    data = lamp_genie.search(base_url, text.encode('cp949'))
    return jsonify(data)

@app.route("/lampgenie/search/<text>", methods=['GET', 'POST'])
def search(text):
    input_txt = text.encode('cp949')
    data = lamp_genie.search_from_all(input_txt)
    return jsonify(data)

    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
