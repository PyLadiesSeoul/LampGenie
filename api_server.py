from flask import Flask, jsonify
import lamp_genie
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return "aladin used book search api"

@app.route("/search/<text>", methods=['GET', 'POST'])
def search(text):
    input_txt = text.encode('cp949')
    data = lamp_genie.search_from_all(input_txt)
    return jsonify(data)
    

if __name__ == "__main__":
    app.run()
