import NatronEngine
from NatronGui import *
from PySide.QtGui import *


def reconnectNodes():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# get user selected nodes #
	selectedNodes = app.getSelectedNodes()

	# check if at least one node has been selected #
	if len(selectedNodes) == 0:
		warning = natron.warningDialog("Warning","Select at least one node.")

	else :
		# create dialog window #
		dialog = app.createModalDialog()

		# set dialog title #
		dialog.setWindowTitle("Nodes list")

		# set dialog margins #
		dialog.setContentsMargins(0, 0, 10, 10)

		# set window size #
		dialog.resize( 400, 100 )

		################################################
		#                   UI CREATION                #
		################################################

		line01 = dialog.createStringParam("sep01","")
		line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
		line02 = dialog.createStringParam("sep02","")
		line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

		# creates node list #
		nodeList = dialog.createChoiceParam("choice02","Nodes : ")
		nodeList.setAddNewLine(False)

		################################################

		originalNodes = app.getSelectedNodes()

		app.selectAllNodes()

		for currentNode in originalNodes:
			app.deselectNode(currentNode)

		selectedNodes = app.getSelectedNodes()

		for currentNode in selectedNodes:
			currentID = currentNode.getPluginID()

			if currentID != 'fr.inria.built-in.Viewer':

				currentLabel = currentNode.getScriptName()
				nodeList.addOption(str(currentLabel),'')


		# deselect all nodes #
		app.clearSelection()

		# reselect user selected nodes #
		app.setSelection(originalNodes)

		# Refresh UI #
		dialog.refreshUserParamsGUI()

		################################################

		# if user press OK #
		if dialog.exec_():

			# retrieve user choice #
			userIndex = nodeList.getValue()
			userChoice = nodeList.getOption(userIndex)

			app.selectAllNodes()
			selectedNodes = app.getSelectedNodes()

			for currentNode in selectedNodes:
				currentLabel = currentNode.getScriptName()

				if currentLabel == str(userChoice):
					toNode = currentNode

			for node in originalNodes:

				if node.getMaxInputCount() != 0:

					node.disconnectInput(0)
					node.connectInput(0,toNode)


		# reselect user selected nodes #
		app.setSelection(originalNodes)