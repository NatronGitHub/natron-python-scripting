#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 26/07/2019.

import os
import string
import NatronEngine
from NatronGui import *


# CREATE A POSTAGE STAMP #

def postageStamp():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# get selected nodes # 
	selectedNodes = app.getSelectedNodes()

	# cycle through every selected node #
	for currentNode in selectedNodes:

		# get current node position #
		currentPosition = currentNode.getPosition()

		# get current node color #
		currentNodeColor = currentNode.getColor()




		# create 'Group' node #
		postageStamp = app.createNode('fr.inria.built-in.Group')

		# set 'Group' position #
		postageStamp.setPosition(currentPosition[0] , currentPosition[1] + 250)

		# set 'Group' label #
		postageStamp.setLabel('PostageStamp')

		# connect 'Group' #
		postageStamp.connectInput(0,currentNode)

		# enable preview #
		postageStamp.getParam('enablePreview').setValue(1)

		# set 'Group' color #
		postageStamp.setColor(currentNodeColor[0] , currentNodeColor[1] , currentNodeColor[2])

		# add 'Controls' page #
		controlsPage = postageStamp.createPageParam("Controls", "Controls")

		line01 = postageStamp.createStringParam("line01","")
		line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
		line02 = postageStamp.createStringParam("line02","")
		line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

		hideCheckbox = postageStamp.createBooleanParam("hideCheckbox", "Hide input : ")
		hideCheckbox.set(1)

		previewCheckbox = postageStamp.createBooleanParam("previewCheckbox", "Enable preview : ")
		previewCheckbox.setAddNewLine(False)
		previewCheckbox.set(1)

		line03 = postageStamp.createStringParam("line03","")
		line03.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
		line04 = postageStamp.createStringParam("line04","")
		line04.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

		pagesOrder = ('Controls','Node')
		postageStamp.setPagesOrder(pagesOrder)

		# hide inputs #
		postageStamp.getParam('hideInputs').setExpression( 'thisNode.hideCheckbox.get()' , False , 0)

		# enable preview
		postageStamp.getParam('enablePreview').setExpression( 'thisNode.previewCheckbox.get()' , False , 0)

		# close pane that pops up at 'Group' creation time #
		currentPane = app.getTabWidget('pane3')
		currentPane.closeCurrentTab()