# 1.Напишите программу, удаляющую из файла все слова, содержащие "абв".

# with open ('fileabv.txt', 'r', encoding = 'utf-8') as f:
#     lst = list(map(str, f.readline().split()))

# print(lst)


# word = 'абв'
# result_txt = filter(lambda x: x.lower().find(word) == -1, lst)
# print(*result_txt)


# 2.Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

count = 2021
player = random.randint(1, 2)
print('Играем против бота!')

while count != 0:
    if player == 1:
        print('Ходит игрок')
        numbers = int(input('Сколько конфет вы заберете? '))
        while numbers < 1 or numbers > 28 or numbers > count:
            if count > 28:
                numbers = int(input('Можно взять не больше 28 конфет! Сколько конфет вы заберете? '))
            else:
                numbers = int(input(f'Можно взять не больше {count} конфет! Сколько конфет вы заберете? '))
        count -= numbers
        player = 0
        print(f'Осталось {count} конфет!\n')
    else:
        print('Ходит бот')
        if count < 29:
            numbers = count
        elif count < 57:
            numbers = count - 29
        else:
            numbers = random.randint(1, 28)
        print(f'Бот взял конфет в количестве {numbers}')
        count -= numbers
        player = 1
        print(f'Осталось {count} конфет!\n')

if player == 0:
    print('Победил игрок!')
else:
    print('Победил бот!')




# 3. Создайте программу для игры в "Крестики-нолики".

# Вариант интерфейса:

#  1  |  2 | 3
# --------------
#  4  |  5 | 6
# --------------
#  7  |  8 | 9


# board = list(range(1,10))

# def interface(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)

# def take_input(symbol):
#    valid = False
#    while not valid:
#       cell = input("В какую ячейку" + symbol + "? ")
#       try:
#          cell = int(cell)
#       except:
#          print("Некорректная ячейка. Вы ввели число?")
#          continue
#       if cell >= 1 and cell <= 9:
#          if(str(board[cell-1]) not in " XO"):
#             board[cell-1] = symbol
#             valid = True
#          else:
#             print("Клетка занята!")
#       else:
#         print("Некорректная ячейка. Введите число от 1 до 9.")

# def check(board):
#    position = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in position:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         interface(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check(board)
#            if tmp:
#               print(tmp, "Выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     interface(board)
# main(board)


# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
# 4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff

# def pressure(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def rebuild(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# s = input("Введите текст для сжатия: ")
# print(f"Текст после сжатия: {pressure(s)}")
# print(f"Текст после восстановления: {rebuild(pressure(s))}")