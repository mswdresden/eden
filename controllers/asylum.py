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
    """
        Application Home page
    """

    module_name = settings.modules[module].name_nice
    response.title = module_name
    return dict(module_name=module_name)



def person_rheader(r, tabs=[]):
    if r.representation != "html":
        # RHeader is a UI facility & so skip for other formats
        return None
    if r.record is None:
        # List or Create form: rheader makes no sense here
        return None

    tabs = [(T("Basic Details"), None),
            (T("Status"), "asylum_status")]
    rheader_tabs = s3_rheader_tabs(r, tabs)

    person = r.record

    rheader = DIV(TABLE(
        TR(
            TH("%s: " % T("Name")),
            person.name,
            TH("%s: " % T("First Name")),
            person.firstname,
            ),
        TR(
            TH("%s: " % T("Is this a status ...")),
            #person.name,
            #s3db.pr_person_represent(course.person_id),
            #s3db.asylum_person_represent(asylum_status.person_id),
            s3db.asylum_person_represent(0),
            #s3db.asylum_status.person_id,
            #val = s3db.asylum_ip_func,
            #"aaaaaa",
            #"bbbbbb",
            #print val
            #s3db.person_represent(person.person_id),
            )
        ), rheader_tabs)

    return rheader


# -------------------------------------------------------------------------
def person():
    print 'hallo msw (asylum person controller)'
    return s3_rest_controller(rheader=person_rheader)

# -------------------------------------------------------------------------
def status():
    return s3_rest_controller()

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


