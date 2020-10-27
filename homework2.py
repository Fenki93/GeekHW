# Dmitry Diachenko

#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
random_list = [1, "a", 12.8, True]
for i in random_list:
    print(type(i))

#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
random_list2 = [1,2,3,4,5,6,7,8,9]

if len(random_list2) % 2 == 0:
    i = 0
    while i < len(random_list2):
        el = my_list[i]
        random_list2[i] = random_list2[i+1]
        random_list2[i+1] = el
        i += 2
else:
    i = 0
    while i < len(random_list2) - 1:
        el = random_list2[i]
        random_list2[i] = random_list2[i + 1]
        random_list2[i + 1] = el
        i += 2
print(random_list2)

#3 Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
season_dict = {1: "winter",
               2: "spring",
               3: "summer",
               4: "autumn"}
season_list = list(season_dict.values())
print(season_list)
month = int(input("Enter the month number"))
if month ==1 or month == 12 or month == 2:
        print(season_dict.get(1))
        print(season_list[0])
elif month == 3 or month == 4 or month ==5:
    print(season_dict.get(2))
    print(season_list[1])
elif month == 6 or month == 7 or month == 8:
    print(season_dict.get(3))
    print(season_list[2])

elif month == 9 or month == 10 or month == 11:
    print(season_dict.get(4))
    print(season_list[3])
else:
        print("No such month")

#4 Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
my_str = input("Enter string: ")
word = my_str.split(' ')
for i, el in enumerate(word, 1):
    if len(el) > 10:
        el = el[:11]
    print(f"{i}. - {el}")

#5 Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
number = int(input("Enter number: "))
index = 0

for item in my_list:
    if new_number <= item:
        index = my_list.index(item) + 1
print(my_list)
