<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

    <!-- **********************************************************************
         Human Resources - CSV Import Stylesheet
         Must be imported through the pr_person resource

         Column headers defined in this stylesheet:

         Organisation...................required.....organisation name
         Branch.........................optional.....branch organisation name
         ...SubBranch,SubSubBranch...etc (indefinite depth, must specify all from root)

         Type...........................optional.....HR type (staff|volunteer|member)
         Office.........................optional.....Facility name
         OrgGroup.......................optional.....OrgGroup name
         Facility Type..................optional.....Office, Facility, Hospital, Shelter, Warehouse
         Office Lat.....................optional.....office latitude
         Office Lon.....................optional.....office longitude
         Office Street address..........optional.....office street address
         Office Postcode................optional.....office postcode
         Department.....................optional.....human_resource.department
         Job Title......................optional.....human_resource.job_title
         Contract Term..................optional.....hrm_contract.term (short-term|long-term|permanent)
         Hours Model....................optional.....hrm_contract.hours (part-time|full-time)
         Staff Level....................optional.....salary.staff_level_id
         Salary Grade...................optional.....salary.salary_grade_id
         Monthly Salary.................optional.....salary.monthly_amount
         Salary Start Date..............optional.....salary.start_date
         Salary End Date................optional.....salary.end_date
         Status.........................optional.....human_resource.status
         Start Date.....................optional.....human_resource start date
         First Name.....................required.....person first name
         Middle Name....................optional.....person middle name
         Last Name......................optional.....person last name (required in some deployments)
         Initials.......................optional.....person initials
         DOB............................optional.....person date of birth
         Nationality....................optional.....person_details nationality
         Occupation.....................optional.....person_details occupation
         Company........................optional.....person_details company
         Affiliations............ ......optional.....person_details affiliation
         Marital Status.................optional.....person_details marital status
         Number of Children.............optional.....person_details number of children
         Place of Birth.................optional.....person_details place of birth
         Father Name....................optional.....person_details father name
         Mother Name....................optional.....person_details mother name
         Grandfather Name...............optional.....person_details grandfather name
         Grandmother Name...............optional.....person_details grandmother name
         Religion.......................optional.....person_details religion
         Criminal Record................optional.....person_details criminal record
         Military Service...............optional.....person_details military service
         Blood Type.....................optional.....pr_physical_description blood_type
         Ethnicity......................optional.....pr_physical_description ethnicity
         National ID....................optional.....person identity type = 2, value
         Passport No....................optional.....person identity type = 1, value
         Passport Country...............optional.....person identity
         Passport Expiry Date...........optional.....person identity
         Email..........................required.....person email address. Supports multiple comma-separated
         Mobile Phone...................optional.....person mobile phone number. Supports multiple comma-separated
         Home Phone.....................optional.....home phone number
         Office Phone...................optional.....office phone number
         Skype..........................optional.....person skype ID
         Twitter........................optional.....person Twitter handle
         Callsign.......................optional.....person Radio Callsign
         Emergency Contact Name.........optional.....pr_contact_emergency name
         Emergency Contact Relationship.optional.....pr_contact_emergency relationship
         Emergency Contact Phone........optional.....pr_contact_emergency phone
         Social Insurance Number........optional.....hrm_insurance.insurance_number
         Social Insurance Place.........optional.....hrm_insurance.insurer
         Health Insurance Number........optional.....hrm_insurance.insurance_number
         Health Care Provider...........optional.....hrm_insurance.provider
         Home Postcode..................optional.....person home address postcode
         Home Lat.......................optional.....person home address latitude
         Home Lon.......................optional.....person home address longitude
         Home Country...................optional.....person home address Country
         Home L1........................optional.....person home address L1
         Home L2........................optional.....person home address L2
         Home L3........................optional.....person home address L3
         Home L4........................optional.....person home address L4
         Permanent Address..............optional.....person permanent address
         Permanent Postcode.............optional.....person permanent address postcode
         Permanent Lat..................optional.....person permanent address latitude
         Permanent Lon..................optional.....person permanent address longitude
         Permanent Country..............optional.....person permanent address Country
         Permanent L1...................optional.....person permanent address L1
         Permanent L2...................optional.....person permanent address L2
         Permanent L3...................optional.....person permanent address L3
         Permanent L4...................optional.....person permanent address L4
         Skills.........................optional.....comma-separated list of Skills
         Teams..........................optional.....comma-separated list of Groups
         Trainings......................optional.....comma-separated list of Training Courses attended
         Training:XXXX..................optional.....Date of Training Course XXXX OR "True" to add Training Courses by column
                                                     Can be Date;Venue in field to specify the Venue of the Training Event
         External Trainings.............optional.....comma-separated list of External Training Courses attended
         Certificates...................optional.....comma-separated list of Certificates
         Certificate:XXXX...............optional.....Expiry Date of Certificate XXXX OR "True" to add Certificate by column
         Education Level................optional.....person education level of award (highest)
         Degree Name....................optional.....person education award
         Major..........................optional.....person education major
         Grade..........................optional.....person education grade
         Year...........................optional.....person education year
         Institute......................optional.....person education institute
         Award Type.....................optional.....hrm_award.award_type_id
         Award Date.....................optional.....hrm_award.date
         Awarding Body..................optional.....hrm_award.awarding_body
         Disciplinary Type..............optional.....hrm_disciplinary_action.disciplinary_type_id
         Disciplinary Date..............optional.....hrm_disciplinary_action.date
         Disciplinary Body..............optional.....hrm_disciplinary_action.disciplinary_body
         Active.........................optional.....volunteer_details.active
         Volunteer Type.................optional.....volunteer_details.volunteer_type
         Availability...................optional.....Availability dropdown
         Availability Comments..........optional.....Availability Comments
         Slot:XXXX......................optional.....Availability for Slot XXXX
         Comments.......................optional.....hrm_human_resource.comments

         Extensions for deploy module:
         Deployable.....................optional.....link to deployments module (organisation name|true)
         Deployable Roles...............optional.....credentials (job_titles for which person is deployable)
         Deployments....................optional.....comma-separated list of Missions for which the person was deployed

         Turkey-specific:
         Identity Card City
         Identity Card Town
         Identity Card District
         Identity Card Volume No
         Identity Card Family Order No
         Identity Card Order No

         PHRC-specific:
         Volunteer Cluster Type.........optional.....volunteer_cluster cluster_type name
         Volunteer Cluster..............optional.....volunteer_cluster cluster name
         Volunteer Cluster Position.....optional.....volunteer_cluster cluster_position name

         Column headers looked up in labels.xml:

         HomeAddress....................optional.....Home Street Address
         JobTitle.......................optional.....HR Job Title/Volunteer Role/Position
         HRMType........................optional.....
         MemberType.....................optional.....
         PersonGender...................optional.....person gender
         StaffID........................optional.....Staff ID/Volunteer ID

         @ToDo:
            - add more labels.xml lookups
            - fix location hierarchy:
                - use country name in location_onaccept to match L0?
            - make updateable (don't use temporary UIDs)

    *********************************************************************** -->
    <!--
	<xsl:import href="award.xsl"/>
    <xsl:import href="contract.xsl"/>
    <xsl:import href="disciplinary.xsl"/>
    <xsl:import href="insurance.xsl"/>
    <xsl:import href="salary.xsl"/>
    <xsl:import href="org_group_person.xsl"/>
	-->
    <xsl:output method="xml"/>
    <xsl:include href="../../xml/commons.xsl"/>
    <xsl:include href="../../xml/countries.xsl"/>

    <xsl:variable name="TeamPrefix" select="'Team:'"/>

    <!-- ****************************************************************** -->
    <!-- Lookup column names -->

    <xsl:variable name="HomeAddress">
        <xsl:call-template name="ResolveColumnHeader">
            <xsl:with-param name="colname">HomeAddress</xsl:with-param>
        </xsl:call-template>
    </xsl:variable>

    <xsl:variable name="HRMType">
        <xsl:call-template name="ResolveColumnHeader">
            <xsl:with-param name="colname">HRMType</xsl:with-param>
        </xsl:call-template>
    </xsl:variable>

    <xsl:variable name="JobTitle">
        <xsl:call-template name="ResolveColumnHeader">
            <xsl:with-param name="colname">JobTitle</xsl:with-param>
        </xsl:call-template>
    </xsl:variable>

    <xsl:variable name="MemberType">
        <xsl:call-template name="ResolveColumnHeader">
            <xsl:with-param name="colname">MemberType</xsl:with-param>
        </xsl:call-template>
    </xsl:variable>

   


    <!-- ******************************************************************
    <xsl:template name="Training">

        <xsl:param name="course"/>

        <xsl:if test="$course and $course!=''">
            <resource name="hrm_training">
                <reference field="course_id" resource="hrm_course">
                    <resource name="hrm_course">
                        <data field="name"><xsl:value-of select="$course"/></data>
                    </resource>
                </reference>
            </resource>
        </xsl:if>

    </xsl:template>
-->
    <!-- ******************************************************************
    <xsl:template name="Trainings">

        <xsl:param name="course_list"/>

        <xsl:if test="$course_list">
            <xsl:choose>
                <xsl:when test="contains($course_list, ',')">
                    <xsl:variable name="head" select="normalize-space(substring-before($course_list, ','))"/>
                    <xsl:variable name="tail" select="substring-after($course_list, ',')"/>
                    <xsl:call-template name="Training">
                        <xsl:with-param name="course" select="$head"/>
                    </xsl:call-template>
                    <xsl:call-template name="Trainings">
                        <xsl:with-param name="course_list" select="$tail"/>
                    </xsl:call-template>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:call-template name="Training">
                        <xsl:with-param name="course" select="$course_list"/>
                    </xsl:call-template>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:if>

    </xsl:template>
-->
    <!-- ****************************************************************** -->
    <!-- Pull this in from training_event.xsl if-required
    <xsl:template name="Course">

        <xsl:variable name="CourseName" select="normalize-space(substring-after(@name, ':'))"/>
        <resource name="hrm_course">
            <xsl:attribute name="tuid"><xsl:value-of select="$CourseName"/></xsl:attribute>
            <data field="name"><xsl:value-of select="$CourseName"/></data>
        </resource>

    </xsl:template> -->

    <!-- Pull this in from training_event.xsl if-required
    <xsl:template name="Trainings">

        <xsl:for-each select="col[starts-with(@name, 'Course')]">
            <xsl:variable name="CourseName" select="normalize-space(substring-after(@field, ':'))"/>
            <xsl:variable name="Dates" select="normalize-space(text())"/>
            <xsl:if test="$Dates!=''">
                <resource name="hrm_training">
                    <reference field="course_id" resource="hrm_course">
                        <xsl:attribute name="tuid">
                            <xsl:value-of select="$CourseName"/>
                        </xsl:attribute>
                    </reference>
                    <xsl:choose>
                        <xsl:when test="$Dates='Y' or $Dates='y'"/>
                        <xsl:when test="contains($Dates, '-')">
                            <xsl:variable name="StartDate" select="normalize-space(substring-before($Dates, '-'))"/>
                            <xsl:variable name="tail" select="normalize-space(substring-after($Dates, '-'))"/>
                            <xsl:variable name="EndDate">
                                <xsl:choose>
                                    <xsl:when test="contains(tail, '(')">
                                        <xsl:value-of select="normalize-space(substring-before($tail, '('))"/>
                                    </xsl:when>
                                    <xsl:otherwise>
                                        <xsl:value-of select="$tail"/>
                                    </xsl:otherwise>
                                </xsl:choose>
                            </xsl:variable>
                            <xsl:variable name="Place">
                                <xsl:choose>
                                    <xsl:when test="contains(tail, '(')">
                                        <xsl:value-of select="normalize-space(substring-before(substring-after($tail, '('), ')'))"/>
                                    </xsl:when>
                                    <xsl:otherwise>
                                        <xsl:value-of select="''"/>
                                    </xsl:otherwise>
                                </xsl:choose>
                            </xsl:variable>
                            <xsl:if test="$StartDate!=''">
                                <data field="start_date"><xsl:value-of select="$StartDate"/></data>
                                <xsl:if test="$EndDate!=''">
                                    <data field="end_date"><xsl:value-of select="$EndDate"/></data>
                                </xsl:if>
                            </xsl:if>
                            <xsl:if test="$Place!=''">
                                <data field="place"><xsl:value-of select="Place"/></data>
                            </xsl:if>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:variable name="Date" select="normalize-space(substring-before($Dates, '-'))"/>
                            <xsl:if test="$Date!=''">
                                <data field="start_date"><xsl:value-of select="$Date"/></data>
                                <data field="end_date"><xsl:value-of select="$Date"/></data>
                            </xsl:if>
                        </xsl:otherwise>
                    </xsl:choose>
                </resource>
            </xsl:if>
        </xsl:for-each>

    </xsl:template> -->

    <!-- ****************************************************************** -->
</xsl:stylesheet>
