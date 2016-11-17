

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
sudo apt-get -y install python-imaging
sudo apt-get -y install python-matplotlib
sudo apt-get -y install python-requests
sudo apt-get -y install python-xlwt
sudo apt-get -y install build-essential
sudo apt-get clean

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

###
# msw's howto:
Incorporate a new model:

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

4. Add a link in the main menu
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
		
