from db_connection import connection


create_table_groups = """
DROP TABLE IF EXISTS groups_st CASCADE;
"""

create_table_teachers = """
DROP TABLE IF EXISTS teachers CASCADE;
"""

create_table_students = """
DROP TABLE IF EXISTS students CASCADE;
"""

create_table_disciplines = """
DROP TABLE IF EXISTS disciplines CASCADE;
"""

create_table_grades = """
DROP TABLE IF EXISTS grades CASCADE;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(create_table_teachers)
        c.execute(create_table_groups)
        c.execute(create_table_students)
        c.execute(create_table_disciplines)
        c.execute(create_table_grades)
        c.close()
        