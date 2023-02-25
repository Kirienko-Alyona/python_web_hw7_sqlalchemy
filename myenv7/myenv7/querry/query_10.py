import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Список курсов, которые определенному студенту читает определенный преподаватель.

query= """
SELECT t.fullname AS teacher, s.fullname AS student, d.name AS discipline
FROM grades gr
JOIN disciplines d ON d.id = gr.discipline_id
JOIN students s ON s.id = gr.student_id
JOIN teachers t ON t.id = d.teacher_id
WHERE s.id = 12 AND t.id = 2
GROUP BY discipline
ORDER BY discipline;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query)
        pprint.pprint(c.fetchall())
        c.close()