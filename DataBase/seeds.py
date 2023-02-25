from random import randint
import random

from faker import Faker

from db import session
from models import Student, Teacher, Team, Discipline, Grade

DISCIPLINES = [
    "Вища математика",
    "Фізика",
    "Програмування",
    "Історія України",
    "Англійська"
]

TEAMS = ["team-1", "team-2", "team-3"]
NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50
fake = Faker("uk_UA")

def create_teams():
    team = Team(
        name = random.choice(TEAMS)
    )
    session.add(team)
    session.commit() 

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
    classes = session.query(Team).all() 
    for student in students:
        team = random.choice(classes)
        team = iter(randint(1, len(TEAMS)) for _ in range(len(students)))
        rel_ship = Student(team_id = team.id, student_id = student.id)
        session.add(rel_ship)
    session.commit()  
    
def create_disciplines():
    discipline = Discipline(
        name = random.choice(DISCIPLINES)
    )
    session.add(discipline)
        
    teachers = session.query(Teacher).all()
    disciplines = session.query(Discipline).all()
      
    teacher = iter(randint(1, teachers) for _ in range(len(disciplines)))
    session.add(teacher_id = teacher.id)
        
    session.commit()    
    
          
    
# def create_grades():
#     grade = Grade(
#     
#     )
#     session.add(grade)
#     session.commit()  

    
if __name__ == '__main__':
    # create_teachers()
    # create_students()
    # create_disciplines()
    #create_teams()
    student = Student(
        fullname = "James Cat"
    )
    session.add(student)
    session.commit()