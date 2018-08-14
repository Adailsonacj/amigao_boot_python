import telepot
from Chatbot import Chatbot

telegram = telepot.Bot('620827053:AAFomD5guWm00hAopL096sST6M6HVwff5UI')

bot = Chatbot('Roberto')

def inMsg(msg):
    #print(msg['text'])
    frase = bot.escuta(frase=msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)
    #chatID = msg['chat']['id']
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, resp)


telegram.message_loop(inMsg)

while True:
    pass


#while True:
#    frase = Bot.escuta()
#    resp = Bot.pensa(frase)
#    Bot.fala(resp)
