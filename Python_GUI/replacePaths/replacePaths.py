#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 19/06/2019.

import os
from NatronGui import *
from PySide.QtGui import *
import NatronEngine


# REPLACE 'READ' OR 'WRITE' NODE PATH #

def replacePaths():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# create dialog window #
	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Replace paths")

	# set dialog margins #
	dialog.setContentsMargins(0, 0, 10, 10)

	# set window size #
	dialog.resize( 400, 100 )

	# UI creation #
	line01 = dialog.createStringParam("line01","")
	line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line02 = dialog.createStringParam("line02","")
	line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	# user list #
	myList = dialog.createChoiceParam("list00","Nodes : ")
	entries = [ ("Selected", ""),("All", "") ]
	myList.setOptions(entries)
	myList.setDefaultValue("Selected")
	myList.restoreDefaultValue()

	sep01 = dialog.createSeparatorParam("sep01","")

	oldPath = dialog.createPathParam("oldPath","Source path : ")
	newPath = dialog.createPathParam("newPath","Destination path : ")


	line03 = dialog.createStringParam("line03","")
	line03.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	sep02 = dialog.createSeparatorParam("sep02","")


	# Refresh UI #
	dialog.refreshUserParamsGUI()




	if dialog.exec_():

		userChoice = myList.getValue()

		if userChoice == 1:
			app.selectAllNodes()

		# get selected nodes #
		selectedNodes = app.getSelectedNodes()

		for currentNode in selectedNodes:

			myID = currentNode.getPluginID()

			if myID == "fr.inria.built-in.Read" :

				oldPathParamValue = oldPath.getValue()

				newPathParamValue = newPath.getValue()

				currentPath = str(currentNode.getParam('filename').get())
				print 'Old path : ' + currentPath

				currentPath = currentPath.replace(oldPathParamValue,newPathParamValue)
				print 'New path : ' + currentPath
				
				oldReadPath = currentNode.getParam('filename').set(currentPath)
