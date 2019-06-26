#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 23/06/2019.

import os
import string
from NatronEngine import*
from NatronGui import *
from PySide.QtGui import *


# BATCH RENAME NODES #

def batchRenameNodes():

	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Batch rename")

	# set dialog margins #
	dialog.setContentsMargins(0, 0, 10, 10)

	# set window size #
	dialog.resize( 300, 170 )

	# create user input fields #
	field1 = dialog.createStringParam("renameField","name : ")
	#field1.setAddNewLine(False)

	line01 = dialog.createSeparatorParam("line01","")

	field2 = dialog.createStringParam("appendField","add : ")
	#field2.setAddNewLine(False)

	line02 = dialog.createSeparatorParam("line02","")

	field3 = dialog.createStringParam("replaceField1","replace : ")
	field4 = dialog.createStringParam("replaceField2","by : ")	
	field4.setAddNewLine(False)

	line03 = dialog.createSeparatorParam("line03","")

	dialog.refreshUserParamsGUI()

	# if user press 'OK' #
	if dialog.exec_():
		selectedNodes = app.getSelectedNodes()

		# we initialize a counter #
		counter = 0
		digit = ''

		# we check every selcted node name #
		for nodes in selectedNodes:

			# we grab current node name #
			oldName = nodes.getLabel()

			# we grab values entered by user #
			newName = dialog.getParam("renameField").get()
			newAdd = dialog.getParam("appendField").get()
			newReplace1 = dialog.getParam("replaceField1").get()
			newReplace2 = dialog.getParam("replaceField2").get()


			if newName != '':
				oldName = newName
				digit = counter
				counter += 1

			if newAdd != '':
				oldName = str(oldName) + str(newAdd)

			if newReplace1 != '':
				oldName = oldName.replace( str(newReplace1), str(newReplace2) )


			oldName = str(oldName) + str(counter)
			nodes.setLabel(oldName)