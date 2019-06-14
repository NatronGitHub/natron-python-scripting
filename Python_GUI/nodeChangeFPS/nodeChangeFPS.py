#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 17/01/2018.

import os
from NatronEngine import*
from NatronGui import *
from PySide.QtGui import *


# SETS FPS FOR SELECTED 'READ' NODES #

def nodeChangeFPS():

	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# create Color picker box #
	fpsInput = dialog.createIntParam("fpsInput","New FPS : ")
	fpsInput.set(25)
	line01 = dialog.createSeparatorParam("line01","")

	dialog.refreshUserParamsGUI()

	if dialog.exec_():
		newFPS = dialog.getParam("fpsInput").get()
		selectedNodes = app.getSelectedNodes()

		for n in selectedNodes:
			myID = n.getPluginID()

			if myID == "fr.inria.built-in.Read" :

				nodeFramerate = n.getParam("frameRate")
				nodeFramerate.set(newFPS)

				print ('Read Node(s) set to : ') + str(nodeFramerate.get()) + (' fps.')
				os.write(1, '\n' + 'Read Node(s) set to : ' + str(nodeFramerate.get()) + ' fps.' + '\n' )

				customFPS = n.getParam("customFps")
				customFPS.set(1)