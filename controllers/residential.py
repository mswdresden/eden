
#def dorm_rheader(r, tabs=[]):
#    if r.representation != "html":
#        # RHeader is a UI facility & so skip for other formats
#        return None
#    if r.record is None:
#        # List or Create form: rheader makes no sense here
#        return None
#
#    tabs = [(T("Basic Details"), None),
#            (T("Participants"), "participant")]
#    rheader_tabs = s3_rheader_tabs(r, tabs)
#
#    dorm = r.record
#
#    rheader = DIV(TABLE(
#        TR(
#            TH("%s: " % T("Name")),
#            dorm.name,
#            #TH("%s: " % T("Start Date")),
#            #dorm.start,
#            ),
#        TR(
#            TH("%s: " % T("Inhabitant")),
#            s3db.pr_person_represent(course.person_id),
#            )
#        ), rheader_tabs)
#
#    return rheader




def dorm():
    return s3_rest_controller()
    #return s3_rest_controller(rheader=dorm_rheader)

def index():
    return dict()