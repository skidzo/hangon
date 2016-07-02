import os,sys

try:

    __file__ = __file__

except NameError:

    __file__ = sys.argv[0]

    print("Running:", __file__,"...")

__root__ = os.path.dirname(os.path.realpath(__file__))

#if os.path.exists(os.path.join(__root__,"library.zip")):
#    __root__ = os.path.join(__root__,"library.zip")
#    _basePath = os.path.dirname(__file__)
#
#    #print ("at location:", __root__)
#    __examples__ = None
#else:
#    __examples__ = os.path.realpath(os.path.join(__root__,"example"))

# Python3
if os.name == 'nt':
    # We are currently only developing for Windows-Clients
    # Checking if environment is set-up correctly

    #if not os.path.isdir(__root__): # check for dev-environment
    #    __root__ = 'C:/Znake-Tool/'  # else set release-env
    sys.path.append(__root__)
else:
    sys.path.append(__root__)


from actiontimerApp import ActiontimerApp
from basicelements import IntervallInput