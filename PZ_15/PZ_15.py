"""
Приложение КАФЕДРА для автоматизации работы отдела кадров ВУЗа. Таблица
Преподавательский состав должна содержать следующие данные: Табельный номер,
Фамилия И.О., Дата рождения, Должность, Ученая степень, Нагрузка, Зарплата
"""

import sqlite3

conn = sqlite3.connect('kafedra.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS TeachingStaff (
    id_teacher INT PRIMARY KEY,
    fullName VARCHAR NOT NULL,
    dateBirth DATE NOT NULL,
    job VARCHAR NOT NULL,
    academicDegree VARCHAR,
    load REAL NOT NULL,
    payment REAL NOT NULL
)
''')

def addTeacher(number, fullname, dateBirth, job, academicDegree, load, payment):
    c.execute('''
    INSERT INTO TeachingStaff (id_teacher, fullName, dateBirth, job, academicDegree, load, payment)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (number, fullname, dateBirth, job, academicDegree, load, payment))
    conn.commit()

addTeacher(1, 'Иванов И.И.', '1980-01-01', 'Профессор', 'Доктор наук', 18, 60000)
addTeacher(2, 'Драгунов В.В.', '1979-17-07', 'Преподаватель', 'Магистр', 10, 49000)
addTeacher(3, 'Менделеев Д.И.', '1834-08-02', 'Профессор', 'Доктор наук', 22, 78000)


def dropTable():
    c.execute('DROP TABLE IF EXISTS TeachingStaff')
    conn.commit()

def getTeacher():
    c.execute('SELECT * FROM TeachingStaff')
    return c.fetchall()

for teacher in getTeacher():
    print(teacher)

conn.close()
