# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

db.define_table('userdetails',Field('email','string'),Field('pwd','password'))
is_date=IS_MATCH('^\d{4}$',error_message="Enter correct year")
is_roll=IS_MATCH('^\d{9}$',error_message="Enter 9 digit roll number Example: 201305578")
db.define_table('student_academicdetails',
                Field('rollno',length=512,requires=is_roll,label="Roll No"),
                Field('emailid',requires = IS_EMAIL(error_message='invalid email!'),label="Email Id",unique=True),
                Field('high_board','string',label="10th Board/University"),
                Field('high_marks',requires=IS_INT_IN_RANGE(0, 100,error_message='Enter in range 0-100!'),label="10th Marks"),
                Field('high_passout',length=512,requires=is_date,label="10th Passout Year"),
                Field('inter_board','string',label="12th Board/University"),
                Field('inter_marks',requires=IS_INT_IN_RANGE(0, 100,error_message='Enter in range 0-100!'),label="10+2 Marks"),
                Field('inter_passout',length=512,requires=is_date,label="12th Passout Year"),
                Field('ug_board','string',label="UG Board/University"),
                Field('ug_marks',requires=IS_INT_IN_RANGE(0, 10,error_message='Enter in range 0-10!')),
                Field('ug_passout',length=512,requires=is_date,label="UG Passout Year"),
                Field('pg_board','string',label="PG Board/University"),
                Field('pg_marks',#requires=IS_INT_IN_RANGE(0, 10,error_message='Enter in range 0-10!')
                      ),
                Field('pg_passout',length=512,#requires=is_date,label="PG Passout Year"
                      ),
                Field('high_marks_check','boolean',default='False',label="Check if you are PG Student"))
                #Field('inter_marks_check','boolean',default='True'),
                #Field('ug_marks_check','boolean',default='True'),
                #Field('pg_marks_check','boolean',default='True'))



is_phone=IS_MATCH('^\d{10}$',error_message="Enter 10 digit mobile number Example: 9999123456")
db.define_table('company_basicdetails',
                Field('companyname',requires=IS_NOT_EMPTY(),label="Company Name"),
                Field('contactpersonname',requires=IS_NOT_EMPTY(),label="Name"),
                Field('designation',requires=IS_NOT_EMPTY(),label="Designation"),
                Field('emailid',requires = IS_EMAIL(error_message='invalid email!'),label="Email Id",unique=True),
                Field('pwd','password', readable=False,label="Choose Password"),
                Field('website','text',label="Company Website"),
                Field('mobileno',length=512,requires=is_phone,label="Contact No"),
                Field('officeno','string',label='HR Office Number'),
                Field('address','text'),
                Field('about','text'))

db.define_table('tpo_basicdetails',
                Field('tponame','string',label="Name"),
                Field('emailid','string',label="Email id"),
                Field('pwd','password',label="Password"),
                Field('mobileno','string',label="Contact No"),
                Field('address','text',label="Address"))

db.define_table('courses',Field('coursename','string'),)

#db.define_table('eventdetails',Field('event_detail','string'),Field('marks','upload'))

db.define_table('jobdetails',
                Field('companyname','string',required=True#,'reference company_basicdetails',requires=IS_IN_DB(db, db.company_basicdetails.companyname, '%(companyname)s'),label='Company Name'
                      ),
                Field('jobprofile','text',label='Job Profile'),
                Field('companytype','string',label='Company Type'),
                Field('ctc','string',label='CTC'),
                Field('selectproc','text',label='Selection Procedure'),
                Field('dateofrec','date',label='Date of Recruitment'),
                Field('placeofjoin','string',label='Place of Joining'),
                Field('eligible','list:string','reference courses', widget=SQLFORM.widgets.checkboxes.widget,requires=IS_IN_DB(db, db.courses.coursename, '%(coursename)s',multiple=True),label='Eligible Courses'),
                Field('high_marks','integer',label='10th Marks'),
                Field('inter_marks','integer',label='10+2 Marks'),
                Field('ug_marks','integer',label='UG Marks'),
                Field('pg_marks','integer',label='PG Marks'),
                Field('deadline','date',label='Deadline Date')
                )
#db.dept.course_id.requires=IS_IN_DB(db, db.courses.id, '%(course_name)s')
is_phone=IS_MATCH('^\d{10}$',error_message="Enter 10 digit mobile number Example: 9999123456")
is_roll=IS_MATCH('^\d{9}$',error_message="Enter 9 digit roll number Example: 201305578")

db.define_table('student_basicdetails',
                Field('rollno',length=512,requires=is_roll,label="Roll No"),
                Field('firstname',requires=IS_NOT_EMPTY(),label="First Name"),
                Field('lastname',requires=IS_NOT_EMPTY(),label="Last Name"),
                Field('gender',requires = IS_IN_SET(['Male', 'Female', 'Others']),label="Gender"),
                Field('emailid',requires = IS_EMAIL(error_message='invalid email!'),label="Email Id",unique=True),
                Field('pwd', 'password',label="Choose Password"),
                Field('course','string',requires=IS_IN_DB(db, db.courses.coursename, '%(coursename)s'),label="Course"),
                Field('mobile',length=512,requires=is_phone,label="Contact No"),
                Field('peradd','text',label="Permanent Address"),
                Field('curradd','text',label="Current Address"),
                Field('ext_emailid',requires = IS_EMAIL(error_message='invalid email!'),label="Alternate Email Id"),
                Field('fathername',requires=IS_NOT_EMPTY(),label="Father's Name"),
                Field('birth_date','date'),label="DOB")
                #Field('appliedjob','list:string','reference jobdetails',
                   #   widget=SQLFORM.widgets.checkboxes.widget,requires=IS_IN_DB(db, db.jobdetails.id, '%(id)s',multiple=True),label='Applied Jobs'))

db.define_table('academics',
                Field('course_id','reference courses',requires=IS_IN_DB(db, db.courses.id, '%(course_name)s')),
                Field('board','string'),
                Field('college','string'),
                Field('marks','string'),
                Field('emailid','string','reference student_basicdetails',requires=IS_IN_DB(db, db.student_basicdetails.emailid, '%(emailid)s')))

db.define_table('student_job',
                Field('emailid','string',requires=IS_IN_DB(db,db.student_basicdetails.emailid,'%(emailid)s')),
               Field('jobid',requires=IS_IN_DB(db,db.jobdetails.id,'%(id)s'),widget=SQLFORM.widgets.checkboxes.widget),
               Field('status','boolean'),
               Field('program','string')
               )

db.define_table('event_details',Field('eventdetail','string'))
db.define_table('notice_details',Field('noticedetail','string'),Field('docs','upload'))
## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
