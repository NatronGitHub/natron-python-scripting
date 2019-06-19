#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 17/01/2018.

from NatronEngine import*
from NatronGui import *
from PySide.QtGui import *


# SETS TIMELINE IN/OUT #

def timelineInOut():

	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# create user input fields #
	firstFrame = dialog.createIntParam("firstFrame","In :")
	defaultFirstFrame = app.getProjectParam('frameRange').get()[0]
	firstFrame.set(defaultFirstFrame)

	lastFrame = dialog.createIntParam("lastFrame","Out :")
	defaultLastFrame = app.getProjectParam('frameRange').get()[1]
	lastFrame.set(defaultLastFrame)
	lastFrame.setAddNewLine(False)

	line01 = dialog.createSeparatorParam("line01","")

	dialog.refreshUserParamsGUI()

	# if user press 'OK' #
	if dialog.exec_():
		# we retrieve the values entered by user #
		newIn = dialog.getParam("firstFrame").getValue()
		newOut = dialog.getParam("lastFrame").getValue()

		# we select all nodes in the Node Graph
		app.selectAllNodes(app)
		currentNode = app.getSelectedNodes()

		# we check every node's 'ID' in the list #
		for node in currentNode:
			currentID = node.getPluginID()

			# if the current node's ID is of 'viewer' type #
			if currentID == 'fr.inria.built-in.Viewer':

				# then we grab its 'label' #
				viewerLabel = node.getLabel()

				# we select it #
				myViewer = app.getViewer(viewerLabel)

				# we set new In/Out values #
				myViewer.setFrameRange(newIn,newOut)
				break