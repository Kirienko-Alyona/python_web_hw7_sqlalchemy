import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Найти какие курсы читает определенный преподаватель.

query= """
SELECT t.fullname AS teacher, d.name AS descipline
FROM disciplines d
JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 2
ORDER BY descipline DESC;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query)
        pprint.pprint(c.fetchall())
        c.close()