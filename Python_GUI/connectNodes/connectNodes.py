from NatronEngine import *
from NatronGui import *


def connectNodes():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# get selected nodes #
	selectedNodes = app.getSelectedNodes()

	firstNode = selectedNodes[0]
	secondNode = selectedNodes[1]

	if len(selectedNodes) == 2 :

		if firstNode.canConnectInput(0,secondNode) == 1:
			firstNode.connectInput(0,secondNode)