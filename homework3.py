import sys


# 1:
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль


def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "No ZeroDivision"
    except ValueError:
        return "enter only number"


print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))


# 2:
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def my_func(name, surname, byear, city, email, phone):
    print(name, surname, byear, city, email, phone)


my_func(name='Dmitry', surname='Dia', byear=1993, city='Kiev', email='no@email', phone='1159')


# 3 Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
#  аргументов.

def my_func(x, y, z):
    numbers = [x, y, z]
    total = []
    max_1 = max(numbers)
    total.append(max_1)
    numbers.remove(max_1)
    max_2 = max(numbers)
    total.append(max_2)
    print(sum(total))


my_func(-2, 4, 8)


# 4 Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
#  возведение числа x в степень y.


def my_func(x, y):
    if y == 0:
        return 1
    x * my_func(x, y - 1)


def my_func2(x, y):
    return 1 / x ** abs(y)


# 5
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

result = 0
while True:
    line = input("Enter number or Exit to exit: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'Exit':
                print(f"You sum is {result}. Program is terminated")
                exit(0)
            else:
                print(f"You sum is {result}. Input error", file=sys.stderr)
                exit(1)


# 6
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую
# его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_fync(x):
    return str(x).title()
