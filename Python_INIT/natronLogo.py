#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 17/01/2018.

import os
import string
from NatronEngine import*
from os import*

# LISTS NATRON PLUGINS PATHS #

def natronLogo():
	print '\n'
	print '\n'
	print ''.join(file('/home/natron/.Natron/Python_INIT/logo.txt'))
