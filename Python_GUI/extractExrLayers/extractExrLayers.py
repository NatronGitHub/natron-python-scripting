#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 25/01/2018.

import os
import string
import NatronEngine
from NatronGui import *


# EXTRACT EXR LAYERS #

def extractExrLayers():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# get selected nodes # 
	selectedNodes = app.getSelectedNodes()

	# cycle through every selected node #
	for currentNode in selectedNodes:

		# get node ID #
		currentID = currentNode.getPluginID()

		# check if selected node is a 'Read' node #
		if currentID == 'fr.inria.built-in.Read':

			# get 'Read' node position #
			readPosition = currentNode.getPosition()




			###################
			# CREATE ROOT DOT #
			###################

			# create root dot #
			rootDot = app.createNode('fr.inria.built-in.Dot')

			# set root dot position #
			rootDot.setPosition(readPosition[0] + 45 , readPosition[1] + 300)

			# connect root dot to 'Read' #
			rootDot.connectInput(0,currentNode)

			# get root dot position #
			rootDotPosition = rootDot.getPosition()





			# get all available layers in EXR #
			layersList = currentNode.getParam('outputLayer').getOptions()

			# sort list alphabetically #
			list.sort(layersList)

			backdropLength = len(layersList)

			# initialize counter #
			channelCounter = 0

			# cycle through every layer #
			for choice in layersList:

				if choice != 'Color.RGBA':

					# full layer name #
					fullLayerName = choice

					# layer name #
					layerName = os.path.splitext(choice)[0]

					print layerName

					# layer channels (RGBA,RGB,XYZ,UV,A,Z) #
					layerChannels = os.path.splitext(choice)[1]

					# remove '.' from channels #
					layerChannels = layerChannels.replace('.','')




					# create the first 'Shuffle' node #
					if channelCounter == 0 :

						###################
						# CREATE SHUFFLE  #
						###################

						# create a 'Shuffle' node #
						newShuffle = app.createNode('net.sf.openfx.ShufflePlugin')

						# set 'Shuffle' label #
						newShuffle.setLabel(str(layerName))

						# enable preview #
						newShuffle.getParam('enablePreview').setValue(1)
						newShuffle.getParam('enablePreview').setValue(0)
						newShuffle.getParam('enablePreview').setValue(1)

						# set 'Shuffle' node position #
						newShuffle.setPosition(rootDotPosition[0] - 45 , rootDotPosition[1] + 200)

						# set 'Shuffle' color #
						newShuffle.setColor(1, 0.5, 0.15)

						# connect 'Shuffle' to root dot #
						newShuffle.connectInput(0,rootDot)

						# create a 'Backdrop' #
						newBackdrop = app.createNode('fr.inria.built-in.BackDrop')
						newBackdrop.setPosition(rootDotPosition[0] - 200 , rootDotPosition[1] - 120)
						newBackdrop.setSize( (backdropLength -1 )*400, 500 )
						newBackdrop.setColor(0.5, 0.35, 0.12)


					# create all the other 'Shuffle' nodes #
					if channelCounter != 0 :

						# create a new dot #
						newDot = app.createNode('fr.inria.built-in.Dot')

						# set root dot position #
						newDot.setPosition(rootDotPosition[0] + 400 , rootDotPosition[1])

						# connect root dot to previous dot #
						newDot.connectInput(0,rootDot)

						# replace old Dot position value
						rootDotPosition = newDot.getPosition()


						###################
						# CREATE SHUFFLE  #
						###################


						# create a 'Shuffle' node #
						newShuffle = app.createNode('net.sf.openfx.ShufflePlugin')

						# set 'Shuffle' label #
						newShuffle.setLabel(str(layerName))

						# enable preview #
						newShuffle.getParam('enablePreview').setValue(1)
						newShuffle.getParam('enablePreview').setValue(0)
						newShuffle.getParam('enablePreview').setValue(1)

						# set 'Shuffle' node position #
						newShuffle.setPosition(rootDotPosition[0] - 45 , rootDotPosition[1] + 200)

						# set 'Shuffle' color #
						newShuffle.setColor(1, 0.5, 0.15)

						# connect 'Shuffle' to root dot #
						newShuffle.connectInput(0,newDot)




					##########################
					# SET SHUFFLE PARAMETERS #
					##########################

					# if layer has 4 channels #
					if len(layerChannels) == 4 :

						newShuffleValue = 'B.' + str(layerName) + '.' + str(layerChannels[0:1])
						newShuffle.getParam('outputR').set(newShuffleValue)


					# if layer has 3 channels #
					if len(layerChannels) == 3 :


						newShuffleValue = 'B.' + str(layerName) + '.' + str(layerChannels[0:1])
						newShuffle.getParam('outputR').set(newShuffleValue)
						newShuffle.getParam('outputA').setValue(4)


					# if layer has 2 channels #
					if len(layerChannels) == 2 :

						newShuffleValue = 'B.' + str(layerName) + '.' + str(layerChannels[0:1])
						newShuffle.getParam('outputR').set(newShuffleValue)
						newShuffle.getParam('outputB').setValue(4)
						newShuffle.getParam('outputA').setValue(4)

					# if layer has 1 channel #
					if len(layerChannels) == 1 :

						newShuffleValue = 'B.' + str(layerName) + '.' + str(layerChannels[0:1])
						newShuffle.getParam('outputR').set(newShuffleValue)
						newShuffle.getParam('outputG').setValue(4)
						newShuffle.getParam('outputB').setValue(4)
						newShuffle.getParam('outputA').setValue(4)

					# if layer has 0 channel #
					if len(layerChannels) == 0 :

						newShuffleValue = 'B.' + str(choice)
						newShuffle.getParam('outputR').set(newShuffleValue)
						newShuffle.getParam('outputG').setValue(4)
						newShuffle.getParam('outputB').setValue(4)
						newShuffle.getParam('outputA').setValue(4)


					# increase counter #
					channelCounter += 1