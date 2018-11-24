from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

PROXY={'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
    
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
logger = logging.getLogger(__name__)

def greet_user(bot, update):
    text = 'Вызван /start'
    print(update)
    logger.info(text)
    update.message.reply_text(text)


def main():
    mybot=Updater('786822524:AAGxqc7Bikm0ugAnEt01u2POQSrm_fHFEms', request_kwargs=PROXY)
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    mybot.start_polling()
    mybot.idle()
   



main()
