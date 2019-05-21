import getpass
import logging

logger = logging.getLogger('crypto_logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('bot_logger.log')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def encrypt(var, key):
    var_len = len(var)
    step = len(key)
    list_p = []
    code_list = []
    pos = 0
    while pos + step < var_len:
        list_p.append(var[pos:pos + step])
        pos += step
    else:
        list_p.append(var[pos:])
    print(list_p)
    for block in list_p:
        for a, b in zip(block, key):
            code_list.append(chr(ord(a) ^ ord(b)))
    return bytes(''.join(code_list), 'utf8')


def decrypt(var):
    logger.info('start decrypting')
    key = getpass.getpass('Type your passphrase: ')
    var_len = len(var)
    step = len(key)
    list_p = []
    code_list = []
    pos = 0
    while pos < var_len:
        list_p.append(var[pos:pos + step].decode('utf8'))
        pos += step
    else:
        list_p.append(var[pos:])
    for block in list_p:
        for a, b in zip(block, key):
            code_list.append(chr(ord(a) ^ ord(b)))
    logger.info('Decrypting finished')
    return ''.join(code_list)
