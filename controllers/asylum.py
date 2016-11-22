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
    return current.rest_controller("asylum", "person",**_attr)


