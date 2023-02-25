from sqlalchemy import Column, Integer, String, ForeignKey, func, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(250), nullable=False)


class Group(Base):
    __tablename__ = "groups_st"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(150), nullable=False)
    

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, nullable=False)
    fullname = Column(String(250), nullable=False)
    
    group_id = Column("group_id", ForeignKey('groups_st.id', ondelete="CASCADE"))
    groups_st = relationship("Group", secondary="group_id", back_populates="students", passive_deletes=True)


class Discipline(Base):
    __tablename__ = "disciplines"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    
    teacher_id = Column("teacher_id", ForeignKey('teachers.id', ondelete="CASCADE"))
    teachers = relationship("Teacher", secondary="teacher_id", back_populates="disciplines", passive_deletes=True)
    
    
class Grade(Base):
    __tablename__ = "grades" 
    id = Column(Integer, primary_key=True, nullable=False)
   
    discipline_id = Column("discipline_id", ForeignKey('disciplines.id', ondelete="CASCADE"))
    discipline = relationship("Discipline", secondary="discipline_id", back_populates="grades", passive_deletes=True)
    student_id = Column("student_id", ForeignKey('students.id', ondelete="CASCADE"))
    students = relationship("Student", secondary="student_id", back_populates="grades", passive_deletes=True)
    date_of = Column(Date, default=func.now())
    