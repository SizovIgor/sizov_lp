def get_summ(num_one, num_two):
    try:
        num_one = int(num_one)
        num_two = int(num_two)
    except ValueError as e:
        print("Сработало исключение: {}".format(e))
    else:
        print("{} + {} ={}".format(num_one, num_two, num_one + num_two))


if __name__ == "__main__":
    get_summ(input('Первое число: '), input("Второе число: "))
