# 1 Вычислить число π c заданной точностью d
# *Пример:* 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi

# n = input("Введите число для заданной точности числа Пи:\n")
# print(f'число Пи с заданной точностью {n} равно {round(pi, len(n) - 2)}')


# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]

# num = int(input("Введите натуральное число: "))
# i = 2
# lst = []
# n = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {n} приведены в списке: {lst}")


# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]


# print('Введите длинну числовой последовательности')          
# x = int(input()) 
# s = []       
# print('Введите последовательность из', x, 'чисел')       
# for i in range(x):       
#     a = int(input()) 
#     s.append(a)          
# w = []       
# for y in range(len(s)):          
#     if s.count(s[y]) == 1:       
#         w.append(s[y])        
# print('Введенные числа:', s)         
# print('Неповторяющиеся числа:', w)




# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# import itertools


# k = int(input("Введите натуральную степень k: "))

# newlist = list([randint(1, 101) for i in range(k+1)])

# print(newlist)

# def polynomial(k, newlist): # с помощью гугла и горючих слёз получаем 
#     str1 = ['*x**']*(k-1) + ['*x']
#     pol = [[a, b, c] for a, b, c  in itertools.zip_longest(newlist, str1, range(k, 1, -1), fillvalue = '') if a !=0]
#     # объединяем несколько списков в список кортежей с самой длинной итерацией
#     # пустые кортежи заполняем пустотой ('')
#     print(pol)
#     for x in pol:
#         x.append(' + ') 
#     pol = list(itertools.chain(*pol)) 
#     print(pol)
#     pol[-1] = ' = 0' # меняем последний '+' на '= 0'
#     return "".join(map(str, pol)).replace(' 1*x',' x') # возвращаем строку

# list = polynomial(k, newlist)
# print(list)


# with open('file4_4.txt', 'w') as f:      
#     f.write(list)                   




# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.


import random

# запись в файл
def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0,101)

# создание коэфф.
def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst

# создание многочлена в виде строки 
def create_str(sp):
    lst= sp[::-1]
    ar = ''
    if len(lst) < 1:
        ar = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                ar += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    ar += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                ar += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    ar += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                ar += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                ar += ' = 0'
    return ar

# получение степени 
def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента 
def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получение его коэффициентов
def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    ii = l-1 # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst


with open('file5_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file5_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])
write_file("file_res.txt", create_str(lst_new))
with open("file_res.txt", 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")  # это было выстраданная задача из последних сил ;(









