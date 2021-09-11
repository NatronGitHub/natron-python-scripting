import NatronEngine
from NatronGui import *
from PySide.QtGui import *

def listProjectNodes(myAppGui,exclusionList,filterUnderscore):
	# creates node list #
	myAppGui.selectAllNodes()

	for currentNode in exclusionList:
		myAppGui.deselectNode(currentNode)

	selectedNodes = myAppGui.getSelectedNodes()
	tempList = []

	for currentNode in selectedNodes:
		currentID = currentNode.getPluginID()
		if currentID != 'fr.inria.built-in.Viewer':
			currentLabel = currentNode.getLabel()
			if filterUnderscore != True :
				tempList.append(currentLabel)
			elif currentLabel[0]=="_" :
				tempList.append(currentLabel)

		# sort list alphabetically #
	list.sort(tempList)
	return tempList
	# END listProjectNodes

def reconnectNodes():

	# get current Natron instance running in memory #
	# app = natron.getGuiInstance(0)
	# replaced below to get active instead of first instance
	myApp = natron.getActiveInstance()
	myAppGui = natron.getGuiInstance( myApp.getAppID() )

	connectedNodes = 0
	userChoiceString = ""
	firstChoiceString = "Don't connect"
	# get user selected nodes #
	originalNodes = myAppGui.getSelectedNodes()

	# create or retrieve options saved in hidden noop node.
	mySettingsNode = myApp.getNode("ABreconnectNodesSettings_v01")
	if mySettingsNode == None :
		# NoTest
		mySettingsNode = myApp.createNode('net.sf.openfx.NoOpPlugin', -1, myApp, dict([ ("CreateNodeArgsPropNoNodeGUI", NatronEngine.BoolNodeCreationProperty(True)), ("CreateNodeArgsPropNodeInitialName", NatronEngine.StringNodeCreationProperty("ABreconnectNodesSettings_v01")) ]))
		# test only
		# mySettingsNode = myApp.createNode('net.sf.openfx.NoOpPlugin', -1, myApp, dict([ ("CreateNodeArgsPropNoNodeGUI", NatronEngine.BoolNodeCreationProperty(False)), ("CreateNodeArgsPropNodeInitialName", NatronEngine.StringNodeCreationProperty("ABreconnectNodesSettings_v01")) ]))
		mySettingsNode.createPageParam("ABRN","abrn")
		myParam = mySettingsNode.createBooleanParam("filterUnderscore" , "Show only _xxx nodes")
		myParam.set(True)
		myParam = mySettingsNode.createBooleanParam("storeInputName" , "store Input Name")
		myParam.set(True)
		myParam = mySettingsNode.createBooleanParam("hideInput","Hide Input")
		myParam.set(True)
		myParam = mySettingsNode.createStringParam("lastChoice" , "Last Choice")
		myParam.set(firstChoiceString)
		mySettingsNode.refreshUserParamsGUI()
	filterUnderscore = mySettingsNode.getParam("filterUnderscore").get()
	storeInputName = mySettingsNode.getParam("storeInputName").get()
	hideInput = mySettingsNode.getParam("hideInput").get()
	lastChoice = mySettingsNode.getParam("lastChoice").get()
	mySettingsNode.refreshUserParamsGUI()

	# check if at least one node has been selected #
	if len(originalNodes) == 0:
		warning = natron.warningDialog("reconnect Node","Select at least one node. \n This script allows to connect selected nodes with the one selected from a list \n Tip: prefix your favorties with _ underscore \n use N shortcut to rename (bug in GUI breaks renaming in properties)")

	else :
		# create dialog window #
		dialog = myAppGui.createModalDialog()
		# set dialog title #
		dialog.setWindowTitle("Reconnect Nodes")
		# set dialog margins #
		dialog.setContentsMargins(0, 0, 10, 10)
		# set window size #
		dialog.resize( 400, 100 )

		################################################
		#                   UI CREATION                #
		################################################

		line01Param = dialog.createStringParam("sep01","")
		line01Param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
		line02Param = dialog.createStringParam("sep02","")
		line02Param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
		line02Param.set("Your selection will be connected to this node:")

		nodeListParam = dialog.createChoiceParam("choice02","Nodes : ")
		nodeListParam.setAddNewLine(True)
		lastChoiceNumber = 0
		myCount = 0
		nodeListParam.addOption(firstChoiceString,'')
		for item in listProjectNodes(myAppGui,originalNodes,filterUnderscore):
			nodeListParam.addOption(str(item),'')
			myCount +=1
			if str(item) == lastChoice :
				lastChoiceNumber = myCount
		nodeListParam.set(lastChoiceNumber)

		filterUnderscoreParam = dialog.createBooleanParam("choice03","Show only nodes with _ prefix")
		filterUnderscoreParam.set(filterUnderscore)
		storeInputNameParam = dialog.createBooleanParam("choice04","Store input name in userTextArea")
		storeInputNameParam.set(storeInputName)
		hideInputParam = dialog.createBooleanParam("choice05","Hide input")
		hideInputParam.set(hideInput)

		################################################


		# deselect all nodes #
		myAppGui.clearSelection()
		# reselect user selected nodes #
		# app.setSelection(originalNodes)
		# Refresh UI #
		dialog.refreshUserParamsGUI()

		################################################

		# if user press OK #
		dialogResult = dialog.exec_()
		if dialogResult == True :
			# retrieve user choices #
			userIndex = nodeListParam.getValue()
			userChoice = nodeListParam.getOption(userIndex)
			userChoiceString = str ( userChoice )
			lastChoice = userChoiceString
			filterUnderscore = filterUnderscoreParam.get()
			storeInputName = storeInputNameParam.get()
			hideInput = hideInputParam.get()
			
			# find the chosen node
			toNode = None
			myAppGui.selectAllNodes()
			selectedNodes = myAppGui.getSelectedNodes()
			for currentNode in selectedNodes:
				currentLabel = currentNode.getLabel()
				if currentLabel == userChoiceString :
					toNode = currentNode
					break

			# make connections
			if toNode != None :
				for node in originalNodes:
					if node.getMaxInputCount() != 0:
						node.disconnectInput(0)
						if node.canConnectInput(0,toNode):
							node.connectInput(0,toNode)
							connectedNodes += 1
							if storeInputName == True :
								nodeTextParam = node.getParam("userTextArea")
								if nodeTextParam != None :
									nodeTextParam.setValue(userChoiceString)
							if hideInput == True :
								node.getParam("hideInputs").setValue(True)
			# save settings in a hidden node
			mySettingsNode.getParam("filterUnderscore").set(filterUnderscore)
			mySettingsNode.getParam("storeInputName").set(storeInputName)
			mySettingsNode.getParam("hideInput").set(hideInput)
			mySettingsNode.getParam("lastChoice").set( userChoiceString )
			mySettingsNode.refreshUserParamsGUI()

		# reselect user selected nodes #
		myAppGui.setSelection(originalNodes)
		if dialogResult == True and toNode != None :
			endMessage = str( connectedNodes) + " node(s) connected to " + userChoiceString + " node."
			info = natron.informationDialog('autoReconnect',endMessage)	

	# END ABreconnectNodes

# test only
#reconnectNodes()