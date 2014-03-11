# coding: utf8
# try something like
from gluon.tools import Mail
def index(): return dict(message="hello from college.py")
#####controller

def resetpassword():
    checkcollegevalidlogin()
    if request.vars.msg:
        response.flash=request.vars.msg
    return dict()    

######method

def changepassword():
    checkcollegevalidlogin()
    print 'emailid', session.emailid
    obj=db(db.tpo_basicdetails.emailid==session.emailid and db.tpo_basicdetails.pwd==request.vars.pwd).select().first()
    print obj
    if obj:
        obj.update_record(pwd=request.vars.newpwd)
        redirect(URL('college','home'))
    else:
        redirect(URL('college','resetpassword'))
   
    #obj_student.getstudentbasicdetails("jindal.manishkumar1@gmail.com",db)
    return dict()


##############################################################################################################





def home():
    checkcollegevalidlogin()
    obj=db(db.tpo_basicdetails.emailid==session.emailid).select().first()
    db.tpo_basicdetails.id.readable=False;
    db.tpo_basicdetails.pwd.readable=False;
    form=SQLFORM(db.tpo_basicdetails,obj,readonly=True)
    return dict(form=form)

def updateprofile():
    checkcollegevalidlogin()
    db.tpo_basicdetails.id.readable=False;
    db.tpo_basicdetails.pwd.readable=False;
    db.tpo_basicdetails.emailid.writeable=False;
    obj=db(db.tpo_basicdetails.emailid==session.emailid).select().first() 
    form=SQLFORM(db.tpo_basicdetails,obj,
                 fields=['tponame','mobileno','address'])
    if form.process().accepted:
        redirect(URL('college','home'))
    elif form.errors:
        response.flash = 'form has errors'
    return dict(form=form)

def addevent():
    return dict()



    


    
#########################################################################################################

############111111111111111111111111111111##############################

#####controller

def login():
    return dict()

#####method

def validate_login():
    row = db(db.tpo_basicdetails.emailid==request.vars.emailid).select().first()
    if row and row.pwd==request.vars.pwd:
         session.user='college'
         session.emailid=request.vars.emailid
         session.login=True
         redirect(URL('college','home'))
         return dict(message=request.vars.emailid)
    else :
        redirect(URL('college','login'))
        return dict(message="Who are you ?")
    



###################################################################################################


###################333333333333333333333############################

##########method

def logout():
   #To logout
    del session.login
    del session.user
    del session.emailid
    redirect(URL('college','login'))
            
        
####################44444444444444444444############################

###########controller
def forgot_pass():
    return dict()


##########method
def forgot_password():
    mail = Mail() 
    mail.settings.server = 'smtp.gmail.com:587' 
    mail.settings.sender = 'placementtpo@gmail.com'
    mail.settings.login = 'placementtpo@gmail.com:placementpg1' 
    mailid=request.vars.emailid
    row=db(db.tpo_basicdetails.emailid==mailid).select().first()
    if row:
        msg=row.pwd
        mail.send(to=[str(mailid)], subject="Reset Password", message=str(msg))
        return(redirect(URL('default','home')))
    else:
        return(redirect(URL('default','home')))
        
#################555555555555555555555555555############################

########controller

def manage_events():
   checkcollegevalidlogin()
   grid = SQLFORM.smartgrid(db.event_details,
                             user_signature=False)
   return dict(grid=grid)


################66666666666666666666666666666#########################

###########controller

def manage_notices():
   checkcollegevalidlogin()
   grid = SQLFORM.smartgrid(db.notice_details,
                             user_signature=False)
   return dict(grid=grid)


######################77777777777777777777777######################

############controller

def viewstudentprofile():
     checkcollegevalidlogin()
     db.student_basicdetails.pwd.readable=False
     grid = SQLFORM.smartgrid(db.student_basicdetails,
                             user_signature=False)
     return dict(grid=grid)

    
    
###########################888888888888888888888888888################

######controller


def job():
   checkcollegevalidlogin()
   grid = SQLFORM.smartgrid(db.jobdetails,
                             user_signature=False,oncreate=updatestudent_job,onupdate=updatestudent_job)
   return dict(grid=grid)



############################999999999999999999999999999################

######controller


def jobapplicants():
   checkcollegevalidlogin()
   visiblefields=[db.jobdetails.companyname,db.jobdetails.dateofrec,db.jobdetails.deadline,db.jobdetails.id]
   grid = SQLFORM.smartgrid(db.jobdetails,
                             user_signature=False
                             ,fields=visiblefields,searchable=False,editable=False,deletable=False,links = [ #start of the list
    dict(    #start of the dict
         header='Eligible Students', #the header
          body = lambda row : A('View Eligible',_href=URL('vieweligiblestudents',vars=dict(jobid=row.id)))
         ), #end of the dict]
    dict(    #start of the dict
         header='Applied Students', #the header
          body = lambda row : A('View Applied',_href=URL('viewappliedstudents',vars=dict(jobid=row.id)))
         ), #end of the dict]
    ]
                             )
   return dict(grid=grid)

########methods

###m1

def vieweligiblestudents():
    checkcollegevalidlogin()
    rows = db(db.student_job.jobid==request.vars.jobid).select()
    listemailid=[]
    rows1=db(db.student_job.jobid==request.vars.jobid).select(db.student_job.emailid,db.student_job.status)
    jobstatus={}
    for row in rows1:
        if row.status:
            jobstatus[row.emailid]="Applied"
        else :
            jobstatus[row.emailid]="Not Applied"
    for row in rows:
        listemailid.append(row.emailid)
    db.student_basicdetails.pwd.readable=False
    visiblefields=[db.student_basicdetails.rollno,db.student_basicdetails.firstname,db.student_basicdetails.lastname,db.student_basicdetails.emailid,
                  db.student_basicdetails.course,db.student_basicdetails.mobile]
    grid=SQLFORM.grid(db.student_basicdetails.emailid.belongs(listemailid),fields=visiblefields,searchable=False,deletable=False,editable=False,
                      orderby=db.student_basicdetails.course,
                      links=[
                              dict(    #start of the dict
         header='Application Status', #the header
          body = lambda row : jobstatus[row.emailid]
          #lambda row : A('Apply',_href=URL('apply',vars=dict(z=row.id)))    #the body
         )]
     )
    return dict(grid=grid)


#####m2
def viewappliedstudents():
    checkcollegevalidlogin()
    rows = db((db.student_job.jobid==request.vars.jobid) & (db.student_job.status=='True')).select()
    listemailid=[]
    for row in rows:
            listemailid.append(row.emailid)
    db.student_basicdetails.pwd.readable=False
    visiblefields=[db.student_basicdetails.rollno,db.student_basicdetails.firstname,db.student_basicdetails.lastname,db.student_basicdetails.emailid,
                  db.student_basicdetails.course,db.student_basicdetails.mobile]
    grid=SQLFORM.grid(db.student_basicdetails.emailid.belongs(listemailid),fields=visiblefields,searchable=False,deletable=False,editable=False,
                      orderby=db.student_basicdetails.course,
     )
    return dict(grid=grid)
    
def updatestudent_job(form):
    rows=db(db.student_job.jobid == form.vars.id)
    print "jobid"
    rows.delete()
    high_marks=form.vars.high_marks
    inter_marks=form.vars.inter_marks
    ug_marks=form.vars.ug_marks
    pg_marks=form.vars.pg_marks
    eligible=form.vars.eligible
    rows =db(db.student_basicdetails.course.belongs(eligible)).select(
                                                  join=db.student_academicdetails.on(db.student_basicdetails.emailid==db.student_academicdetails.emailid))
    for row in rows:
        if (not high_marks or row.student_academicdetails.high_marks>=high_marks):
            if (not inter_marks or row.student_academicdetails.inter_marks>=inter_marks) :
                if (not ug_marks or row.student_academicdetails.ug_marks>=ug_marks):
                    if (not pg_marks or not row.student_academicdetails.high_marks_check or row.student_academicdetails.pg_marks>=pg_marks):
                       db.student_job.insert(emailid=row.student_academicdetails.emailid,jobid=form.vars.id,status=False)
    return dict()

def apply():
   checkcollegevalidlogin()
   redirect(URL('manage_job'))
   return dict()

def viewstudentprofile():
     checkcollegevalidlogin()
     db.student_basicdetails.pwd.readable=False
     grid = SQLFORM.grid(db.student_basicdetails,
                             user_signature=False)
     return dict(grid=grid)

def checkcollegevalidlogin():
    if not session.login or not session.user or not session.user=='college' :
        #student login page
        
        redirect(URL('login'))
        return dict(message="Enter valid login id and password")
