# =====================================
# DSML Chatbot 2017
# Author(Minchul,Taekyung)
# Maintain(Minchul, wow@suwon.ac.kr)
#======================================
# ----- ABSTRACT CLASS -----
class Answer:
    def __init__(self,question):
        self.sineages=[]
        self.answer_bin=[]
        self.j=False
        self.question=question
    def makeAnswer(self):
        self.baseKeyboard = {
            "type": "buttons",
            "buttons": self.buttons,
        }
        self.baseMessage = {
            "message": {
                "text": self.answer,
            },
            "keyboard": self.baseKeyboard
        }
    def evaluate(self):
        self.j=self.question in self.answer_bin
    def send_keyboard(self):
        msg= {"type":"buttons","buttons":self.sineages,}
    def find(self):
        return self.j
class SubAnswer(Answer):
    def __init__(self,ans,but):
        Answer.__init__(self,ans,but)
        self.makeAnswer()
    