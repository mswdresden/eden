# -*- coding: utf-8 -*-
"""
    This is just a commented template to copy/paste from when implementing
    new models. Be sure you replace this docstring by something more
    appropriate, e.g. a short module description and a license statement.

    The module prefix is the same as the filename (without the ".py"), in this
    case "housing". Remember to always add an import statement for your module
    to:

    models/00_tables.py

    like:

    import eden.housing

    (Yeah - not this one of course :P it's just an flat)
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
__all__ = ("S3HousingDataModel",
           "housing_flat_represent"
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
class S3HousingDataModel(S3Model):

    print 'msw: call to S3HousingDataModel\n'
    
    # Declare all the names this model can auto-load, i.e. all tablenames
    # and all response.s3 names which are defined here. If you omit the "names"
    # variable, then this class will serve as a fallback model for this module
    # in case a requested name cannot be found in one of the other model classes
    #
    names = ("housing_flat",
             "housing_flat_id",
             )
    #msw: does not work, as s3db is made after this is called (see 00_
    #s3db = current.s3db

    # Define a function model() which takes no parameters (except self):
    def model(self):
        
        print 'msw: call to S3HousingDataModel.model(self)\n'
        
        # You will most likely need (at least) these:
        db = current.db
        T = current.T

        # This one may be useful:
        settings = current.deployment_settings


        # Now define your table(s),
        # -> always use self.define_table instead of db.define_table, this
        #    makes sure the table won't be re-defined if it's already in db
        # -> use s3_meta_fields to include meta fields (not s3_meta_fields!),
        #    of course this needs the s3 assignment above
        tablename = "housing_flat"
        self.define_table(tablename,
                Field("name", label=T("Name"),requires = IS_NOT_EMPTY(),),# A 'name' field
                Field("address",label=T("Address")),
                Field("zip",label=T("Zip")),
                ##s3db.pr_person_id(label=T("Contact 1")),
                # Link to the Site resource
                self.super_link("site_id", "org_site",
                                label = T("Organisation"),
                                # superlink fields are normally invisible
                                readable = True,
                                writable = True,
                                # we want users to see the site name
                                # rather than just the ID
                                represent = self.org_site_represent,
                                ),
                #??? msw: how would the gis mechanism work (lat/lon) self.location_id(
                #    widget = S3LocationSelector(levels = [],
                #                                    show_address = True,
                #                                    show_postcode = True,
                #                                    show_latlon = True,
                #                                    show_map = True,
                #                                    ),
                #    ),
                self.super_link("pe_id", "pr_pentity"),
                Field("capacity","integer",label=T("Capacity")),
                Field("occupancy", "integer", label=T("Occupancy")),
                Field("telefoneno",label=T("Telefone Number")),
                Field("No1",label=T("No1")),
                Field("No2",label=T("No3")),
                Field("No3",label=T("No4")),

                # This adds all the metadata to store
                # information on who created/updated
                # the record & when
                *s3_meta_fields())


        # Use self.configure to configure your model (or current.s3db.configure)
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
#        xy_table = self.table("xy_table")
        # Alternatively, you can also use on of these:
#        xy_table = self.xy_table
#        xy_table = self["xy_table"]

        # The following two are equivalent:
#        xy_variable = self.xy_variable
        # and:
#        xy_variable = response.s3.xy_variable
        # However, if "xy_variable" is also a tablename, then the first
        # variant would return that table instead. Thus, make sure your
        # response.s3-global variables do not use tablenames as names

        # You can define ReusableFields,
        # -> make sure you prefix their names properly with the module prefix:
        housing_flat_id = S3ReusableField("housing_flat_id", "reference %s" % tablename,
                                               label = T("Housing flat"),
                                               requires = IS_EMPTY_OR(IS_ONE_OF(db,
                                                                      "housing_flat.id")))

        # Pass names back to global scope (s3.*)
        return dict(
            housing_flat_id=housing_flat_id,
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
            housing_flat_id = S3ReusableField("housing_flat_id",
                                                  "integer",
                                                  readable=False,
                                                  writable=False),
        )


    # ---------------------------------------------------------------------
    # Static so that calling it doesn't require loading the models
    @staticmethod
    def housing_flat_onvalidation(form):
        """ Form validation """

        db = current.db
        # Note that we don't need to use s3db here since this is a method of the class,
        # so the table must have loaded
        table = db.housing_flat
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
def housing_flat_represent(id):

    if not id:
        # Don't do a DB lookup if we have no id
        # Instead return a consistenct representation of a null value
        return current.messages["NONE"]

    # Your function may need to access tables. If a table isn't defined
    # at the point when this function gets called, then this:
    s3db = current.s3db
    table = s3db.housing_table # thislooks strange, is however how it's found in skelleton
    #table = s3db.housing_flat # msw: this looks better, but is it correct??

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

# END =========================================================================
