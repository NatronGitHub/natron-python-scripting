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