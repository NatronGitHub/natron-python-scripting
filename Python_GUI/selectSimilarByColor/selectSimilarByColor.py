#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 06/07/2019.

import NatronEngine
from NatronGui import *


# SELECT SIMILAR NODES #

def selectSimilarByClass():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# get selected nodes #
	selectedNodes = app.getSelectedNodes()

	for node in selectedNodes:
		referenceID = node.getPluginID()

	if len(selectedNodes) == 1:

		app.selectAllNodes()
		selectedNodes = app.getSelectedNodes()

		for currentNode in selectedNodes:
			currentID = currentNode.getPluginID()
			
			if currentID != referenceID:
				app.deselectNode(currentNode)