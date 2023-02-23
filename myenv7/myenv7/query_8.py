import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Найти средний балл, который ставит определенный преподаватель по своим предметам.

query= """
SELECT t.fullname AS teacher, d.name AS discipline, ROUND(AVG(gr.grade), 2) AS average_grade
FROM grades gr
JOIN disciplines d ON d.id = gr.discipline_id
JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 2
GROUP BY t.fullname, d.name
ORDER BY average_grade;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query)
        pprint.pprint(c.fetchall())
        c.close()