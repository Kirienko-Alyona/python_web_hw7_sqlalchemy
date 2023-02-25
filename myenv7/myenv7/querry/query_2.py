import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Найти студента с наивысшим средним баллом по определенному предмету.

query = """
SELECT d.name AS discipline, s.fullname AS student, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id
WHERE d.id = 3
GROUP BY s.fullname
ORDER BY average_grade DESC
LIMIT 1;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query)
        pprint.pprint(c.fetchall())
        c.close()