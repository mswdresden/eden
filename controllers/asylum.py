# -*- coding: utf-8 -*-

"""
    Asylum Controllers
"""

module = request.controller
resourcename = request.function

if not settings.has_module(module):
    raise HTTP(404, body="Module disabled: %s" % module)

# -------------------------------------------------------------------------
def index():
    #"Your ip is " + asylum.msw_ip_func()
    #"Your ip is " + current.asylum_ip_func()
    #"Your ip isaaa " + response.s3.asylum_ip_func()
    print "Your ip isaaa " + s3db.asylum_ip_func()
    return dict(bummi = str("Your ip isaaa " + s3db.asylum_ip_func()))

    return dict()
    """
        Application Home page
    """

    module_name = settings.modules[module].name_nice
    response.title = module_name
    return dict(module_name=module_name)

# -------------------------------------------------------------------------
def person():
    #return s3_rest_controller()
    #return current.rest_controller("pr", "person", **_attr)

    _attr = dict(csv_stylesheet = ("hrm", "person.xsl"),
        csv_template = "staff",
        #msw csv_extra_fields = [dict(label="Type",field=s3db.hrm_human_resource.type), ],
        # Better in the native person controller (but this isn't always accessible):
        #deduplicate = "",
        #msw orgname = orgname,
        replace_option = T("Remove existing data before import"),
        #rheader = hrm_rheader,
        )
    #return current.rest_controller("asylum", "person",**_attr)
    #return current.rest_controller("asylum", "person")
    return s3_rest_controller("asylum", "person")


# -------------------------------------------------------------------------
def msw():
    """
        Application Home page
    """

    print "Your ip is, i'll send it to the view ... " + s3db.asylum_ip_func()
    return dict(bummi = str("Your ip isaaa " + s3db.asylum_ip_func()))

    #module_name = settings.modules[module].name_nice
    #response.title = module_name
    #return dict(module_name=module_name)

# -----------------------------------------------------------
def display_form():
    form=FORM('Your Name:',
              INPUT(_name='name', requires=IS_NOT_EMPTY()),
              INPUT(_type='submit'))
    if form.accepts(request,session):
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill in the form correctly'
    return dict(form=form,name="Katharina Witt")

# ------------------------------------------------------------
db.define_table('numbers',
    Field('a', 'integer'),
    Field('b', 'integer'),
    Field('c', 'integer', readable=False, writable=False))
import time
def my_form_processing(form):
    c = form.vars.a * form.vars.b
    if c < 0:
       form.errors.b = 'a*b cannot be negative'

    else:
       form.vars.c = c

def insert_numbers():
   form = SQLFORM(db.numbers)
   if form.process(onvalidation=my_form_processing).accepted:
       session.flash = 'record inserted'
       redirect(URL())
   return dict(form=form)


