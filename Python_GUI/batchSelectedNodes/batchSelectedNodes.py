import NatronEngine
from NatronGui import *
from PySide.QtGui import *


def batchSelectedNodes():

	# get current Natron instance running in memory #
	# app = natron.getGuiInstance(0)
	# replaced below to get active instead of first instance
	myApp = natron.getActiveInstance()
	myAppGui = natron.getGuiInstance( myApp.getAppID() )

	# get user selected nodes #
	originalNodes = myAppGui.getSelectedNodes()

	# check if at least one node has been selected #
	if len(originalNodes) == 0:
		warning = natron.warningDialog("batch Selected Nodes","Select at least one node. \n This script apply selected action to each selected node")
	else :
		# create dialog window #
		dialog = myAppGui.createModalDialog()
		# set dialog title #
		dialog.setWindowTitle("Batch Selected Nodes")
		# set dialog margins #
		dialog.setContentsMargins(0, 0, 10, 10)
		# set window size #
		dialog.resize( 400, 100 )

		################################################
		#                   UI CREATION                #
		################################################

		line01Param = dialog.createStringParam("sep01","")
		line01Param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
		
		actionListParam = dialog.createChoiceParam("choice01","Actions : ")
		actionListParam.setAddNewLine(True)
		actionListParam.addOption('disable Preview','')
		actionListParam.addOption('enable Preview','')
		actionListParam.addOption('disable Node','')
		actionListParam.addOption('enable Node','')
		actionListParam.addOption('hide Inputs','')
		actionListParam.addOption('show Inputs','')
		actionListParam.set(0)
		dialog.refreshUserParamsGUI()

		################################################

		# deselect all nodes #
		myAppGui.clearSelection()

		################################################

		# if user press OK #
		dialogResult = dialog.exec_()
		if dialogResult == True :
			# retrieve user choices #
			userChoice = actionListParam.getValue()
			# intValue = dialog.getParam("choice01").get()
			for currentNode in originalNodes :
				currentNode.beginChanges()
				if userChoice == 0 : # disable Preview
					myknob = currentNode.getParam('enablePreview')
					myknob.setValue(False)
					print 'testfalse'
					currentNode.refreshUserParamsGUI()
				if userChoice == 1 : # enable Preview
					myknob = currentNode.getParam('enablePreview')
					myknob.setValue(True)
					print 'testtrue'
					currentNode.refreshUserParamsGUI()
				elif userChoice == 2 : # disable Node
					myknob = currentNode.getParam('disableNode')
					myknob.setValue(True)
				elif userChoice == 3 : # enable Node
					myknob = currentNode.getParam('disableNode')
					myknob.setValue(False)
				elif userChoice == 4 : # enable Node
					myknob = currentNode.getParam('hideInputs')
					myknob.setValue(True)
				elif userChoice == 5 : # enable Node
					myknob = currentNode.getParam('hideInputs')
					myknob.setValue(False)
				currentNode.endChanges()


		# reselect user selected nodes #
		myAppGui.setSelection(originalNodes)

# test only
# batchSelectedNodes()