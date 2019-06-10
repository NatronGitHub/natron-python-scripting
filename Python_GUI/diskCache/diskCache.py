#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 17/01/2018.

from NatronEngine import*
from NatronGui import *
from PySide.QtGui import *
import NatronEngine


# DISK CACHE THE SELECTED NODE #

def diskCache():

	# creates dialog window #
	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# creates UI #

	line01 = dialog.createStringParam("sep01","")
	line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line02 = dialog.createStringParam("sep02","")
	line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	sep01 = dialog.createSeparatorParam("line03","Disk Cache")

	line03 = dialog.createStringParam("sep03","")
	line03.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line04 = dialog.createStringParam("sep04","")
	line04.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	

	firstFrame = dialog.createIntParam("firstFrame","In :")
	lastFrame = dialog.createIntParam("lastFrame","Out :")
	lastFrame.setAddNewLine(False)

	line05 = dialog.createStringParam("sep05","")
	line05.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	sep02 = dialog.createSeparatorParam("line02","")

	# Refresh UI #
	dialog.refreshUserParamsGUI()

	# code executed when OK button is pressed #
	if dialog.exec_():

		# retrieves values entered by user #
		newFirstFrame = dialog.getParam("firstFrame").getValue()
		newLastFrame = dialog.getParam("lastFrame").getValue()

		counter = 0
		selectedNodes = app.getSelectedNodes()



		for n in selectedNodes:

			# if more than 1 node have been selected, stop the process #
			if len(selectedNodes) != 1 :
				break

			else :
				# creates a DiskCache node #
				parentPosition = n.getPosition()
				diskCache = app.createNode("fr.inria.built-in.DiskCache")

				# connects the Disk Cache node to the selected node, and set graph position. #
				diskCache.connectInput(0, n)
				diskCache.setPosition(parentPosition[0]+150,parentPosition[1]+75)

				# set node color #
				diskCache.setColor(0.521,0.51492,0.0003)

				# set node name #
				parentLabel = n.getLabel()
				diskCache.setLabel('DiskCache_' + str(parentLabel))

				myFrameRange = diskCache.getParam("frameRange")
				myFrameRange.set(2)

				myFirstFrame = diskCache.getParam("firstFrame")
				myFirstFrame.set(newFirstFrame)

				myLastFrame = diskCache.getParam("LastFrame")
				myLastFrame.set(newLastFrame)

				app.render(diskCache, newFirstFrame, newLastFrame)