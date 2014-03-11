# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
from student import Student
from gluon.tools import Mail
from student import  Academicdetails

def layout_check():
    form=SQLFORM(db.tpo_basicdetails)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    return dict(form=form)
    


def student():
    return dict()

def company():
    return dict()

def college():
    return dict()
def chking_footer():
    return dict()
def validate_student():
    row = db(db.student_basicdetails.emailid==request.vars.emailid).select().first()
     
    if row and row.pwd==request.vars.pwd:
        session.user='student'
        session.emailid=request.vars.emailid
        session.login=True
        redirect(URL('student','home'))
        return dict(message=request.vars.emailid)
    else :
        redirect(URL('default','home'))
        return dict()
    
def validate_company():
    redirect(URL('company','home'))
    return dict()

def validate_college():
    return(redirect(URL('college','home')))

def quicklinks():
    return dict()

def contactus():
    return dict()

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message="")



def addstudent_basicdetails():
    obj=Student()
    obj.createstudent(request.vars)
    obj.insertstudent(db)
    return dict()

def home():
   return dict()


def pk():
    return dict()
def student():
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

def student_viewprofile():
    obj=Student();
    return dict(studentdetails=obj)

def company():
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

def company_login():
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

def company_reg():
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

def college():
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

def college_login():
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

def student_reg():
     response.flash = T("Welcome to web2py!")
     return dict(message=T('Hello World'))

def register():
    form=SQLFORM.factory(Field('name',
                               requires=IS_NOT_EMPTY()),
                         Field('email',
                               requires=IS_NOT_EMPTY()),
                        Field('password',
                               requires=IS_NOT_EMPTY()),
                        Field('dob',
                               requires=IS_NOT_EMPTY()),
                        Field('contactno',
                               requires=IS_NOT_EMPTY()),
                        Field('rollno',
                               requires=IS_NOT_EMPTY()),
                        
                        )
    return dict(form=form)
def login():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    form = SQLFORM.factory(Field('name'),
                           Field('password'))
    if form.process().accepted:
        if db().select(db.student.name==form.vars.name):
            redirect(URL('student'))
        else:
            redirect(URL("fwdsfw"))
    return dict(form=form)


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
