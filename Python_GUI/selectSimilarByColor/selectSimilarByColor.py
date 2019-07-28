#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 06/07/2019.

import NatronEngine
from NatronGui import *


# SELECT SIMILAR NODES BY COLOR #

def selectSimilarByColor():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# get selected nodes #
	selectedNodes = app.getSelectedNodes()

	# cycle through every selected nodes #
	for node in selectedNodes:

		# get user selected node color #
		referenceColor = node.getColor()

	if len(selectedNodes) == 1:

		# select all nodes #
		app.selectAllNodes()

		# get selected nodes #
		selectedNodes = app.getSelectedNodes()

		# deselect all nodes #
		app.clearSelection()

		# cycle through every selected nodes #
		for currentNode in selectedNodes:

			# get current node color #
			currentColor = currentNode.getColor()
			
			if currentColor[0] == referenceColor[0] and currentColor[1] == referenceColor[1] and currentColor[2] == referenceColor[2]:

				app.selectNode(currentNode,False)




selectSimilarByColor()