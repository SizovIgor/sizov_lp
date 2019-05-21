import getpass


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
    return ''.join(code_list)

# var = "862054662:AAEgkDdlQ3lh6S-XMfJtpmyT_z-eFapbcJU"

# step = 5
# pos = 0
# var_len = len(var)
# while True:
#     if pos + step > var_len:
#         break
#     print(var[pos:pos + step])
#     pos += step

# passphrase = 'shok'
# code = encrypt(var, passphrase)
# print(decrypt(code, passphrase))
