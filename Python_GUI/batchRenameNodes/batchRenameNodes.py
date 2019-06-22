#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 17/01/2018.

from NatronEngine import*
from NatronGui import *
from PySide.QtGui import *


# SETS FRAME RANGE FOR SELECTED 'READ' NODES #

def batchRenameNodes():

	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Batch rename")

	# set dialog margins #
	dialog.setContentsMargins(0, 0, 10, 10)

	# create user input fields #
	field1 = dialog.createStringParam("renameField","name : ")
	#field1.setAddNewLine(False)

	line01 = dialog.createSeparatorParam("line01","")

	field2 = dialog.createStringParam("appendField","add : ")
	#field2.setAddNewLine(False)

	line02 = dialog.createSeparatorParam("line02","")

	field3 = dialog.createStringParam("replace","replace : ")
	#field3.setAddNewLine(False)

	line03 = dialog.createSeparatorParam("line03","")

	dialog.refreshUserParamsGUI()

	# if user press 'OK' #
	if dialog.exec_():
		print ('toto')


batchRenameNodes()