from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from emoji import emojize
import requests
import logging
import config

config = config.get_config('settings.ini')
# Настройки прокси

# PROXY_socks_h = {'https': "socks5h://learn:python@t3.learn.python.ru:1080"}
PROXY_socks = {'https': "socks5h://learn:python@t3.learn.python.ru:1080"}
PROXY = {'proxy_url': 'socks5{}://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

API_KEY = "862054662:AAEgkDdlQ3lh6S-XMfJtpmyT_z-eFapbcJU"

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=config.get('Logging', 'Loglevel'),
    filename=config.get('Logging', 'Filename')
)

USER_EMOJI = config.get('Settings', 'USER_EMOJI')


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
    user_text = update.message.text
    print('Вызван /commit', 'git commit -m {}'.format(user_text))
    update.message.reply_text('git commit -m {}'.format(user_text.split()[1]))
    eval('git commit -m {}'.format(user_text.split()[1]))
    eval('git push')
# def commit(bot, update):
#     text = 'Вызван /commit'
#     print(text)
#     update.message.reply_text(update.message.text)

def main():
    # if requests.get('https://web.telegram.org', proxies=PROXY_socks_h).ok:
    if requests.get('https://web.telegram.org', proxies=PROXY_socks).ok:
        PROXY['proxy_url'] = PROXY['proxy_url'].format('h')
        print('Correct proxy: {}'.format(PROXY))
    else:
        PROXY['proxy_url'] = PROXY['proxy_url'].format('')
        print('Correct proxy: {}'.format(PROXY))
    mybot = Updater(API_KEY, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("update", greet_update))
    dp.add_handler(CommandHandler("commit", commit))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()
# request_kwargs=PROXY,
