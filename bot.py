from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
import requests
import logging
import config
import crypto
import ephem
from glob import glob
from random import choice
from emoji import emojize

from telegram import ReplyKeyboardMarkup

images_path = "C:\projects\learn_python_source\learn.python.ru\lessons\img\{}"
cats = glob(images_path.format("cat*.jp*g"))

config = config.get_config('settings.ini')
# Настройки прокси

PROXY_socks = {'https': "socks5h://learn:python@t3.learn.python.ru:1080"}
PROXY = {'proxy_url': 'socks5{}://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

API_KEY = b'K^][\x0c\x0c\x0f\x02AR.*|_Rp\x17\x04>XUP\x0fg^0"\rsLIY\n<0\x11\x14]\x7fU\x03\n\x0c!l'

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=config.get('Logging', 'Loglevel'),
    filename=config.get('Logging', 'Filename')
)
logger = logging.getLogger('bot_logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('bot_logger.log')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
USER_EMOJI = config.get('Settings', 'USER_EMOJI')


def log(func):
    def log_func(*args, **kwargs):
        logger.info('Start: {}'.format(func.__name__))
        print('Start: ', func.__name__)
        func(*args, **kwargs)
        print('Finished: ', func.__name__)

    return log_func


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
@log
def greet_user(bot, update, user_data):
    smile = emojize(choice(USER_EMOJI), use_aliases=True)
    print('Вызван /start')
    update.message.reply_text("Привет! {}".format(smile))


@log
def send_cat(bot, update, user_data):
    print('Вызваны котики')
    update.message.reply_text("Сейчас отправлю котика")
    images_path = "C:\projects\learn_python_source\learn.python.ru\lessons\img\{}"
    logger.info("Image path: {}".format(images_path))
    cats_pic = glob(images_path.format("cat*.jp*g"))
    logger.info(cats_pic)
    cat_pic = choice(cats_pic)
    logger.info(cat_pic)
    # update.message.reply_text(choice(cats))
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))
    logger.info('the photo was sending')


# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def greet_update(bot, update):
    text = 'Вызван /update'
    print(text)
    print(update)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def commit(bot, update):
    user_text = update.message.text
    print('Вызван /commit', 'git commit -m {}'.format(user_text))
    update.message.reply_text('git commit -m {}'.format(user_text.split()[1]))
    # eval('git commit -m {}'.format(user_text.split()[1]))
    # eval('git push')


def check_message(bot, update):
    update.message.reply_text('Вы выидите похожее сообщение в консоли?')
    print("Вы видите похожее сообщение от бота?")


@log
def wordcount(bot, update, user_data):
    # print("Вызвн /wordcount")
    words = update.message.text.split()
    update.message.reply_text(len(words[1:]))
    print(len(words[1:]))


@log
def emp(bot, update, user_data):
    moon = ephem.next_full_moon(datetime.datetime.now())
    moon = datetime.strptime(str(moon), "%Y/%m/%d %H:%M:%S")
    update.message.reply_text("Следующее полнолуние будет: {}".format(moon))
    print(moon, type(moon))


def main():
    # if requests.get('https://web.telegram.org', proxies=PROXY_socks_h).ok:
    logger.info('Initializing proxy')
    if requests.get('https://web.telegram.org', proxies=PROXY_socks).ok:
        PROXY['proxy_url'] = PROXY['proxy_url'].format('h')
        print('Correct proxy: {}'.format('socks5h'))
    else:
        PROXY['proxy_url'] = PROXY['proxy_url'].format('')
        print('Correct proxy: {}'.format('socks5'))
    logger.debug('Proxy initializing finished')
    logger.info('Start initialize Updater')
    mybot = Updater(crypto.decrypt(API_KEY), request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler("wordcount", wordcount, pass_user_data=True))
    dp.add_handler(CommandHandler("cat", send_cat, pass_user_data=True))
    dp.add_handler(CommandHandler("update", greet_update, pass_user_data=True))
    dp.add_handler(CommandHandler("commit", commit, pass_user_data=True))
    dp.add_handler(CommandHandler("emp", emp, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    # check_message()
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
# request_kwargs=PROXY,
