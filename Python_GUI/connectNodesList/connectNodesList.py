import NatronEngine
from NatronGui import *
from PySide.QtGui import *


def connectNodesList():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# DIALOG WINDOW CREATION #
	# create dialog window #
	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Nodes list")

	# set dialog margins #
	dialog.setContentsMargins(0, 0, 10, 10)

	# set window size #
	dialog.resize( 400, 100 )


	# UI CREATION #
	line01 = dialog.createStringParam("sep01","")
	line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line02 = dialog.createStringParam("sep02","")
	line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	# creates node list #
	nodeList = dialog.createChoiceParam("choice02","Connect to : ")
	nodeList.setAddNewLine(False)

	# get user selected nodes #
	originalNodes = app.getSelectedNodes()

	# select all nodes #
	app.selectAllNodes()

	# remove user selected nodes from selection #
	for node in originalNodes:
		app.deselectNode(node)

	# get selected nodes #
	selectedNodes = app.getSelectedNodes()

	# add selected nodes to choice list #
	for currentNode in selectedNodes:

		nodeID = currentNode.getPluginID()

		if nodeID != 'fr.inria.built-in.Viewer':
			currentLabel = currentNode.getLabel()
			nodeList.addOption(str(currentLabel),'')


	# deselect all nodes #
	app.clearSelection()

	# regrab originally selected nodes #
	app.setSelection(originalNodes)

	# Refresh UI #
	dialog.refreshUserParamsGUI()


	# press OK button #
	if dialog.exec_():

		# get user choice #
		choosenNodeIndex = nodeList.getValue()
		choosenNodeName = nodeList.getOption(choosenNodeIndex)

		# select user choosen node in Node Graph #
		app.selectAllNodes()
		allNodes = app.getSelectedNodes()

		for node in allNodes:
			nodeLabel = node.getLabel()

			if nodeLabel == str(choosenNodeName):
				toNode = node

		for nodeToConnect in originalNodes:

			if nodeToConnect.canConnectInput(0,toNode) == 1:
				nodeToConnect.connectInput(0,toNode)

		app.setSelection(originalNodes)