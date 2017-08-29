from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type": "buttons",
        "buttons": ["안녕하세요"]
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    # 챗봇 구현부
    
    
    #dataSend로 만들어서 보내야 함
    return jsonify(dataSend)


def getKeybyQuestion(Question):
    answermap={
        "처음으로 돌아가기":"q",
        "q1":"데이터사이언스, 머신러닝이 궁금해요",
        "q1a":"빅데이터가 무엇인가요?",
        "q1b":"기계학습(Machine Learning)이 무엇인가요?",
        "q1c":"데이터 과학은 무엇인가요?"
    }
    return answermap.get(Question)


if __name__ == '__main__':
    app.run()
