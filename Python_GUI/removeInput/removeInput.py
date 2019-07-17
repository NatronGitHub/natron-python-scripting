from NatronEngine import *
from NatronGui import *


def removeInput():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# get selected nodes #
	selectedNodes = app.getSelectedNodes()

	for currentNode in selectedNodes:

			currentNode.disconnectInput(0)