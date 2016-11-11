tablename = "training_course"
#db.define_table(tablename,
#                # A 'name' field
#                Field("name"),
#                # The start time
#                Field("start"),
#                # The facilitator
#                Field("facilitator"),
#                # This adds all the metadata to store
#                # information on who created/updated
#                # the record & when
#                *s3_meta_fields()
#                )
#
tablename = "training_course"
db.define_table(tablename,
                Field("name"),
                # A date type field (includes widget & validation)
                s3base.s3_date(),
                Field("facilitator"),
                # This is a file attachment that contains
                # a welcome pack that will be sent to each participant:
                Field("welcome_pack", "upload"),
                *s3_meta_fields()
                )
