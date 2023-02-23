import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Найти список студентов в определенной группе.

query= """
SELECT g.name AS group, s.fullname AS student
FROM students s
JOIN groups_st g ON g.id = s.group_id
WHERE g.id = 2
ORDER BY student;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query)
        pprint.pprint(c.fetchall())
        c.close()