import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Найти список курсов, которые посещает определенный студент.

query= """
SELECT s.fullname AS student, d.name AS discipline
FROM grades gr
JOIN disciplines d ON d.id = gr.discipline_id
JOIN students s ON s.id = gr.student_id
WHERE s.id = 22
GROUP BY d.name
ORDER BY discipline;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query)
        pprint.pprint(c.fetchall())
        c.close()