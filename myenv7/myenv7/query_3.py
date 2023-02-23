import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Найти средний балл в группах по определенному предмету.

query = """
SELECT d.name AS discipline, gr.name AS group, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN disciplines d ON d.id = g.discipline_id
JOIN groups_st gr ON gr.id = s.group_id
WHERE d.id = 5
GROUP BY gr.name, d.name
ORDER BY average_grade DESC;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query)
        pprint.pprint(c.fetchall())
        c.close()