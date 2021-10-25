# This Source Code Form is subject to the terms of the GNU General Public License version 2
# Created by Alexandre Bon on 2019
# Modified by Alexandre Bon on 2021/09/03: reliable appGui retrievement / reduce spacing / add postage stamps
# The script reconnects node "foo" to the node "_bar" when the Label (or userTextArea) of "foo" is the text string "_bar"
# This is useful for 3D compositing to copy paste parts of the node tree while keeping connections with the various 3D passes

import NatronEngine
from NatronGui import *
from PySide.QtGui import *


def autoReconnect():
	# print ( "start")
	NoGUIApp = natron.getActiveInstance()
	NoGUIAppID = natron.getActiveInstance().getAppID()
	app = natron.getGuiInstance(NoGUIAppID)
	allLabelsWereFound = True
	allLabelsWereUnderscored = True
	reconnectedNodes = 0
	# get user selected nodes #
	selectedNodes = app.getSelectedNodes()

	# check if at least one node has been selected #
	if len(selectedNodes) == 0:
		warning = natron.warningDialog("autoReconnect","Select at least one node. \n \n autoReconnect: \n This script will connect the nodes whit Label _foo to the node with that name.\n Only names starting with _ are reconnected.\n Label is userTextArea in node tab ")

	else :
		# process #
		app.selectAllNodes()
		allNodes = app.getSelectedNodes()
		# mycount = 0
		for currentNode in selectedNodes:
			myTextArea = currentNode.getParam("userTextArea")
			# test only
			# print ( "mta:" )
			# print ( myTextArea.getValue() )

			if myTextArea == None :
				mytext = None
			else :
				mytext = myTextArea.getValue()
				if mytext !="" :
					# sometimes the textarea starts with < html codes sometimes not. It's a refresh issue that we have to deal with
					if mytext[0] == "<":
						ms1 = myTextArea.getValue().split(">")
						ms2 = ms1[1].split("<")
						mysplit = ms2[0]
						mytext = mysplit

			if mytext !="" and mytext != None :
				if mytext[0]== "_" and currentNode.getInput(0) == None :	# test if currentNode should be reconnected
					# test only
					# print( "search:" mytext )
					thisLabelWasFound = False
					for testNode in allNodes :
						if testNode.getLabel() == mytext :
							thisLabelWasFound = True
							if currentNode.canConnectInput(0,testNode):
								currentNode.connectInput(0,testNode)
								reconnectedNodes +=1
								break
					if thisLabelWasFound == False :
						allLabelsWereFound = False
				elif mytext[0]!= "_" and currentNode.getInput(0) == None :
					allLabelsWereUnderscored = False
		endMessage = str( reconnectedNodes) + " node(s) reconnected."
		if allLabelsWereFound == False :
			endMessage +='\n \n Some labels were not found. Please rename parents with N shortcut (bug in GUI breaks renaming in properties)'
		if allLabelsWereUnderscored == False :
			endMessage +='\n \n Only Labels starting with _ are reconnected'
		
		# reselect user selected nodes #
		# deselect all nodes #
		app.clearSelection()
		app.setSelection(selectedNodes)
		info = natron.informationDialog('autoReconnect',endMessage)

# test only
#autoReconnect()