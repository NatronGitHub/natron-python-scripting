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
	dialog.resize( 640, 100 )

	# UI creation #
	line01 = dialog.createStringParam("sep01","")
	line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line02 = dialog.createStringParam("sep02","")
	line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	# pulldown menu creation #
	renderFileParam = dialog.createFileParam("projectPath", "Natron file : ")

	renderInRangeParam = dialog.createStringParam("rangeIn", "In : ")
	renderInRangeParam.resize(50,50)
	renderInRangeParam.setAddNewLine(False)

	renderOutRangeParam = dialog.createStringParam("rangeOut", "Out : ")
	renderOutRangeParam.setAddNewLine(False)

	dialog.refreshUserParamsGUI()


	if dialog.exec_():
		print 'toto'

batchRender()