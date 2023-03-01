from sqlalchemy import func, desc
#from sqlalchemy.orm import in_ #не импортируется

from termcolor import colored

from DataBase.models import Student, Teacher, Team, Discipline, Grade
from DataBase.db import session


# Найти 5 студентов с наибольшим средним баллом по всем предметам.
def select_1():
    results = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade"))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc("avg_grade")).limit(5).all()
    for result in results:    
        print(colored(result, "blue"))  
    print()      


#Найти студента с наивысшим средним баллом по определенному предмету.
def select_2():
    result = session.query(Discipline.name, Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade"))\
        .select_from(Grade).join(Student).join(Discipline).filter(Discipline.id == 3).group_by(Student.fullname, Discipline.name).order_by(desc("avg_grade")).first()
    print(colored(result, "blue"))
    print()
    
#Найти средний балл в группах по определенному предмету.
def select_3():
    results = session.query(Discipline.name, Team.name, func.round(func.avg(Grade.grade), 2).label("avg_grade"))\
        .select_from(Grade).join(Student).join(Discipline).join(Team).filter(Discipline.id == 5).group_by(Discipline.name, Team.name).order_by(desc("avg_grade")).all()
    for result in results:    
        print(colored(result, "blue"))
    print()

#Найти средний балл на потоке (по всей таблице оценок).
def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade"))\
        .select_from(Grade).order_by(desc("avg_grade")).scalar()
    print(colored(result, "blue"))
    print()

#Список курсов, которые читает определенный преподаватель.
def select_5():
    results = session.query(Teacher.fullname, Discipline.name)\
        .select_from(Discipline).join(Teacher).filter(Teacher.id == 2).order_by(desc(Discipline.name)).all()
    for result in results:    
        print(colored(result, "blue"))
    print()   

#Найти список студентов в определенной группе.
def select_6():
    results = session.query(Team.name, Student.fullname)\
        .select_from(Student).join(Team).filter(Team.id == 2).order_by(Student.fullname).all()
    for result in results:    
        print(colored(result, "blue"))
    print()

#Найти оценки студентов в отдельной группе по определенному предмету.
def select_7():
    results = session.query(Student.fullname, Discipline.name, Team.name, Grade.grade)\
        .select_from(Grade).join(Discipline).join(Student).join(Team).filter(Team.id == 2, Discipline.id == 1).order_by(Grade.grade).all()
    for result in results:    
        print(colored(result, "blue"))
    print()    

#Найти средний балл, который ставит определенный преподаватель по своим предметам.
def select_8():
    results = session.query(Teacher.fullname, Discipline.name, func.round(func.avg(Grade.grade), 2).label("avg_grade"))\
        .select_from(Grade).join(Discipline).join(Teacher).filter(Teacher.id == 5).group_by(Teacher.fullname, Discipline.name).order_by("avg_grade").all()
    for result in results:    
        print(colored(result, "blue"))
    print()    

#Найти список курсов, которые посещает определенный студент.
def select_9():
    results = session.query(Student.fullname, Discipline.name)\
        .select_from(Grade).join(Discipline).join(Student).filter(Student.id == 29).group_by(Discipline.name, Student.fullname).order_by(Discipline.name).all()
    for result in results:    
        print(colored(result, "blue"))
    print()

#Список курсов, которые определенному студенту читает определенный преподаватель.
def select_10():
    results = session.query(Teacher.fullname, Student.fullname, Discipline.name)\
        .select_from(Grade).join(Discipline).join(Student).join(Teacher).filter(Student.id == 12, Teacher.id == 5).group_by(Discipline.name, Student.fullname, Teacher.fullname).order_by(Discipline.name).all()
    for result in results:    
        print(colored(result, "blue"))
    print()        
        
#Средний балл, который определенный преподаватель ставит определенному студенту.
def select_11():
    result = session.query(Teacher.fullname, Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade"))\
        .select_from(Grade).join(Discipline).join(Student).join(Teacher).filter(Student.id == 12, Teacher.id == 5).group_by(Discipline.name, Student.fullname, Teacher.fullname).one()    
    print(colored(result, "blue"))
    print()        

#Оценки студентов в определенной группе на последнем занятии (по определенному предмету - который не указывается).
# def select_12():
#     results = session.query(Student.fullname, Discipline.name, Team.name, Grade.grade, Grade.date_of.label("date_last_lesson"))\
#         .select_from(Grade).join(Discipline).join(Student).join(Team).filter((Team.id == 2, Grade.date_of).in_((session.query(func.max(Grade.date_of)).select_from(Grade).first())))
#     for result in results:    
#         print(colored(result, "blue"))        
#         print()

if __name__ == '__main__':
    print(colored("1--> Найти 5 студентов с наибольшим средним баллом по всем предметам.", "magenta"))
    select_1()
    print(colored("2--> Найти студента с наивысшим средним баллом по определенному предмету.", "magenta"))
    select_2()
    print(colored("3--> Найти средний балл в группах по определенному предмету.", "magenta"))
    select_3()
    print(colored("4--> Найти средний балл на потоке (по всей таблице оценок).", "magenta"))
    select_4()
    print(colored("5--> Список курсов, которые читает определенный преподаватель.", "magenta"))
    select_5()
    print(colored("6--> Найти список студентов в определенной группе.", "magenta"))
    select_6()
    print(colored("7--> Найти оценки студентов в отдельной группе по определенному предмету.", "magenta"))
    select_7()
    print(colored("8--> Найти средний балл, который ставит определенный преподаватель по своим предметам.", "magenta"))
    select_8()
    print(colored("9--> Найти список курсов, которые посещает определенный студент.", "magenta"))
    select_9()
    print(colored("10--> Список курсов, которые определенному студенту читает определенный преподаватель.", "magenta"))
    select_10()
    print(colored("11--> Средний балл, который определенный преподаватель ставит определенному студенту.", "magenta"))
    select_11()
    #print(colored("12--> Оценки студентов в определенной группе на последнем занятии (по определенному предмету - который не указывается).", "magenta"))
    # select_12()
    # print()
