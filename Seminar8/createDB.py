def createUsers(con):
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        userid INT PRIMARY KEY,
        fname TEXT,
        lname TEXT,
        dt TEXT,
        uspevaem TEXT);
        """)
    users = [
        ('1', 'Иванов', 'Евгений', '02.07.1975',"Тройка"),
        ('2', 'Волкова', 'Зоя', '02.07.1980',"Четверка"),
        ('3', 'Сидоров', 'Евгений', '02.07.1975',"Отлично"),
        ('4', 'Чкалов', 'Саша', '02.07.1975',"Двойка"),
        ('5', 'Ромашова', 'Инна', '02.07.1975',"Единица"),
        ('6', 'Опушкин', 'Егор', '02.07.1975',"Тройка")
        ]    
    
    cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?);", users)
    con.commit

def createCabinet(con):
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS cabinet(
        cabinetid INT PRIMARY KEY,
        predmet TEXT,
        num_parta TEXT,
        ryad TEXT,
        vid_parta TEXT,
        userid INT);
        """)
    cabinets = [
        ('1', 'Русский язык', '1', 'Первый ряд',"Одноместная","1"),
        ('2', 'Математика', '2', 'Второй ряд',"Двуместная","2"),
        ('3', 'Рисование', '3', 'Первый ряд',"Одноместная","3"),
        ('4', 'Труд', '4', 'Четвертый ряд',"ОДвуместная","4"),
        ('5', 'Алгебра', '5', 'Шестой ряд',"Одноместная","5")
        ]    
    
    cur.executemany("INSERT INTO cabinet VALUES(?, ?, ?, ?, ?, ?);", cabinets)
    con.commit

def poiskFam(con,fam):
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users where fname like '{fam}%';")
    return cur.fetchall()

def poiskID(con,id):
    cur = con.cursor()
    cur.execute(f"SELECT * FROM cabinet where userid={id};")
    return cur.fetchall()

def ShowAllUsers(con):
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users")
    return cur.fetchall()


