#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 17/01/2018.

#from NatronEngine import*
from NatronGui import *
from PySide.QtGui import *


# SETS FRAME RANGE FOR SELECTED 'READ' NODES #

def nodeChangeFrameRange():

	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Change frame range")

	# set dialog margins #
	dialog.setContentsMargins(0, 0, 10, 10)

	dialog.resize( 240, 100 )

	# create Color picker box #
	firstFrame = dialog.createIntParam("firstFrame","In :")
	lastFrame = dialog.createIntParam("lastFrame","Out :")
	lastFrame.setAddNewLine(False)
	line01 = dialog.createSeparatorParam("line01","")

	dialog.refreshUserParamsGUI()

	if dialog.exec_():
		newFirstFrame = dialog.getParam("firstFrame").getValue()
		newLastFrame = dialog.getParam("lastFrame").getValue()


		selectedNodes = app.getSelectedNodes()

		for n in selectedNodes:
			myID = n.getPluginID()

			if myID == "fr.inria.built-in.Read" :

				oldFirstFrame = n.getParam("firstFrame")
				oldFirstFrame.set(newFirstFrame)
				oldLastFrame = n.getParam("lastFrame")
				oldLastFrame.set(newLastFrame)