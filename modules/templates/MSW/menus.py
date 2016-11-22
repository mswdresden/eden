# -*- coding: utf-8 -*-

from gluon import *
from s3 import *
from s3layouts import *
try:
    from .layouts import *
except ImportError:
    pass
import s3menus as default

# Below is an example which you can base your own template's menus.py on
# - there are also other examples in the other templates folders

# =============================================================================
class S3MainMenu(default.S3MainMenu):
    """
        Custom Application Main Menu:

        #The main menu consists of several sub-menus, each of which can
        #be customised separately as a method of this class. The overall
        #composition of the menu is defined in the menu() method, which can
        #be customised as well:

        #Function        Sub-Menu                Access to (standard)

        #menu_modules()  the modules menu        the Eden modules
        #menu_gis()      the GIS menu            GIS configurations
        #menu_admin()    the Admin menu          System/User Administration
        #menu_lang()     the Language menu       Selection of the GUI locale
        #menu_auth()     the User menu           Login, Logout, User Profile
        #menu_help()     the Help menu           Contact page, About page

        #The standard uses the MM layout class for main menu items - but you
        #can of course use a custom layout class which you define in layouts.py.

        #Additional sub-menus can simply be defined as additional functions in
        #this class, and then be included in the menu() method.

        #Each sub-menu function returns a list of menu items, only the menu()
        #function must return a layout class instance.
    """

    # -------------------------------------------------------------------------
    @classmethod
    def menu(cls):
        """ Compose Menu """

        main_menu = MM()(

            # Modules-menu, align-left
            cls.menu_modules(),

            # Service menus, align-right
            # Note: always define right-hand items in reverse order!
            cls.menu_help(right=True),
            cls.menu_auth(right=True),
            cls.menu_lang(right=True),
            cls.menu_admin(right=True),
            cls.menu_gis(right=True)
        )
        return main_menu

    # -------------------------------------------------------------------------
    # msw: this is a simple way to overwrite the default menu_modules function
    #@classmethod
    #def menu_modules(cls):
    #    """ Custom Modules Menu """
    #
    #    return [
    #        homepage(),
    #        homepage("gis"),
    #        homepage("pr")(
    #            MM("Persons", f="person"),
    #            MM("Groups", f="group")
    #        ),
    #        MM("more", link=False)(
    #            homepage("dvi"),
    #            homepage("irs")
    #        ),
    #    ]
# -------------------------------------------------------------------------
    @classmethod
    def menu_modules(cls): 

        # ---------------------------------------------------------------------
        # Modules Menu
        # @todo: this is very ugly - cleanup or make a better solution
        # @todo: probably define the menu explicitly?
        #
        
        print 'msw: calling menu_modules(cls) in MSW/menus.py'
        
        menu_modules = []
        all_modules = current.deployment_settings.modules
        
        #msw
        #print 's3menus.py, menu_modules(cls):\n\t cls=',cls,'\n\t all_modules', all_modules
        
        # Home always 1st (commented because redundant/unnecessary)
        # msw
        module = all_modules["default"]
        menu_modules.append(MM(module.name_nice, c="default", f="index"))

        # Modules to hide due to insufficient permissions
        hidden_modules = current.auth.permission.hidden_modules()

        # The Modules to display at the top level (in order)
        for module_type in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            for module in all_modules:
                if module in hidden_modules:
                    continue
                _module = all_modules[module]
                if (_module.module_type == module_type):
                    if not _module.access:
                        menu_modules.append(MM(_module.name_nice, c=module, f="index"))
                    else:
                        groups = re.split("\|", _module.access)[1:-1]
                        menu_modules.append(MM(_module.name_nice,
                                               c=module,
                                               f="index",
                                               restrict=groups))

        # Modules to display off the 'more' menu
        modules_submenu = []
        for module in all_modules:
            if module in hidden_modules:
                continue
            _module = all_modules[module]
            if (_module.module_type == 10):
                if not _module.access:
                    modules_submenu.append(MM(_module.name_nice, c=module, f="index"))
                else:
                    groups = re.split("\|", _module.access)[1:-1]
                    modules_submenu.append(MM(_module.name_nice,
                                              c=module,
                                              f="index",
                                              restrict=groups))

        if modules_submenu:
            # Only show the 'more' menu if there are entries in the list
            module_more_menu = MM("more", link=False)(modules_submenu)
            menu_modules.append(module_more_menu)

        return menu_modules

# =============================================================================
class S3OptionsMenu(default.S3OptionsMenu):
    """
        #Custom Controller Menus

        #The options menu (left-hand options menu) is individual for each
        #controller, so each controller has its own options menu function
        #in this class.

        #Each of these option menu functions can be customised separately,
        #by simply overriding (re-defining) the default function. The
        #options menu function must return an instance of the item layout.

        #The standard menu uses the M item layout class, but you can of
        #course also use any other layout class which you define in
        #layouts.py (can also be mixed).

        #Make sure additional helper functions in this class don't match
        #any current or future controller prefix (e.g. by using an
        #underscore prefix).
    """

    #def cr(self):
        #""" CR / Shelter Registry """

        #return M(c="cr")(
                    #M("Camp", f="shelter")(
                        #M("New", m="create"),
                        #M("List All"),
                        #M("Map", m="map"),
                        #M("Import", m="import"),
                    #)
                #)
                
                
    #msw
    def org(self):
        #""" ORG / Organization Registry """
        return M(c="org")(
            M("Organizations", f="organisation")(
                M("New", m="create"),
                M("List All"),
                M("Search", m="search"),
                M("Import", m="import")
            ),
            M("Venues", f="office")(
                M("New", m="create"),
                M("List All"),
                #M("Map", m="map"),
                #M("Search", m="search"),
                M("Import", m="import")
            ),
        )

    # msw
    def asylumseeker(self):
        return M(c="asylumseeker")(
            M("Asylumseeker", f="person")(
                M("Create", m="create"),
                M("Import", m="import"),
                M("Report", m="report")
            )
        )
        
    # msw
    def residential(self):
        return M(c="residential")(
            M("Residential", f="dorm")( 
                M("Create", m="create"),
                M("List All"),
                M("Import", m="import"),
                M("Report", m="report"),
                M("Export", m="export")
            ),
            M("Asylumseeker", f="person")(
                #M("Create", m="create"),
                M("List All"),
                #M("Import", m="import"),
                #M("Report", m="report")
            ),
        )
        
     # msw
    def housing(self):
        return M(c="housing")(
            M("Housing", f="flat")(
                M("Create", m="create", right=True),
                M("Import", m="import", right=True),
                M("Report", m="report", right=True),
            )
        ) 
        
# END =========================================================================
