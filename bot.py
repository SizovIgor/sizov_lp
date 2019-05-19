from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}
API_KEY = "706687382:AAFCm5L0-Be5wmyPtldr82zNG5Mb71-IJlE"

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def greet_update(bot, update):
    text = 'Вызван /update'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def commit(bot, update):
    eval()

def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("update", greet_update))
    dp.add_handler(CommandHandler("commit", commit))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()
