from NatronGui import *

def mergeBlendingMinus():
	
	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# we store selected node(s) in a list #
	selectedNodes = app.getSelectedNodes()

	# cycle every selected node #
	for node in selectedNodes :

		# get node type #
		nodeID = node.getPluginID()

		# check if selected node is a 'Merge' node #
		if nodeID == "net.sf.openfx.MergePlugin":
			
			oldOperation = node.getParam('operation').get()
			newOperation = oldOperation - 1

			node.getParam('operation').set(newOperation)