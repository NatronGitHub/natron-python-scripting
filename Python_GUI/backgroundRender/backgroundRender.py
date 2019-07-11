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

def backgroundRender():

	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Batch render")

	# set dialog margins #
	dialog.setContentsMargins(0, 0, 10, 10)

	# set window size #
	dialog.setFixedSize( 340, 150 )

	########################### UI CREATION ###################################

	# separators #
	line01 = dialog.createStringParam("line01","")
	line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line02 = dialog.createStringParam("line02","")
	line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	# range choice parameter #
	rangeList = dialog.createChoiceParam("rangeChoice","Frame Range : ")
	rangeList.addOption('Project','')
	rangeList.addOption('Custom','')

	# if a viewer exists in comp, add it to the choice list #
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
	line03 = dialog.createStringParam("line03","")
	line03.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line04 = dialog.createStringParam("line04","")
	line04.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

 	# IN parameter #
	inRange = dialog.createIntParam("inRange","Start Frame : ")

 	# OUT parameter #
	outRange = dialog.createIntParam("outRange","End Frame : ")
	outRange.setAddNewLine(False)

	###########################################################################

	dialog.refreshUserParamsGUI()


	# user press OK button 
	if dialog.exec_():

		# grab current project name #
		projectName = app.getProjectParam('projectName').get()
		projectName = os.path.splitext(projectName)[0]

		# save the project #
		app.saveProjectAs(projectName)

		# grab range user choice #
		userChoice = rangeList.get()


		
		# 'Project' is selected #
		if userChoice == 0 :
			print 'Project frame range selected'

			# get project frame range #
			frameRange = app.getProjectParam('frameRange').get()
			inFrame = frameRange[0]
			outFrame = frameRange[1]

			print inFrame
			print outFrame

		# 'Custom' is selected #
		if userChoice == 1 :
			print 'Custom frame range selected'

			# get user frame range #
			inFrame = inRange.get()
			outFrame = outRange.get()

			print inFrame
			print outFrame

			renderRange = str(inFrame) + '-' + str(outFrame)

		# a 'Viewer' is selected #
		if userChoice >1 :
			print 'Viewer frame range selected'

			# we grab selected 'viewer' #
			viewerChoice = rangeList.getOption(userChoice)

			# select all nodes in Node Graph #
			app.selectAllNodes()
			selectedNodes = app.getSelectedNodes()

			# cycle through every selected nodes #
			for currentNode in selectedNodes:

				# get current node ID #
				currentID = currentNode.getPluginID()

				# if the current node's ID is of 'viewer' type #
				if currentID == 'fr.inria.built-in.Viewer':

					# then we grab its 'label' #
					viewerLabel = currentNode.getLabel()

					# select it #
					myViewer = app.getViewer(viewerLabel)

					# get its frame range #
					currentRange = myViewer.getFrameRange()
					inFrame = currentRange[0]
					outFrame = currentRange[1]

					print inFrame
					print outFrame

					app.clearSelection()





backgroundRender()