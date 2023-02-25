from random import randint

from faker import Faker

from db import session
from models import Teacher, Student, Group, Discipline, Grade

disciplines = [
    "Вища математика",
    "Фізика",
    "Програмування",
    "Історія України",
    "Англійська"
]

groups_st = ["group-1", "group-2", "group-3"]
NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50
fake = Faker("uk_UA")

def create_teachers():
    for _ in range(NUMBER_TEACHERS):
        teacher = Teacher(
            fullname = fake.name()
        )
        session.add(teacher)
    session.commit()   
    
def create_students():
    for _ in range(NUMBER_STUDENTS):
        student = Student(
            fullname = fake.name()
        )
        session.add(student)
    students = session.query(Student).all()  
    groups_st = session.query(Group).all() 
    group = iter(randint(1, len(groups_st)) for _ in range(len(students)))
    rel = Student(group_id = group.id)
    session.add(rel)
    session.commit()  
    
def create_disciplines():
    for _ in range(disciplines):
        discipline = Discipline(
            name = disciplines.get()
        )
        session.add(discipline)
        
    teachers = session.query(Teacher).all()
    disciplines = session.query(Discipline).all()
      
    teacher = iter(randint(1, teachers) for _ in range(len(disciplines)))
    session.add(teacher_id = teacher.id)
        
    session.commit()    
    
def create_groups():
    for _ in range(groups_st):
        group = Group(
            name = group.get()
        )
        session.add(group)
    session.commit()           
    
def create_grades():
    for _ in range(groups_st):
        group = Group(
            name = group.get()
        )
        session.add(group)
    session.commit()  

    
if __name__ == '__main__':
    create_teachers()
    create_students()
    create_disciplines()
    create_groups()