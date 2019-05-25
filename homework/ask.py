speach = {
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Программирую"
}


def ask_user():
    while True:
        try:
            answer = input("Программа: Как дела?\nПользователь: ")
        except KeyboardInterrupt:
            print("Ладно, пока!")
            break
        if answer == speach["Как дела?"]:
            print("Ладно, пока!")
            break
        elif answer in speach.keys():
            print("Программа: {}".format(speach[answer]))


if __name__ == "__main__":
    ask_user()
