# =====================================
# DSML Chatbot 2017
# Author(Minchul,Taekyung)
# Maintain(Minchul, wow@suwon.ac.kr)
#======================================
# ----- ABSTRACT CLASS -----
import re
class Answer:
    def __init__(self,question):
        self.sineages=[]
        self.j=False
        self.question=question
        answer_marker="어떤 것이 궁금해요?"
    def evaluate(self):
        self.j=self.question.endswith(self.answer_marker)
        return self.j
    def send_keyboard(self,qna):
        msg= {"message":{"text":qna},"keyboard":{"type":"buttons","buttons":self.sineages}}
        return msg
    def find(self):
        return self.j
# --- INTERFACE -----
class AboutAnswer(Answer):
    def __init__(self,question):
        Answer.__init__(self,question)
        answer_marker="DSML에 관하여"
        self.sineages=['DSML의 약자는요?','DSML은 어떻게 태어났어요?','DSML 사무실은요?','DSML 센터는 뭐하는 곳인가요?']
class ProgramAnswer(Answer):
    def __init__(self,question):
        Answer.__init__(self,question)
        answer_marker="DSML의 프로그램에 관하여"
        self.sineages=['수업 지원','멘토링 프로그램','연구 지원','산학협력']
class InfoAnswer(Answer):
    def __init__(self,question):
        Answer.__init__(self,question)
        answer_marker="데이터 과학이나 머신러닝에 관하여"
        self.sineages=['데이터 과학','머신러닝']
class FunAnswer(Answer):
    def __init__(self,question):
        Answer.__init__(self,question)
        answer_marker="기타 궁금한 점"
    def send_keyboard(self,qna):
        msg={"message":{"text":qna},"keyboard":{"type":"text"}}
        return msg