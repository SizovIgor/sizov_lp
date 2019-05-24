from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import logging
import config
import crypto
import ephem

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
def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

@log
def planet(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


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
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(CommandHandler("update", greet_update))
    dp.add_handler(CommandHandler("commit", commit))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__=="__main__":
    main()
# request_kwargs=PROXY,
