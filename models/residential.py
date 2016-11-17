tablename = "residential_dorm"
db.define_table(tablename,
                # A 'name' field
                Field("name", label=T("Name")),
                # The start time
                Field("address",label=T("Address")),
                Field("zip",label=T("Zip")),
                s3db.pr_person_id(label=T("Contact 1")),
                s3db.pr_person_id(label=T("Contact 2")),
                # Link to the Site resource
                s3db.super_link("site_id", "org_site",
                                label = T("Venue"),
                                # superlink fields are normally invisible
                                readable = True,
                                writable = True,
                                # we want users to see the site name
                                # rather than just the ID
                                represent = s3db.org_site_represent,
                                ),
                Field("capacity",label=T("Capacity")),
                Field("telefoneno",label=T("Telefone Number")),
                # This adds all the metadata to store
                # information on who created/updated
                # the record & when
                *s3_meta_fields()
                )

s3.crud_strings[tablename] = Storage(
    label_create = T("Create Dormitory"),
    title_display = T("Dormitory Details"),
    title_list = T("Dormitories"),
    title_update = T("Edit Dormitory"),
    title_upload = T("Import Dormitory"),
    subtitle_list = T("Dormitory"),
    label_list_button = T("List  Dormitories"),
    label_delete_button = T("Delete Dormitory"),
    msg_record_created = T("Dormitory added"),
    msg_record_modified = T("Dormitory updated"),
    msg_record_deleted = T("Dormitory deleted"),
    msg_list_empty = T("No Dormitory currently registered"))

# msw
###from s3 import S3Represent
#
#represent = S3Represent(lookup = tablename)
#residential_id = S3ReusableField("residential_id", "reference %s" % tablename,
#                            label = T("Dormitory"),
#                            ondelete = "RESTRICT",
#                            represent = represent,
#                            requires = IS_ONE_OF(db,
#                                                 "residential_dorm.id",
#                                                 represent),
#                            ) 
#
#
#residential_dorm_opts = {
#    1: T("No Show"),
#    2: T("Cool place"),
#    3: T("Not nice")
#}
#
#tablename = "residential_inhabitant"
#db.define_table(tablename,
#                residential_id(),
#                s3db.asylumseeker_person_id(label=T("Inhabitant")),
#                Field("satisfied", "integer",
#                      label=T("Statisfied"),
#                      requires=IS_IN_SET(residential_dorm_opts),
#                      ),
#                *s3_meta_fields()
#                )
#
#s3db.add_components("residential_inhabitant",
#                    asylumseeker_person = "residential_id")



