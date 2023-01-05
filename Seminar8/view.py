import createDB

def option(db):
    print("\nВас приветствует программа мониторинга процессов обучения студентов!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть класс  и место которое занимает  студент \n \
    3: Полный список студентов \n \
    4: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        Fam = str(input("Введите фамилию ученика: "))
        print(createDB.poiskFam(db,Fam))
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option(db)
        exit()

    elif ch == 2:
        c = input('Введите ID студента для вывода по классам: ')
        print(createDB.poiskID(db,c))
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option(db)
        exit()

    elif ch == 3:
        print(createDB.ShowAllUsers(db))
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option(db)
        exit()

    else:
        print('еще раз')
    exit()


