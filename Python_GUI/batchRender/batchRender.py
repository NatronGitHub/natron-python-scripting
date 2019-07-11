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


# BATCH RENDER #

def batchRender():

	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Batch render")

	# set dialog margins #
	dialog.setContentsMargins(0, 0, 10, 10)

	# set window size #
	dialog.setFixedSize( 340, 400 )

	########################### UI CREATION ###################################

	# separators #
	line01 = dialog.createStringParam("line01","")
	line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line02 = dialog.createStringParam("line02","")
	line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	# file path parameter #
	renderFileParam0 = dialog.createFileParam("projectPath0", "Natron file : ")

	# separators #
	line03 = dialog.createStringParam("line03","")
	line03.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line04 = dialog.createStringParam("line04","")
	line04.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	# range choice parameter #
	rangeList = dialog.createChoiceParam("rangeChoice","Frame Range : ")
	rangeList.addOption('Project','')
	rangeList.addOption('Custom','')

	# if viewer exists in comp, add it to the choice list #
	app.selectAllNodes()
	selectedNodes = app.getSelectedNodes()
	isViewer = 0

	for currentNode in selectedNodes:
		currentID = currentNode.getPluginID()

		if currentID == 'fr.inria.built-in.Viewer':
			currentLabel = currentNode.getLabel()
			rangeList.addOption(str(currentLabel),'')

	app.clearSelection()
	
	rangeList.setDefaultValue('Project')
	rangeList.restoreDefaultValue()

	# separators #
	line05 = dialog.createStringParam("line05","")
	line05.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line06 = dialog.createStringParam("line06","")
	line06.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

 	# IN parameter #
	inRange = dialog.createIntParam("inRange","Start Frame : ")

 	# OUT parameter #
	outRange = dialog.createIntParam("outRange","End Frame : ")

	sep01 = dialog.createSeparatorParam("sep01","")

	###########################################################################

	dialog.refreshUserParamsGUI()



	if dialog.exec_():
		print 'toto'







batchRender()