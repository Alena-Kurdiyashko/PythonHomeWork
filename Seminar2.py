# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0.56 -> 11

# num = float(input('Введите вещественное число: '))
# sum = 0
# for i in str(num):
#     if i != ".":
#         sum += int(i)
# print(f'Сумма цифр вещественного числа = {sum}')



#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите целое число N: '))
# mult = {}
# a = 1
# for i in range(1, n + 1):
#               a = a * i
#               mult[i]= a
# print('пусть N = ', n, 'тогда ', mult)

# 3 Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.

# *Пример:*

# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно)

# n = int(input('Введите число N: '))
# summa = 0

# for i in range(1, n + 1):
#     summa = summa + (1+1/i) ** i
# print(round(summa, 2))



# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

# n = int(input(f'Введите число для массива: '))
# a = int(input(f'Введите первое число: '))
# b = int(input(f'Введите второе число: '))

# lst = []

# for i in range(-n, n + 1):
#     lst.append(i)
# print(*lst)   

# print('Произведение на позициях', a, b, '=', lst[a] * lst[b])




# 5.Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

from random import randint

def mix(lst):
    for i in range (len(lst)):
        new_i = randint(0, len(lst) - 1)
        lst[i], lst[new_i] = lst[new_i], lst[i] 


lst = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4]
mix(lst) 
print(lst)       



