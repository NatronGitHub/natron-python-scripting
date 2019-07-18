#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 18/07/2019.

from NatronEngine import *
from NatronGui import *


def connectNodes():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# get selected nodes #
	selectedNodes = app.getSelectedNodes()

	numNodes = len(selectedNodes)

	lastIndex = numNodes - 1

	lastNode = selectedNodes[lastIndex]
	counter = 0

	for currentNode in selectedNodes:

		if numNodes >1 :
			if counter != lastIndex:
				currentNode.disconnectInput(0)
				if currentNode.canConnectInput(0,lastNode) == 1:
					currentNode.connectInput(0,lastNode)

		counter += 1