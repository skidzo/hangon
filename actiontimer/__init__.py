import os,sys

try:

    __file__ = __file__

except NameError:

    __file__ = sys.argv[0]

    #print("Running:", __file__,"...")

__root__ = os.path.dirname(os.path.realpath(__file__))

# Python3
if os.name == 'nt':
    # Windows
    # Checking if environment is set-up correctly
    #if not os.path.isdir(__root__): # check for dev-environment
    sys.path.append(__root__)
else:
    # Others
    sys.path.append(__root__)


from actiontimerApp import ActiontimerApp
from basicelements import IntervallInput
