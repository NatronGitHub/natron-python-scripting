#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 25/01/2018.

from NatronEngine import*
from NatronGui import *
from PySide.QtGui import *


# SETS SELECTED READ NODES OUTPUT COMPONENTS TO RGBA #

def autoAlpha():

	app = natron.getGuiInstance(0)
	selectedNodes = app.getSelectedNodes()

	for n in selectedNodes:
		myID = n.getPluginID()

		if myID == "fr.inria.built-in.Read" or nodeID == 'fr.inria.openfx.ReadOIIO':

			newComponents = n.getParam("outputComponents")
			newComponents.set(0)
