# =====================================
# DSML Chatbot 2017
# Author(Minchul,Taekyung)
# Maintain(Minchul, wow@suwon.ac.kr)
#======================================
from flask import Flask, request, jsonify
from answer import *
app = Flask(__name__)
# ----- INTERFACE ------
def getAnswer(question):
    url = 'https://westus.api.cognitive.microsoft.com/qnamaker/v2.0/knowledgebases/{my-key}/generateAnswer'
    headers = {'Content-Type':'application/json; charset=utf-8',
                'Ocp-Apim-Subscription-Key':'{hidden}'}
    data = json.dumps({"question": question})
    r = requests.post(url, headers=headers, data=data)
    rjson = json.loads(r.text)
    answer = rjson.get('answers')[0]['answer']
    return answer
# ----- MAIN PAGE -----
@app.route('/')
def hello_world():
    return 'Hello World!'
# ----- SINEAGE ------
@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type": "buttons",
        "buttons": ["안녕하세요"]
    }
    return jsonify(dataSend)
# ----- MSG PASSED BY AZURE -----
@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    # 챗봇 구현부
    
    
    #dataSend로 만들어서 보내야 함
    return jsonify(dataSend)




if __name__ == '__main__':
    app.run()
