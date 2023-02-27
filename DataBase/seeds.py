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
    for team_ in TEAMS:
        team = Team(
            name = team_
    )
    session.add(team)
    session.commit() 

def create_teachers():
    for _ in range(1, NUMBER_TEACHERS + 1):
        teacher = Teacher(
            fullname = fake.name()
        )
        session.add(teacher)
    session.commit()   
    
def create_students():
    for _ in range(1, NUMBER_STUDENTS + 1):
        student = Student(
            fullname = fake.name()
        )
        session.add(student)
    teams_rel = session.query(Team).all() 
    students_rel = session.query(Student).all()  
    #session.rollback()
    
    for student in students_rel:
        team = random.choice(teams_rel)
        #for team in teams_rel:
        rel_ship = Student(team_id = team.id)
        session.add(rel_ship)
    session.commit()  
    
def create_disciplines():
    for discip in DISCIPLINES:
        discipline = Discipline(
            name = discip
        )
        session.add(discipline)
            
    teachers_rel = session.query(Teacher).all()
    disciplines_rel = session.query(Discipline).all()
    
    for teacher in teachers_rel:
        discipline = random.choice(disciplines_rel)
        rel_ship = Discipline(teacher_id = teacher.id)
        session.add(rel_ship)
        
    session.commit()    
            
    
def create_grades():
    for _ in range(1, 12):
        grade = Grade(
            grade = fake.num(),
            Date = fake.date_between(start_date="-1y") 
        )
            
        
        session.add(grade)
    session.commit()  

    
if __name__ == '__main__':
    create_teams()
    create_teachers()
    create_students()
    create_disciplines()
    create_grades()
    # student = Student(
    #     fullname = "James Cat"
    # )
    # session.add(student)
    # session.commit()