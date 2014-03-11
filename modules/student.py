#!/usr/bin/env python
# coding: utf8
from gluon import *
class Student:
    rollno=""
    firstname=""
    lastname=""
    birth_date=""
    gender=""
    emailid=""
    pwd=""
    course=""
    mobile=""
    peradd=""
    curradd=""
    ext_emailid=""
    fathername=""
    def createbasicstudent(self,obj):
        self.rollno=obj.rollno
        self.firstname=obj.firstname
        self.lastname=obj.lastname
      
        self.gender=obj.gender
        self.emailid=obj.emailid
        self.pwd=obj.pwd
        self.course=obj.course
        
        self.mobile=obj.mobile
        
    def createbasicstudent(self,obj):
        self.rollno=obj.rollno
        self.firstname=obj.firstname
        self.lastname=obj.lastname
        self.birth_date=obj.birth_date
        self.gendeyr=obj.gender
        self.emailid=obj.emailid
        self.pwd=obj.pwd
        self.course=obj.course
        
        self.mobile=obj.mobile
        self.peradd=obj.peradd
        self.curradd=obj.curradd
        
        self.ext_emailid=obj.ext_emailid
        self.fathername=obj.fathername

    def createstudent(self,obj):
        self.rollno=obj.rollno
        self.firstname=obj.firstname
        self.lastname=obj.lastname
        self.birth_date=obj.birth_date
        self.gender=obj.gender
        self.emailid=obj.emailid
        self.course=obj.course
        
        self.mobile=obj.mobile
        self.peradd=obj.peradd
        self.curradd=obj.curradd

        self.ext_emailid=obj.ext_emailid
        self.fathername=obj.fathername
        
    def getstudentbasicdetails(self,emailid,db):
        print "getstudentbasicdetails", emailid
        obj=db(db.student_basicdetails.emailid==emailid).select().first()
        print obj
        self.rollno=obj.rollno
        self.firstname=obj.firstname
        self.lastname=obj.lastname
        self.birth_date=obj.birth_date
        self.gender=obj.gender
        self.emailid=obj.emailid
        self.course=obj.course
        
        self.mobile=obj.mobile
        self.peradd=obj.peradd
        self.curradd=obj.curradd
        
        self.ext_emailid=obj.ext_emailid
        self.fathername=obj.fathername
        
    def insertstudent(self,db):
        db.student_basicdetails.insert(rollno=self.rollno,firstname=self.firstname,lastname=self.lastname,birth=self.birth,
    gender=self.gender,emailid=self.emailid,pwd=self.pwd,program=self.program,dept=self.dept,mobile=self.mobile)
        
    def updatestudent(self,emailid,db):
        obj=db(db.student_basicdetails.emailid==emailid).select().first()
        obj.update_record(rollno=self.rollno,firstname=self.firstname,
       lastname=self.lastname,birth=self.birth,gender=self.gender,emailid=self.emailid,
       program=self.program,dept=self.dept,mobile=self.mobile,
    peradd=self.peradd,curradd=self.curradd,passout=self.passout,marks=self.marks,ext_emailid=self.ext_emailid,fathername=self.fathername)

class Academicdetails:
    rollno=""
    emailid=""
    high_board=""
    high_marks=""
    high_passout=""
    inter_board=""
    inter_marks=""
    inter_passout=""
    ug_board=""
    ug_marks=""
    ug_passout=""
    pg_board=""
    pg_marks=""
    pg_passout=""
      
    def createacademicdetails(self,obj):
        self.rollno=obj.rollno
        self.emailid=obj.emailid
        self.high_board=obj.high_board
        self.high_marks=obj.high_marks
        self.high_passout=obj.high_passout
        self.inter_board=obj.inter_board
        self.inter_marks=obj.inter_marks
        self.inter_passout=obj.inter_passout
        self.ug_board=obj.ug_board
        self.ug_marks=obj.ug_marks
        self.ug_passout=obj.ug_passout
        self.pg_board=obj.pg_board
        self.pg_marks=obj.pg_marks
        self.pg_passout=obj.pg_passout
        
    def getacademicdetails(self,emailid,db):
        obj=db(db.student_academicdetails.emailid==emailid).select().first()
        print "getacademicdetails "
        print emailid
        print obj
        self.rollno=obj.rollno
        self.emailid=obj.emailid
        self.high_board=obj.high_board
        self.high_marks=obj.high_marks
        self.high_passout=obj.high_passout
        self.inter_board=obj.inter_board
        self.inter_marks=obj.inter_marks
        self.inter_passout=obj.inter_passout
        self.ug_board=obj.ug_board
        self.ug_marks=obj.ug_marks
        self.ug_passout=obj.ug_passout
        self.pg_board=obj.pg_board
        self.pg_marks=obj.pg_marks
        self.pg_passout=obj.pg_passout
        
    def insertacademicdetails(self,emailid,rollno,db):
        db.student_academicdetails.insert(rollno=rollno,emailid=emailid)
        
    def updateacademicdetails(self,emailid,db):
        row=db(db.student_academicdetails.emailid==emailid).select().first()
        row.update_record(high_board=self.high_board,high_marks=self.high_marks,high_passout=self.high_passout,
                                       inter_board=self.inter_board,inter_marks=self.inter_marks,
    inter_passout=self.inter_passout,ug_board=self.ug_board,ug_marks=self.ug_marks,ug_passout=self.ug_passout,
    pg_board=self.pg_board,pg_marks=self.pg_marks,pg_passout=self.pg_passout)
