from datetime import datetime, date, timedelta
from random import randint
from pprint import pprint

from psycopg2 import Error
from faker import Faker

from db import connection

disciplines = [
    "Вища математика",
    "Фізика",
    "Програмування",
    "Історія України",
    "Англійська"
]

groups_st = ["group-1", "group-2", "group-3"]
NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50
fake = Faker('uk-UA')

def seed_teachers():
    teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers(fullname) VALUES(%s);"
    c.executemany(sql, zip(teachers))

def seed_disciplines():
    sql = "INSERT INTO disciplines(name, teacher_id) VALUES(%s, %s);"
    c.executemany(sql, zip(disciplines, iter(randint(1, NUMBER_TEACHERS) for _ in range(len(disciplines)))))

def seed_groups():
    sql = "INSERT INTO groups_st(name) VALUES(%s);"
    c.executemany(sql, zip(groups_st,))

def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    sql = "INSERT INTO students(fullname, group_id) VALUES(%s, %s);"
    c.executemany(sql, zip(students, iter(randint(1, len(groups_st)) for _ in range(len(students)))))

def seed_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-15", "%Y-%m-%d")
    sql = "INSERT INTO grades(discipline_id, student_id, grade, date_of) VALUES(%s, %s, %s, %s);"

    def get_list_date(start: date, end: date) -> list[date]:
        result = []
        crent_date = start
        while crent_date <= end:
            if crent_date.isoweekday() < 6:
                result.append(crent_date)
            crent_date += timedelta(1)
        return result

    list_dates = get_list_date(start_date, end_date)

    grades = []
    for day in list_dates:
        random_discipline = randint(1, len(disciplines))
        random_students = [randint(1, NUMBER_STUDENTS) for _ in range(5)]
        for student in random_students:
            grades.append((random_discipline, student, randint(1, 12), day.date()))
    c.executemany(sql, grades)


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        try:
            seed_teachers()
            seed_disciplines()
            seed_groups()
            seed_students()
            seed_grades()
            conn.commit()
        except Error as error:
            pprint(error)
        finally:
            c.close()