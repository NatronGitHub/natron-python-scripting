#WINDOWS : where natron -> trouver le dossier d'installation
#LINUX : which natron

#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 29/06/2019.

#import os
#import string
import os
import string
from NatronEngine import*
from NatronGui import *
from PySide.QtGui import *
import NatronEngine


# TRACKER TO ROTO #

def batchRender():

	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Batch render")

	# set dialog margins #
	dialog.setContentsMargins(0, 0, 10, 10)

	# set window size #
	dialog.resize( 800, 200 )
	#dialog.setFixedSize( 800, 100 )

	# UI creation #
	line01 = dialog.createStringParam("line01","")
	line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line02 = dialog.createStringParam("line02","")
	line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	# enable/disable parameter #
	checkBox0 = dialog.createBooleanParam("check0", "")

	# file path parameter #
	renderFileParam0 = dialog.createFileParam("projectPath0", "Natron file : ")
	renderFileParam0.setAddNewLine(False)

	# frame range parameter #
	renderRangeParam0 = dialog.createIntParam("range0", "Range : ")
	renderRangeParam0.setAddNewLine(False)

	outputPath0 = dialog.createPathParam("outputPath0", "Output : ")
	outputPath0.setAddNewLine(False)

	sep01 = dialog.createSeparatorParam("sep01","")

	#############################################################################

	# enable/disable parameter #
	checkBox1 = dialog.createBooleanParam("check1", "")

	# file path parameter #
	renderFileParam1 = dialog.createFileParam("projectPath1", "Natron file : ")
	renderFileParam1.setAddNewLine(False)

	# frame range parameter #
	renderRangeParam1 = dialog.createIntParam("range1", "Range : ")
	renderRangeParam1.setAddNewLine(False)

	sep02 = dialog.createSeparatorParam("sep02","")

	#############################################################################

	# enable/disable parameter #
	checkBox2 = dialog.createBooleanParam("check2", "")

	# file path parameter #
	renderFileParam2 = dialog.createFileParam("projectPath2", "Natron file : ")
	renderFileParam2.setAddNewLine(False)

	# frame range parameter #
	renderRangeParam2 = dialog.createIntParam("range2", "Range : ")
	renderRangeParam2.setAddNewLine(False)

	dialog.refreshUserParamsGUI()


	if dialog.exec_():
		print 'toto'

batchRender()