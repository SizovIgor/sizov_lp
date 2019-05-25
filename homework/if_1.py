def where_he_togo(years_old: int,
                  what_he_do: str = "Либо вы ввели неправильно, либо вы хитрый перец...") -> str:
    if 7 > years_old >= 3:
        what_he_do = "Вы ходите в садик"
    elif 17 >= years_old >= 7:
        what_he_do = "Вы учитесь в школе"
    elif 65 >= years_old > 17:
        what_he_do = "Вы работаете"
    elif 100 >= years_old > 65:
        what_he_do = "Пенсии нет, но вы держитесь!.."
    else:
        print("Ну как же так ?...")

    return what_he_do


if __name__ == "__main__":
    years_old = input('Введите ваш возраст: ')
    if not years_old.isdigit(): print("Вы ввели не верное значение")
    else:
        years_old = int(years_old)
        he_doing = where_he_togo(years_old)
        print(he_doing)
