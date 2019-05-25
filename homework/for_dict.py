# Задание 1
print("Задание 1", "*" * 30)
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = [x["first_name"] for x in students]
for student, count in {name: names.count(name) for name in names}.items():
    print("{}: {}".format(student, count))
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

# Задание 2
print("Задание 2", "*" * 30)
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = [x["first_name"] for x in students]
names_and_count = {name: names.count(name) for name in names}
max_count = max(names_and_count.values())

for name, count in names_and_count.items():
    if count == max_count:
        print(name)

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
]
print("Задание 3", "*" * 30)
for students in school_students:
    names = [x["first_name"] for x in students]
    names_and_count = {name: names.count(name) for name in names}
    max_count = max(names_and_count.values())

    for name, count in names_and_count.items():
        if count == max_count:
            print(name)

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
print("Задание 4", "*" * 30)
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {
        'class': '2a',
        'students': [
            {'first_name': 'Маша'},
            {'first_name': 'Оля'}
        ]
    },
    {
        'class': '3c',
        'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]
    },
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
for clas in school:
    boys_count = 0
    girl_count = 0
    for student in clas['students']:
        for name in student.values():
            if is_male[name]:
                boys_count += 1
            else:
                girl_count += 1
            # print(name, 'муж' if is_male[name] else "жен")

    print("В классе {} {} девочки и {} мальчика ".format(clas["class"],
                                                         girl_count,
                                                         boys_count))

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
print("Задание 5", "*" * 30)
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a',
     'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c',
     'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
clases = {}
for clas in school:
    clases[clas["class"]] = {"boys_count": 0, "girls_count": 0}
    boys_count = 0
    girl_count = 0
    for student in clas['students']:
        for name in student.values():
            if is_male[name]:
                clases[clas["class"]]["boys_count"] += 1
            else:
                clases[clas["class"]]["girls_count"] += 1
clas_with_max_girl = ''
max_boys = 0
max_girls = 0
clas_with_max_boy = ''
for clas in clases.keys():
    if max_boys < clases[clas]['boys_count']:
        max_boys = clases[clas]['boys_count']
        clas_with_max_boy = clas
    if max_girls < clases[clas]['girls_count']:
        max_girls = clases[clas]['girls_count']
        clas_with_max_girl = clas
print("Больше всего мальчиков в классе {}".format(clas_with_max_boy))
print("Больше всего девочек в классе {}".format(clas_with_max_girl))

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
