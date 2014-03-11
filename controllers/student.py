# coding: utf8
# try something like
from student import Student
from gluon.tools import Mail
from student import  Academicdetails
from datetime import date
def index(): return dict(message="hello from student.py")

# controller



def updateprofile():
    return dict()

def random1():
   form=SQLFORM(db.jobdetails)
   if form.process().accepted:
      response.flash = 'form accepted'
   elif form.errors:
      response.flash = 'form has errors'
   return dict(form=form)
   
def download():
    print request.args;
    return response.download(request,db)
def jq_check():
    return dict()

def layout_check():
   request.vars.lab="jindal is here"
   record = db.person(request.args(0))
   form = SQLFORM(db.person, record, deletable=True,
                  upload=URL('download'))
   if form.process().accepted:
       response.flash = 'form accepted'
   elif form.errors:
       response.flash = 'form has errors'
   return dict(form=form)

def download():
    return response.download(request, db)

def studentloginpage():
    return(redirect(URL('student/login')))


    


    







    
def random():
     
      #obj_student=Student()
     #obj_student.getstudentbasicdetails(session.emailid,db)
     grid = SQLFORM.smartgrid(db.student_basicdetails,
                             user_signature=False)
     return dict(grid=grid)
   

############################################################################################################     




###########################111111111111111111###########
###controller
def login():
    response.flash = T("Welcome to web2py!")
    return dict(message="")


###method
def validate_login():
    if request.vars.signin:
        row = db((db.student_basicdetails.emailid==request.vars.emailid) & (db.student_basicdetails.pwd==request.vars.pwd)).select().first()
        print request.vars.pwd
        print request.vars.emailid
        print row
        if row:    
            session.user='student'
            session.emailid=request.vars.emailid
            session.login=True
            redirect(URL('student','home'))
            return dict(message=request.vars.emailid)
        else :
            redirect(URL('student','login'))
            #redirect(URL('company','registration'))
            return dict(message="Who are you ?")
    else:
        return (redirect(URL('student','registration')))

            
#######################22222222222222222#############
###controller

def registration():
   form=SQLFORM(db.student_basicdetails,
                fields=['rollno','firstname','lastname','fathername','birth_date','gender','emailid','pwd','course','mobile'])
   if form.process().accepted:
       obj_academicdetails=Academicdetails()
       obj_academicdetails.insertacademicdetails(request.vars.emailid,request.vars.rollno,db)
       redirect(URL('student','login'))
   elif form.errors:
       response.flash = 'form has errors'
    #form = SQLFORM(db.student_basicdetails,
     #              fields=['rollno', 'firstname'])
   return dict(form=form)


###method##################                 use less
def new_registration():
    obj=Student()
    obj.createbasicstudent(request.vars)
    obj.insertstudent(db)
    obj_academicdetails=Academicdetails()
    obj_academicdetails.insertacademicdetails(request.vars.emailid,request.vars.rollno,db)
    return dict(redirect(URL('student','login')))


            
########3333333333333333333333333333333333

######method

def logout():
   #To logout
    del session.login
    del session.user
    del session.emailid
    redirect(URL('student','login'))
            
 
        
        
########444444444444444444444444444444444444

#####controller
def forgot_pass():
    return dict()


#####method
def forgot_password():
    mail = Mail() 
    mail.settings.server = 'smtp.gmail.com:587'
    mail.settings.sender = 'placementtpo@gmail.com'
    mail.settings.login = 'placementtpo@gmail.com:placementpg1'
    mailid=request.vars.emailid
    row=db(db.student_basicdetails.emailid==mailid).select().first()
    if row:
        msg=row.pwd
        mail.send(to=[str(mailid)], subject="Reset Password", message=str(msg))
        return(redirect(URL('default','home')))
    else:
        return(redirect(URL('default','home')))
    
    
    
#######################555555555555555555555555555555

######controller
def home():
    checkstudentvalidlogin()
    obj_student=Student()
    #obj_student.getstudentbasicdetails("jindal.manishkumar1@gmail.com",db)
    obj_student.getstudentbasicdetails(session.emailid,db)
    images1 = db().select(db.notice_details.ALL)
    images2 = db().select(db.event_details.ALL)
    return dict(images1=images1,images2=images2)


######################66666666666666666666666666666666666666

#######controller

def viewprofile():
    checkstudentvalidlogin()
    obj=db(db.student_basicdetails.emailid==session.emailid).select().first()
    db.student_basicdetails.id.readable=False;
    form1=SQLFORM(db.student_basicdetails,obj,readonly=True)
    
    obj=db(db.student_academicdetails.emailid==session.emailid).select().first()
    db.student_academicdetails.id.readable=False;
    db.student_academicdetails.rollno.readable=False;
    db.student_academicdetails.emailid.readable=False;
    db.student_academicdetails.high_marks_check.readable=False;
    form2=SQLFORM(db.student_academicdetails,obj,
                  readonly=True)
    #checkstudentvalidlogin()
    #obj_student=Student()
    #obj_academicdetails=Academicdetails()
    #obj_student.getstudentbasicdetails("jindal.manishkumar1@gmail.com",db)
    #obj_student.getstudentbasicdetails(session.emailid,db)
    #obj_academicdetails.getacademicdetails("jindal.manishkumar1@gmail.com",db)
    #obj_academicdetails.getacademicdetails(session.emailid,db)
    #return dict(studentdetails=obj_student,academicdetails=obj_academicdetails)
    return dict(form1=form1,form2=form2)
#########method



def profile():
    checkstudentvalidlogin()
    return(redirect(URL('student','updateprofile')))


################################7777777777777777777777777777777777777777777

######controller

def updateprofile():
    #checkstudentvalidlogin()
    #obj_student=Student()
    #obj_academicdetails=Academicdetails()
    #obj_student.getstudentbasicdetails("jindal.manishkumar1@gmail.com",db)
    #obj_student.getstudentbasicdetails(session.emailid,db)
    #obj_academicdetails.getacademicdetails("jindal.manishkumar1@gmail.com",db)
    #obj_academicdetails.getacademicdetails(session.emailid,db)
    #return dict(studentdetails=obj_student,academicdetails=obj_academicdetails)
    #db.student_basicdetails.id.readable=False;
    #db.student_basicdetails.pwd.writeable=False;
    #db.student_basicdetails.emailid.writable=False;
    #obj=db(db.student_basicdetails.emailid==session.emailid).select().first()
   
    #form=SQLFORM(db.student_basicdetails,obj)
   checkstudentvalidlogin()
   db.student_basicdetails.id.readable=False;
   obj1=db(db.student_basicdetails.emailid==session.emailid).select().first() 
   form1=SQLFORM(db.student_basicdetails,obj1,
                fields=['rollno','firstname','lastname','fathername','birth_date','gender','ext_emailid','course','mobile','birth_date','peradd','curradd'])
   
   obj2=db(db.student_academicdetails.emailid==session.emailid).select().first()
   db.student_academicdetails.id.readable=False;
   db.student_academicdetails.rollno.readable=False;
   db.student_academicdetails.emailid.readable=False;
   db.student_academicdetails.high_marks_check.readable=False;
    
    
   form2=SQLFORM(db.student_academicdetails,obj2,
               fields=['high_board','high_marks','high_passout','inter_board','inter_marks','inter_passout','ug_board','ug_marks','ug_passout','pg_board','pg_marks','pg_passout','high_marks_check'])
  
   if form1.process().accepted:
       print "form one accepted"
       response.flash = 'form accepted'
   elif form1.errors:
       print "form one errros"
       response.flash = 'form has errors'
    #form = SQLFORM(db.student_basicdetails,
     #              fields=['rollno', 'firstname'])
   if form2.process().accepted:
       print "form two accepted"
       response.flash = 'form accepted'
   elif form2.errors:
       print "form two errros"
       response.flash = 'form has errors'
    #form = SQLFORM(db.student_basicdetails,
     #              fields=['rollno', 'firstname'])
   return dict(form1=form1,form2=form2)    
 
######method


def saveprofile():
    checkstudentvalidlogin()
    obj_student=Student()
    obj_student.createstudent(request.vars)
    #obj_student.getstudentbasicdetails("jindal.manishkumar1@gmail.com",db)
    obj_student.updatestudent(session.emailid,db)
    obj_academicdetails=Academicdetails()
    obj_academicdetails.createacademicdetails(request.vars)
    obj_academicdetails.updateacademicdetails(session.emailid,db)
 
    return dict()




###############################88888888888888888888888888888888888888888888888

######controller(job applications)

def viewjobs():
   checkstudentvalidlogin()
   #session.emailid='ga@gmail.com'
   rows = db(db.student_job.emailid==session.emailid).select(join=db.jobdetails.on(db.student_job.jobid==db.jobdetails.id))
   print rows
   listjobid=[]
   listavailjob=[]
   for row in rows:
    listjobid.append(row.student_job.jobid)
    print "today date ",date.today()
    print "email id ", session.emailid
    if (not row.jobdetails.deadline) or row.jobdetails.deadline >= date.today():
        listavailjob.append(row.jobdetails.id)
    #listlinks.append(dict)
    print "avaialble jobs", listavailjob
    newrow=row
    print row
   visiblefields=[db.jobdetails.companyname,db.jobdetails.dateofrec,db.jobdetails.deadline,db.student_job.status]
   jobstatus={}
   rows=db(db.student_job.emailid==session.emailid).select()
   print "job status rows ", rows
   for row in rows:
        jobstatus[row.jobid]=row.status
        
   print "jobstatus ",jobstatus
   grid = SQLFORM.grid(
                       #db(
                           db.jobdetails.id.belongs(listjobid)
                          #db.student_job.emailid==session.emailid and db.jobdetails
                          #)
                       #.select(join=db.jobdetails.on(db.student_job.jobid==db.jobdetails.id)
                       #)
                       ,fields=visiblefields,
                       #left=db.jobdetails.on(db.jobdetails.id==db.student_job.jobid),
                       user_signature=False,
                            deletable=False,
                           editable=False,
                           create=False,links = [ #start of the list
    dict(    #start of the dict
         header='Job Application', #the header
          body = lambda row :  display1(jobstatus,listavailjob,row.id)#
          #lambda row : A('Apply',_href=URL('apply',vars=dict(z=row.id)))    #the body
         ) #end of the dict
] 
                         )
    #grid=rowsdent
    #print 'manage_job'
   # grid=SQLFORM.grid(db.jobdetails,
          #            user_signature=False,oncreate=createjob,links = [ #start of the list
   # dict(    #start of the dict
    #       header='Job Application', #the header
     #      body = lambda row : A('Apply',_href=URL('apply'))    #the body
      #     ) #end of the dict
#] )   
   return dict(grid=grid)




########################################99999999999999999999999999999999999

#########controller

def contact_tpo():
    checkstudentvalidlogin()
    return dict()
    
###########method
    
def sendmail():
    mail = Mail() 
    mail.settings.server = 'smtp.gmail.com:587' 
    mail.settings.sender = 'placementtpo@gmail.com'
    mail.settings.login = 'placementtpo@gmail.com:placementpg1' 
 #elect_id = request.args(0,cast=int) 
 #m=db(db.election.id==elect_id) 
 #for row in db(db.election.id==elect_id).select(): 
 #title=row.title 
 #m.update(electionflag=True) 
 #m.update(row.is_active=False) 
 #for row in db().select(db.voter.ALL): 
 # if row.election_id==title: 
    mail.send(to=['jindal.manishkumar1@gmail.com'], subject=request.vars.subject, message=request.vars.msg)
    return(redirect(URL('student','home')))
    



##################################10101010101010101010101010101010101010101

#####controller

def resetpassword():
    checkstudentvalidlogin()
    if request.vars.msg:
        response.flash=request.vars.msg
    return dict()    

######method

def changepassword():
    checkstudentvalidlogin()
    print 'emailid', session.emailid
    obj=db(db.student_basicdetails.emailid==session.emailid and db.student_basicdetails.pwd==request.vars.pwd).select().first()
    print obj
    if obj:
        obj.update_record(pwd=request.vars.newpwd)
        redirect(URL('student','home'))
    else:
        redirect(URL('student','resetpassword'))
   
    #obj_student.getstudentbasicdetails("jindal.manishkumar1@gmail.com",db)
    return dict()



##########################################################################################################################
def checkstudentvalidlogin():
    if not session.login or not session.user or not session.user=='student' :
        #student login page
        
        redirect(URL('login'))
        return dict(message="Enter valid loginid and password")

    
    
    
    
    
    
###################################################################################################################################


def  display1(jobstatus,listavailjob,jobid):
    print "current status ",jobid
    print jobstatus
    if jobstatus[str(jobid)]:
        print "Withdraw"
        if jobid in listavailjob:
            return A(str('Withdraw'),_href=URL('updatestatus',vars=dict(jobid=jobid,jobstatus=jobstatus)))
        else:
            return str('Applied Deadline Over')
    elif not jobstatus[str(jobid)]:
        print "Apply"
        if jobid in listavailjob:
            return A(str('Apply'),_href=URL('updatestatus',vars=dict(jobid=jobid,jobstatus=jobstatus)))
        else:
            return str('Not Applied Deadline Over')

        return A(str('Apply'),_href=URL('updatestatus',vars=dict(jobid=jobid,jobstatus=jobstatus)))
                 #URL('updatestatus',vars=dict(jobstatus=jobstatus,jobid=jobid)))
def updatestatus():
        print "Request ",request.vars.jobid
        #request.vars.jobstatus[request.vars.jobid]=not request.vars.jobstatus[request.vars.jobid]
        row=db(db.student_job.emailid==session.emailid and db.student_job.jobid==request.vars.jobid).select().first()
        print "row before ",row
        newstatus=not row.status
        print "newstatus ",newstatus
        row.update_record(status=newstatus)
        row=db(db.student_job.emailid==session.emailid and db.student_job.jobid==request.vars.jobid).select().first()
        print "row after ",row
        redirect(URL('student','viewjobs'))
        return (str(newstatus)) 
def Apply():
    row=db(db.student_job.jobid==request.vars.jobid and db.student_job.emailid==session.emailid).select().first()
    print "jobid ",request.vars.jobid," Apply",row
   # row.update_record(status=True)
    #redirect(URL('viewjobs'))
    print row
    return dict()
def Withdraw():
    obj=db(db.student_job.jobid==request.vars.jobid and db.student_job.emailid==session.emailid).select().first()
    row=db(db.student_job.jobid==request.vars.jobid and db.student_job.emailid==session.emailid).select().first()
    print "jobid ",request.vars.jobid," Withdraw ",row
    row.update_record(status=False)
    #redirect(URL('viewjobs'))
    print row
    return dict()
