"""
Приложение КАФЕДРА для автоматизации работы отдела кадров ВУЗа. Таблица
Преподавательский состав должна содержать следующие данные: Табельный номер,
Фамилия И.О., Дата рождения, Должность, Ученая степень, Нагрузка, Зарплата
"""
import sqlite3 as sq

with sq.connect('kafedra.db') as c:
    con = c.cursor()
    con.execute("DROP TABLE IF EXISTS teachingStaff")
    con.execute("""CREATE TABLE IF NOT EXISTS teachingStaff (
                id_teacher INTEGER PRIMARY KEY AUTOINCREMENT,
                fullName VARCHAR,
                dateBirth DATE,
                job VARCHAR,
                academicDegree VARCHAR,
                load INTEGER,
                payment REAL
                )""")
    c.commit()
    con.close()

def addTeacher(number, fullname, dateBirth, job, academicDegree, load, payment): # Добавляем элементы со значениями ?
    con = c.cursor()
    con.execute('''
    INSERT INTO TeachingStaff (id_teacher, fullName, dateBirth, job, academicDegree, load, payment)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (number, fullname, dateBirth, job, academicDegree, load, payment))
    c.commit()

addTeacher(1, 'Иванов И.И.', '1980-01-01', 'Профессор', 'Доктор наук', 18, 60000)
addTeacher(2, 'Драгунов В.В.', '1979-17-07', 'Преподаватель', 'Магистр', 10, 49000)
addTeacher(3, 'Менделеев Д.И.', '1834-08-02', 'Профессор', 'Доктор наук', 22, 78000)
addTeacher(4, 'Шелбузов А.И.', '1974-21-08', 'Доцент', 'Бакалавр', 14, 52500)
addTeacher(5, 'Аванасов Ю.А.', '1945-15-04', 'Преподаватель', 'Магистр', 17, 58900)
addTeacher(6, 'Шестаков Д.И.', '1927-30-01', 'Преподаватель', 'Бакалавр', 20, 70000)
addTeacher(7, 'Гайдай В.Д.', '1987-08-02', 'Профессор', 'Доктор наук', 13, 51700)
addTeacher(8, 'Макаридзе Д.О.', '1977-12-09', 'Доцент', 'Бакалавр', 14, 52500)
addTeacher(9, 'Булыгин В.В.', '1999-01-01', 'Профессор', 'Доктор наук', 18, 60000)
addTeacher(10, 'Путин А.В.', '1941-02-02', 'Преподаватель', 'Магистр', 10, 49000)

def findByPosition(job):
    """Поиск по должности"""
    con = sq.connect("kafedra.db")
    c = con.cursor()
    c.execute('''SELECT * FROM teachingStaff WHERE job=?''', (job,))
    result = c.fetchall()
    con.close()
    return result

def findByDegree(academicDegree):
    """Поиск по ученой степени"""
    con = sq.connect("kafedra.db")
    c = con.cursor()
    c.execute('''SELECT * FROM teachingStaff WHERE academicDegree=?''', (academicDegree,))
    result = c.fetchall()
    con.close()
    return result

def findByPayment(payment):
    """Поиск по зарплате"""
    con = sq.connect("kafedra.db")
    c = con.cursor()
    c.execute('''SELECT * FROM teachingStaff WHERE payment=?''', (payment,))
    result = c.fetchall()
    con.close()
    return result

def deleteByNumber(teacher_id):
    """Удаление по номеру"""
    con = sq.connect("kafedra.db")
    c = con.cursor()
    c.execute('''DELETE FROM teachingStaff WHERE teacher_id=?''', (teacher_id, ))
    con.commit()
    con.close()

def getTeacher():
    con = sq.connect("kafedra.db")
    c = con.cursor()
    c.execute('SELECT * FROM TeachingStaff')
    return c.fetchall()

for teacher in getTeacher():
    print(teacher)

con.close()
