from flask import Flask, jsonify
import lamp_genie
app = Flask(__name__)

@app.route("/lampgenie", methods=['GET', 'POST'])
def hello():
    desc = """
    <html>
    <head></head>
    <body>
    <h1>aladin used book search api</h1>
    <div>
    검색 방법.<br/>
    /lampgenie/search/검색어 로 검색한다. 한 2분쯤 걸리니 당황하지 않았으면 좋겠다....
    </div>
    </body>
    </html>
    """
    return desc

@app.route("/lampgenie/search/<text>", methods=['GET', 'POST'])
def search(text):
    input_txt = text.encode('cp949')
    data = lamp_genie.search_from_all(input_txt)
    return jsonify(data)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
