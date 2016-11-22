def person():
    return s3_rest_controller()


def index():
    return dict()


def wurbel():
#    form = FORM(INPUT(_name='visitor_name', requires=IS_NOT_EMPTY()),
#                INPUT(_type='submit'))
#    if form.process().accepted:
#        session.visitor_name = form.vars.visitor_name
#        redirect(URL('bortsch'))
#    return dict(form=form)

    # msw: works
    response.title = "Msw changed Title in the controllerfunction wurbel() for class asylumseeker"

    # no effect
    response.menu = [('Google', False, 'http://www.google.com',[]),
                 ('Index',  True,  URL('index'), [])]

    # hmmm
    #globals.left_sidebar_enabled = 1
    #globals.right_sidebar_enabled = 1

    # works
    mswtext="Hallo, ich bin ein Text"
    menu = MENU([['One', False, 'link1'], ['Two', False, 'link2']])
    return dict(mswtext=mswtext,mswmenu=menu)

def bortsch():
    return dict()
