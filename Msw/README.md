

##########################################
# installation of web2py and sahana-eden # 
##########################################

# following istructions found in:
# wget https://raw.githubusercontent.com/nursix/sahana-setup/master/prod/debian/cherokee-postgis-install.sh

# update your system an get all needed python stuff
# Update system
sudo apt-get update
sudo apt-get upgrade
sudo apt-get clean

# Install Admin Tools
# fails due to missing elinks-lite: sudo apt-get install -y unzip psmisc mlocate telnet lrzsz vim elinks-lite rcconf htop sudo p7zip dos2unix curl
sudo apt-get install unzip psmisc mlocate telnet lrzsz vim  rcconf htop sudo p7zip dos2unix curl

# Install Git
sudo apt-get install git-core
sudo apt-get clean

# Email
sudo apt-get install exim4-config exim4-daemon-light
sudo apt-get clean

# Python
sudo apt-get install libgeos-c1
sudo apt-get install libgeos-dev
sudo apt-get install python-dev
sudo apt-get install python-lxml python-setuptools python-dateutil python-pip
sudo apt-get install python-serial
sudo apt-get install python-imaging
sudo apt-get install python-matplotlib
sudo apt-get install python-requests
sudo apt-get install python-xlwt
sudo apt-get install build-essential
sudo apt-get clean


# from an installation on a different laptop (64-debian)
# for web2py (does not work do to two missing sources): apt-get install -y unzip psmisc mlocate telnet lrzsz vim elinks-lite rcconf htop sudo p7zip dos2unix curl
=> sudo apt-get install -y unzip psmisc mlocate telnet lrzsz vim  htop sudo p7zip dos2unix cur
sudo apt-get install libgeos-c1v5
sudo apt-get install python-lxml python-setuptools python-dateutil python-pip
sudo apt-get install libgeos-dev
sudo apt-get install python-dev
sudo apt-get install python-lxml python-setuptools python-dateutil python-pip
sudo apt-get install python-serial
sudo apt-get install python-imaging
sudo apt-get install python-matplotlib
sudo apt-get install python-requests
sudo apt-get install python-xlwt
sudo apt-get install build-essential
sudo apt-get install libodbc1
sudo apt-get install python-openid
from: http://eden.sahanafoundation.org/wiki/InstallationGuidelines/Linux/Developer/Manual#InstallPythonLibraries
sudo apt-get install python-lxml
sudo apt-get install python-shapely
sudo apt-get install python-reportlab
sudo apt-get install python-imaging
sudo apt-get install python-imaging
sudo apt-get install python-dateutil
sudo apt-get install python-xlwt
sudo apt-get install python-xlrd
sudo apt-get install python-numpy
sudo apt-get install python-matplotlib
sudo apt-get install python-setuptools
sudo apt-get install python-serial
sudo apt-get install python-tz
sudo apt-get install python-mysqldb
  	
# Web2Py
sudo apt-get install libodbc1

# for some reason insalled also (msw):
sudo apt-get install python-openid

# get web2py and reset it to last stable version, which is compatible with sahana-eden
git clone --recursive git://github.com/web2py/web2py.git
cd web2py/
git reset --hard cda35fd
git submodule update
(in an older manual it read: git submodule update --init --recursive )

# get sahana-eden
cd applications
git clone git://github.com/mswdresden/eden

# run web2py (setting admin password to "pass")
python web2py.py -a pass

go to URL: http://127.0.0.1:8000/
	- you can here login to web2py interface with the password ("pass") set earlier.
	  then you can go to the admin area, check 'eden' and edit things
	  
	  however, before everything runs, you have to edit web2py/applications/eden/models/000_config.py
	  ACTION REQUIRED: The following files were copied from templates and should be edited: models/000_config.py 
	  therefore: edit line (17) to read: FINISHED_EDITING_CONFIG_FILE = True
	  
	  now editing works from within the web2py interface.
	  now also works calling eden from your browser: http://127.0.0.1:8000/eden
	  
	  'register for an account' for the first time:
	  ATTENTION: the first user registered will be the administrator
		 - give some email (any random mail works, I use a real one, however)
		 - give a admin password (as long as you work only locally, do not bother too much with complex passwords)
		 - after 'OK' you should be logged in, ... log out and test if login works
	
	It most probably is usefull to edit also settings.base.debug to match
	settings.base.debug = True
	in 000_config.py

Passwords for development:
web2py: pass
eden:   msw@3dd2.de 1234	
	 

#######
# Git #
#######

https://github.com/mswdresden/eden # repository

# push and pull
git push https://github.com/mswdresden/eden.git
git pull [seems to work w/o https://github.com/mswdresden/eden.git]

# updating from original master? 
#http://www.flossmanuals.net/sahana-eden/installing-a-developer-environment/
#
# once do: git remote add upstream git://github.com/flavour/eden.git
git pull upstream master # this should do the job?!


#########
# links #
#########

# Sahana Eden

https://sahanafoundation.org/        # sahana foundation main page
http://eden.sahanafoundation.org/    # eden at sahana foundation (and wiki)
https://github.com/sahana/eden       # sahana eden on github
http://flossmanuals.net/sahana-eden/ # sahana book!
http://booki.flossmanuals.net/sahana-eden/

# sahana-eden google groups mailing list
https://groups.google.com/forum/#!forum/sahana-eden

# the sahana eden wiki
http://eden.sahanafoundation.org/

# demo on the net:
http://demo.eden.sahanafoundation.org/eden/

# insalling local sahana instance on suse
https://github.com/nursix/sahana-setup/wiki/Developer-Setup#opensuse

# sahana components explained
https://github.com/nursix/sahana-setup/wiki/Components

# first long sahana tutorial
# https://www.youtube.com/watch?v=UhvlxZFnUM8

# gis (maps?) is something very cool and a little different
http://eden.sahanafoundation.org/wiki/GIS

# s3 documentation
http://pub.nursix.org/eden/s3/
http://eden.sahanafoundation.org/wiki/S3/S3Model/SuperEntities

# web-course (7 parts) on web2py
https://www.youtube.com/watch?v=bW9lpN95zwQ&index=5&list=PL5E2E223FE3777851



########
# TODO #
########
- create and improve a model
- figure out how languages work (browser settings or setting within eden or setting within web2py?)
	- github anmelden (account wiederfinden)
	- sahana eden in git und workflow testen
	- erste eigene entwicklungen (z.B. spreadsheet beispiel von web2py)
- neue module machen	
- module syntax lernen
- styles und links und menues lernen

######################################################
# msw's howto:                                       #
######################################################
// ---------------------------
*0. Web2py version*

	from: http://write.flossmanuals.net/sahana-eden/maintenance/

	Since Sahana Eden extends Web2Py, and the two are both undergoing rapid development, 
	the revision of Web2Py can be critical. Whilst the latest 'bleeding edge' version of Web2Py is usually stable,
	some Web2Py revisions have bugs which break a part of Sahana Eden. You can try upgrading to the latest 
	revision of Web2Py or else downgrading to an older version which does not exhibit this bug.

	Sometimes a new version of Sahana Eden may use features from a more recent Web2py than the currently 
	installed version.  This typically leads to an error ticket with a message indicating that some item was 
	not found.  Update to either the latest Web2py, or the latest known-stable Web2py revision, 
	the version number for which can be found in modules/s3_update_check.py

	It is also sometimes posted in the #sahana-eden IRC channel topic (see the Community chapter for 
	connecting to IRC).
	
	
// ---------------------------
*1. Basics*
  - you need a running environment of web2py
  - you need web2py/applications/eden <= your instance of eden
  
  - in .../web2py
  	# python web2py.py -a pass
  
	- start a browser 
		- and navigate to http://localhost:8000/welcome/default/index
		- log in (password is pass)
  		- go to "my applications" 
	    - go to application -> eden
			- log in (email/password of first registered user is admin)
		
		- or directly navigate to http://localhost:8000/eden
			- log in (email/password of first registered user is admin)

		- or select	'edit' and edit eden (however, you will most probably later 
	  	  edit the files directly in an editor)
	  
// ---------------------------
*2. .../models/000_config.py*
		- is NOT part of git (gitignore). 
		  For changes to be committed, please also edit: modules/templates/000_config.py

		- basic setting
			- the template (choose using intuition templatenames found in modules/templates)
			- security settings must now be somewhere else!?
			- override here the settings of your template ...
			
			- for that copy modules/templates/default to modules/templates/<yourtemplate>
			  and look there in config.py which settings exist
			
			
// ---------------------------
*3. modules/templates/<yourtemplate>/config.py*
	- vast number of options you can change. either there or override values in 000_config.py (see above)
	- at the bottom there is the section where you can select/deselect the used modules
	  (can also be done in 000_config.py, it is however more nice and clean to do it in the config.py files)
	  
// ---------------------------
*4. Favicon, footer and basic layout*
	- needs to be found out!

// ---------------------------
*5. Import*
		- go to desired data (e.g. Organisation, Staff, Shelters)
		- click 'Import' in the menue
		- select 'download template' => it will be a .cvs file
		- open template in libreoffice
		    - character set: UTF-8 (unicode)
			- selector ","
			- text delimiter """
			- quoted field as text
		- edit and save file (as CSV!)
		- upload	
		
	TODO: how do the many colums in the csv file correspond to the insert-mask (which contains fewer data)?	

// ---------------------------
*6. Export*

    TODO: how to export CSV
	
	csv should be included as one of the standard export file-types (http://write.flossmanuals.net/sahana-eden/data-export/).
	Unfortunately, I do not find the icon. It is, however, possible to export as XLS. this opens libreoffice and you can
	save the file in the csv fomat (komma, ", and text-filed in quotes).
	
	TODO: try to import such a file again (after changes)
	


// ---------------------------
*. *
// ---------------------------
*. *
// ---------------------------
*. *
// ---------------------------
*. *
// ---------------------------
*. *
// ---------------------------
*. *
// ---------------------------
*. *
// ---------------------------
*. *
// ---------------------------
*2. Incorporate a new model*

yourtaskhere: what you are trying to do
namebody    : something 'bigger' than your task

1. You need two files:

	models/<namebody>.py
	controllers/<namebody>.py
	edit text according to examples (e.g. asylumseeker.py)
	
	It is very important that the 'namebody' of your file matches
	the fist part of tablename = "<namebody>_<yourtaskhere>"

2. update CRUD texts
	see examles (e.g. models/asylumseeker.py)

	- you can see your page at eden/<namebody>/<yourtaskhere>
	
3. 	add an index.html
#cd eden/views
#mkdir <namebody>
#cp asylumseeker/index.html <namebody>
# edit <namebody>/index.html
# add to controller file:
	def index():
    	return dict()
	
	- now it should be possible to see: eden/<namebody>

4. Add model to system (also create a link in the main menu)
add to your config.py (in your template directory)
settings.modules["<namebody>"] = Storage(
        name_nice=T("<Namebody>"),
        module_type=2)

5. Add a menu at the side
	- edit modules/s3menus.py or <mytemplate>/menues.py => see examples there
	- add new module to active modules in <mytemplate>/confg.py

6. Write data to file
	- create one entry
	- click export as XLS
	- some soffice will open,
	- save file as csv (set filter to: delimiter "," (comma) and embrace text with '"')
	- edit 
	- save
7. Read data from file


questions:
 - how to incorporate upload facility for user classes?
 - where to steer the look-and-feel of the page (number of entries, search, downlowd-options,...)
 - how to make user classes work with 'standard' classes.
 - where to alter the frontpage?
 - should one edit s3dm, ... or something else
 - new modules like in 'book' or as a new class?
 - is there a 'read more' button for classes with many data-points?
 - where is the 'homepage'
 - what isy module_type? (config.py)
 settings.modules["housing"] = Storage(
        name_nice=T("Housing"),
        module_type=2)
 - do we need ansible  http://docs.ansible.com/ansible/quickstart.html
 - ... 
		


// skeleton to own class
1. change skeleton case sensitive to your name (e.g. housing)
2. add new module in models/00_tables.py
3. add controller and index functions in ./controller/housing.py
4. edit eden/views/housing/index.html


#
# migrating to other db / transformin to a real server
#

look at /web2py/application/welcome/private/appconfig.ini
this seem to have someting to do with it (see: http://www.web2py.com/books/default/chapter/29/01/introduction)


# some info (18.12.16) on working installarion scripts (from the ML-digest):
Normally for Developer mode, I install manually all the required libraries and install web2py and then EDEN. That should not be much of work.
For production mode, the scripts are maintained here: https://github.com/sahana/eden_deploy. I used this few month ago and they worked out of the box.
You can use it for developer mode as well for installing libraries and configuring them.
