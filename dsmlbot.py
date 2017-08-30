# =====================================
# DSML Chatbot 2017
# Author(Minchul,Taekyung)
# Maintain(Minchul, wow@suwon.ac.kr)
#======================================
from flask import Flask, request, jsonify
from answer import *
main_msg={"type":"buttons","buttons":[
    AboutAnswer.answer_marker,
    ProgramAnswer.answer_marker,
    InfoAnswer.answer_marker,
    FunAnswer.answer_marker]}
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
    return jsonify(main_msg)
# ----- MSG PASSED BY AZURE -----
@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    sign_board_1=[AboutAnswer(content),ProgramAnswer(content),InfoAnswer(content),FunAnswer(content)]
    check_1=list(lambda x:x.evaluate(),sign_board_1)
    try:
        obj = sign_board_1[check_1.index(True)]
        dataSend=obj.send_keyboard(getAnswer(obj.answer_marker))
    except ValueError:
        dataSend=main_msg
    return jsonify(dataSend)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000)
