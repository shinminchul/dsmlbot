class Answer:
    def __init__(self, ans, but):
        self.answer = ans
        self.buttons = but

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
