# - специальный символ для написания коментариев Все символы после него игнорируются

# type() - "показывает" тип объекта
my_int = 5
my_str = "123"
print(my_int, my_str)
print("my_int: ", my_int, "type: ", type(my_int))
print("my_str: ", my_str, "type: ", type(my_str))
print("----------------------------------------")
my_int = str(my_int)
my_str = int(my_str)
print("my_int: ", my_int, "type: ", type(my_int))
print("my_str: ", my_str, "type: ", type(my_str))
print(my_str // 12)

# Приведение типов
# int() - приводит к типу int
# str() - приводит к типу str
# float() - приводит к типу float
tmp = "12.99"
tmp = float(tmp)
print(tmp)
tmp = int(tmp)
print(tmp * 2)

# bool - логический тип. Принимает значения True/False
# and - логическое И
# or - логическое ИЛИ
# not - логическое отрицание

my_bool_1 = 2 > 1
my_bool_2 = 123 < 100
print(my_bool_1 or my_bool_2)

# Задача №1
# Написать программу которая считывает с клавиатуры число и выводит на экран сообщение: 
# «Это число четное» или «Это число нечетное»

my_value = input("Введи число:")
my_value = int(my_value)

if (my_value % 2) == 0:  # TODO another way
    print("Это число четное")
else:
    print("Это число нечетное")

# Задача №2
# Написать программу которая считывает с клавиатуры число и выводит на экран сообщение:
# «Это число положительное» или «Это число отрицательное»

my_value = input("Введи число:")
my_value = int(my_value)

if my_value > 0:
    print("Это число положительное")
if my_value < 0:
    print("Это число отрицательное")

# Задача №3
# Написать программу которая считывает с клавиатуры число и выводит на экран сообщение: 
# «Это число положительное» или 
# «Это число отрицательное» или
# «Это ноль»

my_value = input("Введи число:")
my_value = int(my_value)

if my_value > 0:
    print("Это число положительное")
elif my_value < 0:
    print("Это число отрицательное")
elif my_value == 0:
    print("Это ноль")
else:
    print("Что-то пошло не так! Проверь")

# Задача №4
# Написать программу которая считывает с клавиатуры число дней
# и выводит на экран день недели.Будем считать с понедельника.
# Если ввели 1, значит выводим «Понедельник» а если 0, значит выводим «Воскресенье».

my_value = input("Введи количество дней:")
my_value = int(my_value)

if my_value % 7 == 1:
    print("Понедельник")
elif my_value % 7 == 2:
    print("Вторник")
elif my_value % 7 == 3:
    print("Среда")
elif my_value % 7 == 4:
    print("Четверг")
elif my_value % 7 == 5:
    print("Пятница")
elif my_value % 7 == 6:
    print("Суббота")
else:
    print("Воскресенье")