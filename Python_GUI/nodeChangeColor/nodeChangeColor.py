#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 17/01/2018.

import os
from NatronGui import *
from PySide.QtGui import *


# SETS NODE COLOR FOR SELECTED NODES #

def nodeChangeColor():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# create modal dialog #
	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Change node color")

	# set dialog margins #
	dialog.setContentsMargins(0, 0, 10, 10)

	# create Color picker box #
	myColor = dialog.createColorParam("myColor","Color : ", 0)
	myColor.set(1,1,1,0)

	dialog.refreshUserParamsGUI()

	if dialog.exec_():
		newColor = dialog.getParam("myColor").get()

		selectedNodes = app.getSelectedNodes()

		for currentNode in selectedNodes:

			curentNodeLabel = currentNode.getLabel()

			currentNode.setColor(newColor[0],newColor[1],newColor[2])

			os.write( 1, '\n' + str(curentNodeLabel) + ' color changed to [R :' + str(newColor[0]) + ' , G: ' + str(newColor[1]) + ' , B: ' + str(newColor[2]) +']\n' )