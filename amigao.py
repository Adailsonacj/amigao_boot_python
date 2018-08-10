import telepot

bot = telepot.Bot('620827053:AAFomD5guWm00hAopL096sST6M6HVwff5UI')

def inMsg(msg):
    print(msg['text'])

bot.message_loop(inMsg)

while True:
    pass