import telepot
from Chatbot import Chatbot

telegram = telepot.Bot('620827053:AAFomD5guWm00hAopL096sST6M6HVwff5UI')
bot = Chatbot("HashLDash")

def inMsg(msg):
    print(msg['text'])

telegram.message_loop(inMsg)

while True:
    pass