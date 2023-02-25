import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Средний балл, который определенный преподаватель ставит определенному студенту.

query= """
SELECT s.fullname AS student, t.fullname AS teacher, ROUND(AVG(gr.grade), 2) AS average_grade
FROM grades gr
JOIN disciplines d ON d.id = gr.discipline_id
JOIN students s ON s.id = gr.student_id
JOIN teachers t ON t.id = d.teacher_id
WHERE s.id = 17 AND t.id = 2;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query)
        pprint.pprint(c.fetchall())
        c.close()