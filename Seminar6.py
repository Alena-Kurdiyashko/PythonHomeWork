# 1 предложить улучшения кода для четырёх уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# Начиная с 3 семинара.

# 1.1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# lst = [2, 3, 5, 9, 3, 2, 1, 2]
# i = 1
# sum = 0
# while i < len(lst):
#     sum = sum + lst[i]
#     i += 2
# print(sum)


# my_list = list(map(int, input('Введите числа, через пробел: ').split()))
# print(sum(my_list[1::2]))



# 1.2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint

# number = int(input('Введите размер списка '))
# lst_1 = []
# lst_2 = []

# for i in range(number):
#     lst_1.append(randint(0, 9))

# for i in range(len(lst_1)):
#     while i < len(lst_1)/2 and number > len(lst_1)/2:
#         number = number - 1
#         a = lst_1[i] * lst_1[number]
#         lst_2.append(a)
#         i += 1

# print(lst_1)
# print(lst_2)


# import math
# list_a = list(map(int, input('Введите числа, через пробел: ').split()))
# print('Исходный список: ',list_a)
# print('Результат: ',list([a * b for a, b in zip(list_a[0:math.ceil(len(list_a) / 2)],list_a[::-1])]))


# 1.3  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# from os import system
# system("cls")

# n = int(input("Введите число N: "))

# factorial = lambda x: 1 if x == 0 else x * factorial(x - 1) # Высчитываем факториал рекурсией

# lst = [factorial(i) for i in range(1, n+1)] # Добавляем в лист рекурсию от 1 до N
# print(f"\nПроизведение чисел от 1 до {n}: {lst}\n")


# 1.4 Напишите программу, которая на вход принимает вещественное число и показывает сумму его цифр 
# 
# n = input('Введите вещественное число: ')
# sum = sum(map(int, n.replace('.', '')))
# print(sum)

