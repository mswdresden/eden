
tablename = "asylumseeker_person"
db.define_table(tablename,
                # A 'first-name' field
                Field("firstname",label=T("First Name")),
                Field("lastname" ,label=T("Last Name")),
                Field("title" ,label=T("Title")),                
                # person's birth date
                s3base.s3_date(label=T("Birth Date")),
                
                # Where does the person live
                Field("Accomodation"),
                #s3db.warehouse_type_id(label=T("Accomodation"))
                s3db.pr_person_id(label=T("Personal Support")),
                
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
                # This adds all the metadata to store
                # information on who created/updated
                # the record & when
                *s3_meta_fields()
                )

s3.crud_strings[tablename] = Storage(
    label_create = T("Create AsylumSeeker"),
    title_display = T("Course Details"),
    title_list = T("Asylumseekers"),
    title_update = T("Edit Asylumseeker"),
    title_upload = T("Import  Asylumseeker"),
    subtitle_list = T("Asylumseeker"),
    label_list_button = T("List  Asylumseeker"),
    label_delete_button = T("Delete  Asylumseeker"),
    msg_record_created = T("Asylumseeker added"),
    msg_record_modified = T("Asylumseeker updated"),
    msg_record_deleted = T("Asylumseeker deleted"),
    msg_list_empty = T("No Asylumseeker currently registered"))


