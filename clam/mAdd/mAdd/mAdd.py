#!/usr/bin/env python
#-*- coding:utf-8 -*-

###############################################################
# CLAM: Computational Linguistics Application Mediator
# -- Service Configuration File (Template) --
#       by Maarten van Gompel (proycon)
#       Centre for Language and Speech Technology / Language Machines
#       Radboud University Nijmegen
#
#       https://proycon.github.io/clam
#
#       Licensed under GPLv3
#
###############################################################

#Consult the CLAM manual for extensive documentation

#If we run on Python 2.7, behave as much as Python 3 as possible
from __future__ import print_function, unicode_literals, division, absolute_import

from clam.common.parameters import *
from clam.common.formats import *
from clam.common.converters import *
from clam.common.viewers import *
from clam.common.data import *
from clam.common.digestauth import pwhash
import clam
import sys
import os

REQUIRE_VERSION = 2.3

CLAMDIR = clam.__path__[0] #directory where CLAM is installed, detected automatically
WEBSERVICEDIR = os.path.dirname(os.path.abspath(__file__)) #directory where this webservice is installed, detected automatically

# ======== GENERAL INFORMATION ===========

# General information concerning your system.


#The System ID, a short alphanumeric identifier for internal use only
SYSTEM_ID = "mAdd"
#System name, the way the system is presented to the world
SYSTEM_NAME = "mAdd"

#An informative description for this system (this should be fairly short, about one paragraph, and may not contain HTML)
SYSTEM_DESCRIPTION = " mAdd: Coadd the reprojected images in an input list to form an output mosaic with FITS header keywords specified in a header file. Creates two output files, one containing the coadded pixel values, and the other containing coadded pixel area values. The pixel area values can be used as a weighting function if the output pixel values are themselves to be coadded with other projected images, and may also be used in validating the fidelity of the output pixel values."

#A version label of the underlying tool and/or this CLAM wrapper
#(If you can derive this dynamically then that is strongly recommended!)
#SYSTEM_VERSION = 0.1

#The author(s) of the underlying tool and/or this CLAM wrapper
#(If you can derive this dynamically then that is strongly recommended!)
#SYSTEM_AUTHOR = ""

#How to reach the authors?
#SYSTEM_EMAIL = ""

# ======== LOCATION ===========

#Either add a section for your host here, or
#specify these variables in an external yaml file
#called $hostname.yaml or config.yaml and use the loadconfig() mechanism.
#Such an external file will be looked for my default and is the recommended way.

host = os.uname()[1]
if host == "localhost":
    #The root directory for CLAM, all project files, (input & output) and
    #pre-installed corpora will be stored here. Set to an absolute path:
    ROOT = "/tmp/clam.projects/"

    #The URL of the system (If you start clam with the built-in webserver, you can override this with -P)
    PORT= 8080

    #The hostname of the system. Will be automatically determined if not set. (If you start clam with the built-in webserver, you can override this with -H)
    #Users *must* make use of this hostname and no other (even if it points to the same IP) for the web application to work.
    HOST = 'localhost'

    #If the webservice runs in another webserver (e.g. apache, nginx, lighttpd), and it
    #doesn't run at the root of the server, you can specify a URL prefix here:
    #URLPREFIX = "/myservice/"

    #Optionally, you can force the full URL CLAM has to use, rather than rely on any autodetected measures:
    #FORCEURL = "http://localhost.com"

    # ======== AUTHENTICATION & SECURITY ===========

    #Users and passwords

    #set security realm, a required component for hashing passwords (will default to SYSTEM_ID if not set)
    #REALM = SYSTEM_ID

    USERS = None #no user authentication/security (this is not recommended for production environments!)
    #If you want to enable user-based security, you can define a dictionary
    #of users and (hashed) passwords here. The actual authentication will proceed
    #as HTTP Digest Authentication. Although being a convenient shortcut,
    #using pwhash and plaintext password in this code is not secure!!

    #USERS = { user1': '4f8dh8337e2a5a83734b','user2': pwhash('username', REALM, 'secret') }

    ADMINS = None #List of usernames that are administrator and can access the administrative web-interface (on URL /admin/)
else:
    #This invokes the automatic loader, do not change it;
    #it will try to find a file named $system_id.$hostname.yml or just $hostname.yml, where $hostname
    #is the auto-detected hostname of this system. Alternatively, it tries a static $system_id.config.yml or just config.yml .
    #You can also set an environment variable CONFIGFILE to specify the exact file to load at run-time.
    #It will look in several paths including the current working directory and the path this settings script is loaded from.
    #Such an external configuration file simply defines variables that will be imported here. If it fails to find
    #a configuration file, an exception will be raised.
    loadconfig(__name__)





#Amount of free memory required prior to starting a new process (in MB!), Free Memory + Cached (without swap!). Set to 0 to disable this check (not recommended)
REQUIREMEMORY = 0

#Maximum load average at which processes are still started (first number reported by 'uptime'). Set to 0 to disable this check (not recommended)
#MAXLOADAVG = 4.0

#Minimum amount of free diskspace in MB. Set to 0 to disable this check (not recommended)
#DISK = '/dev/sda1' #set this to the disk where ROOT is on
#MINDISKSPACE = 10

#The amount of diskspace a user may use (in MB), this is a soft quota which can be exceeded, but creation of new projects is blocked until usage drops below the quota again
#USERQUOTA = 100

#The secret key is used internally for cryptographically signing session data, in production environments, you'll want to set this to a persistent value. If not set it will be randomly generated.
#SECRET_KEY = 'mysecret'

#Allow Asynchronous HTTP requests from **web browsers** in following domains (sets Access-Control-Allow-Origin HTTP headers), by default this is unrestricted
#ALLOW_ORIGIN = "*"

# ======== WEB-APPLICATION STYLING =============

#Choose a style (has to be defined as a CSS file in clam/style/ ). You can copy, rename and adapt it to make your own style
STYLE = 'classic'

# ======== ENABLED FORMATS ===========

#In CUSTOM_FORMATS you can specify a list of Python classes corresponding to extra formats.
#You can define the classes first, and then put them in CUSTOM_FORMATS, as shown in this example:

#class MyXMLFormat(CLAMMetaData):
#    attributes = {}
#    name = "My XML format"
#    mimetype = 'text/xml'

# CUSTOM_FORMATS = [ MyXMLFormat ]

# ======= INTERFACE OPTIONS ===========

#Here you can specify additional interface options (space separated list), see the documentation for all allowed options
#INTERFACEOPTIONS = "inputfromweb" #allow CLAM to download its input from a user-specified url

# ======== PREINSTALLED DATA ===========

#INPUTSOURCES = [
#    InputSource(id='sampledocs',label='Sample texts',path=ROOT+'/inputsources/sampledata',defaultmetadata=PlainTextFormat(None, encoding='utf-8') ),
#]

# ======== PROFILE DEFINITIONS ===========

#Define your profiles here. This is required for the project paradigm, but can be set to an empty list if you only use the action paradigm.

PROFILES = [
    Profile(
        InputTemplate('imgdir', PlainTextFormat,"input FITS files",
            StaticParameter(id='encoding',name='Encoding',description='The character encoding of the file', value='utf-8'), 
            extension='.fits',
            multi=True
        ),            
        InputTemplate('images', PlainTextFormat,"ASCII table (generated by mImgtbl) containing metadata for all images to be reprojected.",
            StaticParameter(id='encoding',name='Encoding',description='The character encoding of the file', value='utf-8'), 
            extension='.tbl',
            unique=True
        ),        
        InputTemplate('template', PlainTextFormat,"FITS header template to be used in generation of output FITS.",
            StaticParameter(id='encoding',name='Encoding',description='The character encoding of the file', value='utf-8'), 
            extension='.hdr',
            unique=True 
        ),
        #------------------------------------------------------------------------------------------------------------------------
        OutputTemplate('out',PlainTextFormat,'Name of output FITS image.',
            SetMetaField('encoding','utf-8'), #note that encoding is required if you work with PlainTextFormat
            filename='out.fits',
            unique=True
        ),
    )
]

# ======== COMMAND ===========

#The system command for the project paradigm.
#It is recommended you set this to small wrapper
#script around your actual system. Full shell syntax is supported. Using
#absolute paths is preferred. The current working directory will be
#set to the project directory.
#
#You can make use of the following special variables,
#which will be automatically set by CLAM:
#     $INPUTDIRECTORY  - The directory where input files are uploaded.
#     $OUTPUTDIRECTORY - The directory where the system should output
#                        its output files.
#     $TMPDIRECTORY    - The directory where the system should output
#                        its temporary files.
#     $STATUSFILE      - Filename of the .status file where the system
#                        should output status messages.
#     $DATAFILE        - Filename of the clam.xml file describing the
#                        system and chosen configuration.
#     $USERNAME        - The username of the currently logged in user
#                        (set to "anonymous" if there is none)
#     $PARAMETERS      - List of chosen parameters, using the specified flags
#
COMMAND = WEBSERVICEDIR + "/mAdd_wrapper.py $DATAFILE $STATUSFILE $OUTPUTDIRECTORY"

#Or for the shell variant:
#COMMAND = WEBSERVICEDIR + "/mAdd_wrapper.sh $STATUSFILE $INPUTDIRECTORY $OUTPUTDIRECTORY $PARAMETERS"

#Or if you only use the action paradigm, set COMMAND = None

# ======== PARAMETER DEFINITIONS ===========

#The global parameters (for the project paradigm) are subdivided into several
#groups. In the form of a list of (groupname, parameters) tuples. The parameters
#are a list of instances from common/parameters.py

PARAMETERS =  [
    ('Switches', [
        BooleanParameter(id='n',name='n',description='Co-addition ignores weighting by pixel areas and performs coaddition based only on pixel postions. This flag refers to input images; the area file for the output image will still be created.'),
        ChoiceParameter(id='a',name='a',description='Select type of averaging to be done on accumulated pixel values (either mean or median). To generate a map showing counts of how many times each pixel was overlapped by the input images, use count.', choices=['','mean','median','count'],default=''),
        BooleanParameter(id='e',name='e',description='Enables exact size mode. The output image will match the header template exactly, instead of shrinking the output to fit the data.'),   
        ChoiceParameter(id='d',name='d',description='Turns on debugging to the specified level (1-3).', choices=['0','1','2','3'],default='0'),        
        #StringParameter(id='author',name='Author',description='Sign output metadata with the specified author name',maxlength=255),
    ] )
]
    


# ======= ACTIONS =============

#The action paradigm is an independent Remote-Procedure-Call mechanism that
#allows you to tie scripts (command=) or Python functions (function=) to URLs.
#It has no notion of projects or files and must respond in real-time. The syntax
#for commands is equal to those of COMMAND above, any file or project specific
#variables are not available though, so there is no $DATAFILE, $STATUSFILE, $INPUTDIRECTORY, $OUTPUTDIRECTORY or $PROJECT.

ACTIONS = [
    #Action(id='multiply',name='Multiply',parameters=[IntegerParameter(id='x',name='Value'),IntegerParameter(id='y',name='Multiplier'), command=sys.path[0] + "/actions/multiply.sh $PARAMETERS" ])
    #Action(id='multiply',name='Multiply',parameters=[IntegerParameter(id='x',name='Value'),IntegerParameter(id='y',name='Multiplier'), function=lambda x,y: x*y ])
]

# ======= FORWARDERS =============

#Global forwarders call a remote service, passing a backlink for the remote service to download an archive of all the output data. The remote service is expected to return a redirect (HTTP 302) . CLAM will insert the backlink where you put $BACKLINK in the url:

#FORWARDERS = [
    #Forwarder(id='otherservice', name="Other service", description="", url="https://my.service.com/grabfrom=$BACKLINK")
#]

# ======== DISPATCHING (ADVANCED! YOU CAN SAFELY SKIP THIS!) ========

#The dispatcher to use (defaults to clamdispatcher.py), you almost never want to change this
#DISPATCHER = 'clamdispatcher.py'

#DISPATCHER_POLLINTERVAL = 30   #interval at which the dispatcher polls for resource consumption (default: 30 secs)
#DISPATCHER_MAXRESMEM = 0    #maximum consumption of resident memory (in megabytes), processes that exceed this will be automatically aborted. (0 = unlimited, default)
#DISPATCHER_MAXTIME = 0      #maximum number of seconds a process may run, it will be aborted if this duration is exceeded.   (0=unlimited, default)
#DISPATCHER_PYTHONPATH = []        #list of extra directories to add to the python path prior to launch of dispatcher

#Run background process on a remote host? Then set the following (leave the lambda in):
#REMOTEHOST = lambda: return 'some.remote.host'
#REMOTEUSER = 'username'

#For this to work, the user under which CLAM runs must have (passwordless) ssh access (use ssh keys) to the remote host using the specified username (ssh REMOTEUSER@REMOTEHOST)
#Moreover, both systems must have access to the same filesystem (ROOT) under the same mountpoint.
