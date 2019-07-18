#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 16/07/2019.

from NatronEngine import *
from NatronGui import *


def removeInput():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# get selected nodes #
	selectedNodes = app.getSelectedNodes()

	for currentNode in selectedNodes:

			currentNode.disconnectInput(0)