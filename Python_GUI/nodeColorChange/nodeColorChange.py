#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 17/01/2018.

import os
from NatronEngine import*
from NatronGui import *
from PySide.QtGui import *


# SETS NODE COLOR FOR SELECTED NODES #

def nodeColorChange():

	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# create Color picker box #
	myColor = dialog.createColorParam("myColor","Color : ", 0)
	myColor.set(1,1,1,0)

	dialog.refreshUserParamsGUI()

	if dialog.exec_():
		newColor = dialog.getParam("myColor").get()

		selectedNodes = app.getSelectedNodes()
		for n in selectedNodes:
			n.setColor(newColor[0],newColor[1],newColor[2])

	print ('Node(s) color changed to R : ' + str(newColor[0]) + ' , G : ' + str(newColor[1]) + ' , B : ' + str(newColor[2]) )
	os.write( 1, '\n' + 'Node(s) color changed to R : ' + str(newColor[0]) + ' , G : ' + str(newColor[1]) + ' , B : ' + str(newColor[2]) + '\n' )