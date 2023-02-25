from sqlalchemy import Column, Integer, String, ForeignKey, func, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    
    
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(250), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id", ondelete="CASCADE"))
    
    teams = relationship("Team", backref="students", passive_deletes=True)
    
    
class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(250), nullable=False)
    

class Discipline(Base):
    __tablename__ = "disciplines"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    teacher_id = Column("teacher_id", ForeignKey('teachers.id', ondelete="CASCADE"))
    
    teachers = relationship("Teacher", backref="disciplines", passive_deletes=True)
    
    
class Grade(Base):
    __tablename__ = "grades" 
    id = Column(Integer, primary_key=True)
    discipline_id = Column("discipline_id", ForeignKey('disciplines.id', ondelete="CASCADE"))
    student_id = Column("student_id", ForeignKey('students.id', ondelete="CASCADE"))
    date_of = Column(Date, default=func.now())
    discipline = relationship("Discipline", backref="grades", passive_deletes=True)
    students = relationship("Student", backref="grades", passive_deletes=True)
    
    