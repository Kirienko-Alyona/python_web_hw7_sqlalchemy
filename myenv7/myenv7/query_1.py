import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Найти 5 студентов с наибольшим средним баллом по всем предметам.

query = """
    SELECT s.fullname AS student, ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    GROUP BY s.fullname
    ORDER BY average_grade DESC
    LIMIT 5;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query)
        pprint.pprint(c.fetchall())
        c.close()