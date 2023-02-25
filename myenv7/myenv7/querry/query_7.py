import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Найти оценки студентов в отдельной группе по определенному предмету.

query= """
SELECT s.fullname AS student, d.name AS discipline, gr.grade AS grade
FROM grades gr
JOIN students s ON s.id = gr.student_id
JOIN disciplines d ON d.id = gr.discipline_id
JOIN groups_st g ON g.id = s.group_id
WHERE g.id = 2 AND d.id = 1
ORDER BY grade;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query)
        pprint.pprint(c.fetchall())
        c.close()