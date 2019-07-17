#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 25/01/2018.

import NatronEngine
from NatronGui import *


# ENABLE/DISABLE FORCE CACHING FOR SELECTED NODES #

def invertSelection():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# get user selected nodes #
	originalNodes = app.getSelectedNodes()

	# select all nodes #
	app.selectAllNodes()

	# cycle every selected node #
	for currentNode in originalNodes:
		
		# originally selected nodes get unselected #
		app.deselectNode(currentNode)