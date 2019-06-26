#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 12/06/2019.

from NatronEngine import*
from NatronGui import *
from PySide.QtGui import *


# SETS SELECTED NODES TO BE DISPLAYED IN ITALIC IN THE NODE GRAPH #

def nodeItalic_HTML():

	app = natron.getGuiInstance(0)
	selectedNodes = app.getSelectedNodes()

	for n in selectedNodes:
		myLabel = n.getLabel()

		# parse existing name #
		if '<i>' in myLabel:
			oldLabel = myLabel.replace('<i>', '')
			n.setLabel(oldLabel)
		else :
			italicLabel = '<i>' + myLabel
			n.setLabel(italicLabel)
