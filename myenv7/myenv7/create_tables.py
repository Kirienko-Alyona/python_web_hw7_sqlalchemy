from db_connection import connection

create_table_groups = """
CREATE TABLE IF NOT EXISTS groups_st (
  id SERIAL PRIMARY KEY NOT NULL,
  name VARCHAR UNIQUE
);
"""

create_table_teachers = """
CREATE TABLE IF NOT EXISTS teachers (
  id SERIAL PRIMARY KEY NOT NULL,
  fullname VARCHAR
);
"""

create_table_students = """
CREATE TABLE IF NOT EXISTS students (
  id SERIAL PRIMARY KEY NOT NULL,
  fullname VARCHAR,
  group_id SERIAL REFERENCES groups_st (id)
);
"""

create_table_disciplines = """
CREATE TABLE IF NOT EXISTS disciplines (
  id SERIAL PRIMARY KEY NOT NULL,
  name VARCHAR,
  teacher_id SERIAL REFERENCES teachers (id)
);
"""

create_table_grades = """
CREATE TABLE IF NOT EXISTS grades (
  id SERIAL PRIMARY KEY NOT NULL,
  discipline_id SERIAL REFERENCES disciplines (id),
  student_id SERIAL REFERENCES students (id),
  grade SERIAL,
  date_of DATE
);
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
        