with open('referat.txt') as f:
    file = f.read()
print(len(file))  # 1509
print(len(file.split()))  # 163
file = file.replace('.', '!')
with open('referat2.txt', 'w') as f:
    f.write(file)
