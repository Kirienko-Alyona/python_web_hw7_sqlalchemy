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

def create_teachers():
    for _ in range(1, NUMBER_TEACHERS + 1):
        teacher = Teacher(
            fullname = fake.name()
        )
        session.add(teacher)
    session.commit() 
    
def create_disciplines():
    teachers_rel = session.query(Teacher.id).all()
    print(teachers_rel)
    
    for discip in DISCIPLINES:
        discipline = Discipline(
            name = discip,
            teacher_id = (random.choice(teachers_rel))[0]
        )   
        session.add(discipline)
    session.commit()             
    
def create_grades():
    disciplines_rel = session.query(Discipline.id).all()
    for _ in range(1, NUMBER_STUDENTS + 1):
        grade = Grade(
            grade = random.choice(range(1, 12)),
            date_of = fake.date_between(start_date="-1y")
            #discipline_id = 
            #discipline_id = random.choice(range(len(session.query(Discipline.id).all()))),
            #student_id = random.choice(range(len(session.query(Student.id).all())))
        )
            
        
        session.add(grade)
    session.commit()  

    
if __name__ == '__main__':
    #create_teams()
    #create_students()
    create_teachers()
    create_disciplines()
    create_grades()
    # student = Student(
    #     fullname = "James Cat"
    # )
    # session.add(student)
    # session.commit()