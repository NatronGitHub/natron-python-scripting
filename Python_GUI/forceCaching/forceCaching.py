#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 25/01/2018.

import NatronEngine
from NatronGui import *


# ENABLE/DISABLE FORCE CACHING FOR SELECTED NODES #

def forceCaching():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# we store selected node(s) in a list #
	selectedNodes = app.getSelectedNodes()

	# cycle every selected node #
	for n in selectedNodes:
		
		cacheParam = n.getParam("forceCaching")
		cacheValue = n.getParam("forceCaching").get()

		if cacheValue == False:
			cacheParam.set(1)

		if cacheValue == True:
			cacheParam.set(0)