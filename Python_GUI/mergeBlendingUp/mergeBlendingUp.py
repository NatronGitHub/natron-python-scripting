#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 28/06/2019.

from NatronGui import *


# CYCLES THROUGH MERGE BELNDING MODES UPWARD #

def mergeBlendingUp():
	
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