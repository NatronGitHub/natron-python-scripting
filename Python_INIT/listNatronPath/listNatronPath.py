#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 17/01/2018.

import os
import string
from NatronEngine import*
from os import*

# LISTS NATRON PLUGINS PATHS #

def listNatronPath():
	myPath = natron.getNatronPath()
	listIndex = 0

	for p in myPath:
		print ('   ' + myPath[listIndex])
		listIndex +=1
