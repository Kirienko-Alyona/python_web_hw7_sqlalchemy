import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Оценки студентов в определенной группе по определенному предмету на последнем занятии.

query = """
SELECT s.fullname AS student, g.name AS group_, d.name AS discipline, gr.grade AS grade, gr.date_of AS date_last_lesson
FROM grades gr
JOIN disciplines d ON d.id = gr.discipline_id
JOIN students s ON s.id = gr.student_id
JOIN groups_st g ON g.id = s.group_id
WHERE g.id = 3 AND gr.date_of IN (
    SELECT gr.date_of 
    FROM grades as gr
    JOIN students s ON s.id = gr.student_id
    JOIN groups_st g ON g.id = s.group_id
    WHERE g.id = 3 AND discipline_id = 2
    ORDER BY gr.date_of desc 
    LIMIT 1);
"""
#Оценки студентов в определенной группе на последнем занятии (по определенному предмету - который не указывается).
query_plus= """
SELECT s.fullname AS student, g.name AS group_, d.name AS discipline, gr.grade AS grade, gr.date_of AS date_last_lesson
FROM grades gr
JOIN disciplines d ON d.id = gr.discipline_id
JOIN students s ON s.id = gr.student_id
JOIN groups_st g ON g.id = s.group_id
WHERE g.id = 2 AND gr.date_of IN (
    SELECT MAX(gr.date_of)
    FROM grades gr
    )    
"""



if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query)
        pprint.pprint(c.fetchall())
        print()
        c.execute(query_plus)
        pprint.pprint(c.fetchall())
        c.close()