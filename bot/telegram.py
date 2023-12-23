import telebot
import os
from dotenv import load_dotenv
import time
import fastapi
from fastapi import Request
from pydantic import BaseModel
from typing import Union
import uvicorn
import logging
import threading
from icecream import ic

#from graphic_generator import *
from new_graphic_generator import *


#from bot.OLD.startup import startup

#startup()


load_dotenv()
TOKEN = os.getenv('TOKEN')
WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
WEBHOOK_PORT = 443
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (TOKEN)

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(TOKEN, parse_mode='HTML') # You can set parse_mode by default. HTML or MARKDOWN
app = fastapi.FastAPI(docs=None, redoc_url=None)
app.type = "00"
class Winner(BaseModel):
    tele_user: Union[str, int, None]
    winner: Union[str, None]




#list of people who are still generating their answer
generating = []

# Empty webserver index, return nothing, just http 200
@app.get('/')
def index():
    return ''


bot.delete_my_commands(scope=None, language_code=None)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("/start", "Starts the bot!"),
        telebot.types.BotCommand("/help", "Help"),
		telebot.types.BotCommand("/winner", "Starts to spin the wheel!")
    ],
    # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command for users
    # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	reply_message = """Welcome to IndecisiveBot! This is a bot designed to help you <b>REALLY DECISIVE PEOPLE</b> decide stuff on Telegram! To get started, use /winner, or click the menu button below!
    
        /winner example:
        -------
        /winner option1 option2 option3
        -------
    """
	bot.reply_to(message, reply_message)
	
@bot.message_handler(commands=['winner'])
def winner(message):
    wheel_values = message.text.split()[1:]
    if len(wheel_values) == 0:
        bot.reply_to(message, "Sorry! Please input at least 1 option.")
    else:
        if str(message.chat.id) not in generating:
            generating.append(str(message.chat.id))

            bot.reply_to(message, "Deciding...")
            bot.send_chat_action(message.chat.id, 'typing')
            thread1 = threading.Thread(target=record_wheel, args=(message.chat.id, wheel_values))
            thread1.start()
            time.sleep(5)
            bot.send_chat_action(message.chat.id, 'typing')
            bot.send_message(message.chat.id, "Still deciding...")
            time.sleep(3)
            bot.send_chat_action(message.chat.id, 'typing')
            bot.send_message(message.chat.id, "Almost there...")
            bot.send_chat_action(message.chat.id, 'record_video')
            ic(pids)
        else:
            bot.reply_to(message, "Please wait for the previous wheel to finish spinning before you generate a new winner!")
            


@app.get('/finished')
def finished(tele_user: str, winner: str):
    ic(pids)
    stop_recording(tele_user)
    bot.send_chat_action(tele_user, 'upload_video')
    bot.send_animation(tele_user, animation=open('/data/output_{tele_user}.gif'.format(tele_user = tele_user), 'rb'))
    bot.send_chat_action(tele_user, 'typing')
    bot.send_message(tele_user, "Winner is: <span class='tg-spoiler'>" + winner + "!</span>")
    os.remove('/data/output_{tele_user}.gif'.format(tele_user = tele_user))
    generating.remove(tele_user)





@app.post(f'/{TOKEN}/')
def process_webhook(update: dict):
    """
    Process webhook calls
    """
    if update:
        update = telebot.types.Update.de_json(update)
        bot.process_new_updates([update])
    else:
        return


bot.remove_webhook()
time.sleep(0.1)
# Set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)
                #certificate=open(WEBHOOK_SSL_CERT, 'r'))

# uvicorn.run(
#     app,
#     host='0.0.0.0',
#     port=8001,
#     workers=1,
    
#     #ssl_certfile=WEBHOOK_SSL_CERT,
#     #ssl_keyfile=WEBHOOK_SSL_PRIV
# )

