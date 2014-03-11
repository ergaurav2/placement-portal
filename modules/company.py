#!/usr/bin/env python
# coding: utf8
from gluon import *
class Company:
    companyname=""
    contactpersonname=""
    designation=""
    emailid=""
    officeno=""
    mobileno=""
    website=""
    pwd=""
    about=""
    address=""
    def createbasiccompany(self,obj):
        self.companyname=obj.companyname
        self.contactpersonname=obj.contactpersonname
        self.designation=obj.designation
        self.emailid=obj.emailid
        self.officeno=obj.officeno
        self.mobileno=obj.mobileno
        self.website=obj.website
        self.pwd=obj.pwd
        self.about=obj.about
        self.address=obj.address
        
    def createcompany(self,obj):
        self.companyname=obj.companyname
        self.contactpersonname=obj.contactpersonname
        self.designation=obj.designation
        self.emailid=obj.emailid
        self.officeno=obj.officeno
        self.mobileno=obj.mobileno
        self.website=obj.website
        self.about=obj.about
        self.address=obj.address
        
    def getcompanybasicdetails(self,emailid,db):
        obj=db(db.company_basicdetails.emailid==emailid).select().first()
        self.companyname=obj.companyname
        self.contactpersonname=obj.contactpersonname
        self.designation=obj.designation
        self.emailid=obj.emailid
        self.officeno=obj.officeno
        self.mobileno=obj.mobileno
        self.website=obj.website
        self.pwd=obj.pwd
        self.about=obj.about
        self.address=obj.address
        
    def insertcompany(self,db):
        db.company_basicdetails.insert(companyname=self.companyname,
                                       contactpersonname=self.contactpersonname,designation=self.designation,
                                          emailid=self.emailid,officeno=self.officeno,mobileno=self.mobileno,website=self.website,pwd=self.pwd,
                                          about=self.about,address=self.address)
    def updatecompany(self,emailid,db):
        obj=db(db.company_basicdetails.emailid==emailid).select().first()
        obj.update_record(companyname=self.companyname,
                                       contactpersonname=self.contactpersonname,designation=self.designation,
                            emailid=self.emailid,officeno=self.officeno,mobileno=self.mobileno,website=self.website,about=self.about,address=self.address)
