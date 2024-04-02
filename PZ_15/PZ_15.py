import sqlite3

conn = sqlite3.connect('kafedra.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS Преподавательский_состав (
    Табельный_номер INTEGER PRIMARY KEY,
    Фамилия_ИО TEXT NOT NULL,
    Дата_рождения DATE NOT NULL,
    Должность TEXT NOT NULL,
    Ученая_степень TEXT,
    Нагрузка REAL NOT NULL,
    Зарплата REAL NOT NULL
)
''')

def addTeacher(number, fullname, dateBirth, job, academicDegree, load, payment):
    c.execute('''
    INSERT INTO Преподавательский_состав (Табельный_номер, Фамилия_ИО, Дата_рождения, Должность, Ученая_степень, Нагрузка, Зарплата)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (number, fullname, dateBirth, job, academicDegree, load, payment))
    conn.commit()


addTeacher(1, 'Иванов И.И.', '1980-01-01', 'Профессор', 'Доктор наук', 18, 60000)

def getTeacher():
    c.execute('SELECT * FROM Преподавательский_состав')
    return c.fetchall()

for teacher in getTeacher():
    print(teacher)
conn.close()
