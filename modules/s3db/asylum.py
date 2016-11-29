# -*- coding: utf-8 -*-
"""
    This is just a commented template to copy/paste from when implementing
    new models. Be sure you replace this docstring by something more
    appropriate, e.g. a short module description and a license statement.

    The module prefix is the same as the filename (without the ".py"), in this
    case "asylum". Remember to always add an import statement for your module
    to:

    models/00_tables.py

    like:

    import eden.asylum

    (Yeah - not this one of course :P it's just an person)
"""

# mandatory __all__ statement:
#
# - all classes in the name list will be initialized with the
#   module prefix as only parameter. Subclasses of S3Model
#   support this automatically, and run the model() method
#   if the module is enabled in deployment_settings, otherwise
#   the default() method.
#
# - all other names in the name list will be added to response.s3
#   if their names start with the module prefix plus underscore
#
__all__ = ( "S3AsylumDataModel",
            "asylum_person_represent",
            "asylum_ip_func"
           )

# The following import statements are needed in almost every model
# (you may need more than this in your particular case). To
# import classes from s3, use from + relative path like below
#
from gluon import *
from gluon.storage import Storage
from ..s3 import *
from s3layouts import S3PopupLink

# =============================================================================
# Define a new class as subclass of S3Model
# => you can define multiple of these classes within the same module, each
#    of them will be initialized only when one of the declared names gets
#    requested from s3db
# => remember to list all model classes in __all__, otherwise they won't ever
#    be loaded.
#
class S3AsylumDataModel(S3Model):

    print 'msw: call to S3AsylumDataModel\n'
    
    # Declare all the names this model can auto-load, i.e. all tablenames
    # and all response.s3 names which are defined here. If you omit the "names"
    # variable, then this class will serve as a fallback model for this module
    # in case a requested name cannot be found in one of the other model classes
    #
    names = ("asylum_person",
             "asylum_person_id",
             )
    #msw: does not work, as s3db is made after this is called (see 00_
    #s3db = current.s3db

    # Define a function model() which takes no parameters (except self):
    def model(self):
        
        print 'msw: call to S3AsylumDataModel.model(self)\n'
        
        # You will most likely need (at least) these:
        db = current.db
        T = current.T
        gis = current.gis
        # this is the place for this call ih hrm, however, in skelleton it is further up
        s3db = current.s3db

        # from hrm
        s3 = current.response.s3
        auth = current.auth
        settings = current.deployment_settings

        ADMIN = current.session.s3.system_roles.ADMIN
        is_admin = auth.s3_has_role(ADMIN)
        print "asylum: my admin status is: ", is_admin

        messages = current.messages
        UNKNOWN_OPT = messages.UNKNOWN_OPT
        AUTOCOMPLETE_HELP = messages.AUTOCOMPLETE_HELP
        # hrm copy end

        print 'ADMIN=', ADMIN

        # This one may be useful:
        #settings = current.deployment_settings


        # Now define your table(s),
        # -> always use self.define_table instead of db.define_table, this
        #    makes sure the table won't be re-defined if it's already in db
        # -> use s3_meta_fields to include meta fields (not s3_meta_fields!),
        #    of course this needs the s3 assignment above

        # msw: tablename is a local variable
        tablename = "asylum_person"

        # msw: self is this class which is derived form S3Model eden/modules/s3/s3model.py
        #      S3Model has in it some Storage objects -> gluon/storage.py
        #      and defines variables like self.prefix /cache / context/ classes
        #      and self.model which is a storage of some storages Storage(config = Storage(),
        #      components= St..., methods, cmethods,  hierarchies
        #
        # msw: the next line calls define_table from this class. Same as db.define_table except that
        #      it does not repeat a table definition if the table is already defined.
        #      the web2py define_table function takes the following parameters (http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer):
        #      (the S3Model representation has other/additional parameters, hmmm??)
        # db.define_table('person',
        #            Field('name'),
        #            id=id,
        #            rname=None,
        #            redefine=True
        #            common_filter,
        #            fake_migrate,
        #            fields,
        #            format,
        #            migrate,
        #            on_define,
        #            plural,
        #            polymodel,
        #            primarykey,
        #            redefine,
        #            sequence_name,
        #            singular,
        #            table_class,
        #            trigger_name)

        self.define_table(tablename,
                # msw: a Field most probably is form dal (see gluon/tools.py -> from dal import DAL, Field)
                # it should have the following parameter ()
                # Field(fieldname, type='string',
                # length=None, # msw: for BWcompatibility in the future (web2py): should always be used
                # default=None,
                # required=False, requires='<default>',
                # ondelete='CASCADE', # msw: if True (or CASCADE??), deletes also all referencing data!
                # notnull=False, unique=False,
                # uploadfield=True, widget=None, label=None, comment=None,
                # writable=True, readable=True, update=None, authorize=None,
                # autodelete=False, represent=None, compute=None,
                # uploadfolder=None, uploadseparate=None, uploadfs=None, rname=None)


                Field("name", notnull=True, length=64,
                    label=T("Name"),
                    requires=IS_NOT_EMPTY(),
                    comment=T("The main Name of a person")
                ),
                Field("firstname", label=T("Firstname")),# A 'name' field
                Field("address",label=T("Address")),
                Field("telno",
                        label = T("Telephone Number")),
                Field("email", label=T("EMail")),

                          # person's birth date
                s3_date(label=T("Birth Date")),
                self.pr_gender(),

                # Current status
                Field("status", "integer",
                           default = 1,
                           label = T("Status"),
                           ),
                Field("native_country", label=T("Native Country")),
                Field("nationality", label=T("Nationality")),
                s3_date(label=T("Arrival in Germany")),
                s3_date(label=T("Arrival in Dresden")),
                Field("first_language", label=T("First Language")),
                Field("oter_languages", label=T("Other Languages")),
                s3_comments(),

                # This adds all the metadata to store
                # information on who created/updated
                # the record & when
                *s3_meta_fields())


        # Use self.configure to configure your model (or current.s3db.configure)
        # msw: Update the extra configuration of a table
        #    @param tablename: the name of the table
        #    @param attr: dict of attributes to update
        self.configure(tablename,
                       listadd=False)

        # The following shortcuts for S3 model functions are available (make
        # sure you do not overwrite them):
        #
        # self.define_table   => db.define_table (repeat-safe variant)
        # self.super_entity   => super_entity
        # self.super_key      => super_key
        # self.super_link     => super_link
        # self.add_components => s3db.add_components
        # self.configure      => s3db.configure
        # self.table          => s3db.table
        #

        # If you need to reference external tables, always use the table-method.
        # This will automatically load the respective model unless it is already
        # loaded at this point:
#msw?        xy_table = self.table("xy_table")
        # Alternatively, you can also use on of these:
#msw?        xy_table = self.xy_table
#msw?        xy_table = self["xy_table"]

        # The following two are equivalent:
#msw?        xy_variable = self.xy_variable
        # and:
#msw?        xy_variable = response.s3.xy_variable
        # However, if "xy_variable" is also a tablename, then the first
        # variant would return that table instead. Thus, make sure your
        # response.s3-global variables do not use tablenames as names

        # You can define ReusableFields,
        # -> make sure you prefix their names properly with the module prefix:
        asylum_person_id = S3ReusableField("asylum_person_id", "reference %s" % tablename,
                                               label = T("Asylum person"),
                                               requires = IS_EMPTY_OR(IS_ONE_OF(db,
                                                                      "asylum_person.id")))

        # Pass names back to global scope (s3.*)
        return dict(
            asylum_person_id=asylum_person_id,
        )

    # -------------------------------------------------------------------------
    @staticmethod
    def defaults():
        """
            Return safe defaults for model globals, this will be called instead
            of model() in case the model has been deactivated in
            deployment_settings.

            You don't need this function in case your model is mandatory anyway.
        """

        return dict(
            asylum_person_id = S3ReusableField("asylum_person_id",
                                                  "integer",
                                                  readable=False,
                                                  writable=False),
        )


    # ---------------------------------------------------------------------
    # Static so that calling it doesn't require loading the models
    @staticmethod
    def asylum_person_onvalidation(form):
        """ Form validation """

        db = current.db
        # Note that we don't need to use s3db here since this is a method of the class,
        # so the table must have loaded
        table = db.asylum_person
        query = (table.id == form.vars.id)
        record = db(query).select(table.name,
                                  limitby=(0, 1)).first()

        return

# =============================================================================
# Module-global functions will automatically be added to response.s3 if
# they use the module prefix and are listed in __all__
#
# Represents are good to put here as they can be put places without loading the
# models at that time
#
def asylum_person_represent(id):

    if not id:
        # Don't do a DB lookup if we have no id
        # Instead return a consistenct representation of a null value
        return current.messages["NONE"]

    # Your function may need to access tables. If a table isn't defined
    # at the point when this function gets called, then this:
    s3db = current.s3db
    table = s3db.asylum_table   # thislooks strange, is however how it's found in skelleton
    #table = s3db.asylum_person # msw: this looks better, but is it correct??

    # will load the table. This is the same function as self.table described in
    # the model class except that "self" is not available here, so you need to
    # use the class instance as reference instead

    db = current.db
    query = (table.id == id)
    record = db(query).select(table.name,
                              limitby=(0, 1)).first()
    try:
        # Try faster than If for the common case where it works
        return record.name
    except:
        # Data inconsistency error!
        return current.messages.UNKNOWN_OPT

# a truely msw function
#from gluon import *

def asylum_ip_func():
    print 'hi msw'
    return current.request.client

# END =========================================================================
