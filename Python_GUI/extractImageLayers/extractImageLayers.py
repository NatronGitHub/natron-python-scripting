#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
# Derived from Fabrice Fernandez extractEXRLayers. Implemented by CGVIRUS

import os
import string
import NatronEngine
from NatronGui import *


# EXTRACT IMAGE LAYERS #

def extractImageLayers():

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

			rootShuffle = app.createNode('net.sf.openfx.ShufflePlugin')
			rootShuffle.setLabel('tempshuffle')
			rootShuffle.connectInput(0, currentNode)


			# get all available layers in Image #
			layersList = rootShuffle.getParam('outputLayer').getOptions()

			# sort list alphabetically #
			list.sort(layersList)

			#Hard coded. May be there is a better way?
			abandonlist = ['uk.co.thefoundry.OfxImagePlaneColour',
			'uk.co.thefoundry.OfxImagePlaneStereoDisparityLeft',
			'uk.co.thefoundry.OfxImagePlaneStereoDisparityRight',
			'uk.co.thefoundry.OfxImagePlaneBackMotionVector',
			'uk.co.thefoundry.OfxImagePlaneForwardMotionVector',
			'Deep','Depth','Mask','Motion']

			backdropLength = len(layersList)-len(abandonlist)

			# initialize counter #
			channelCounter = 0

			# cycle through every layer #
			for choice in layersList:

				if choice not in abandonlist:

					# full layer name #
					LayerName = choice

					# layer name #
					layerName = choice

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

						# set 'Shuffle' node position #
						newShuffle.setPosition(rootDotPosition[0] - 45 , rootDotPosition[1] + 200)

						# set 'Shuffle' color #
						newShuffle.setColor(1, 0.5, 0.15)

						# connect 'Shuffle' to root dot #
						newShuffle.connectInput(0,rootDot)

						# create a 'Backdrop' #
						newBackdrop = app.createNode('fr.inria.built-in.BackDrop')
						newBackdrop.setPosition(rootDotPosition[0] - 200 , rootDotPosition[1] - 120)
						newBackdrop.setSize( (backdropLength )*400, 500 )
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

						# set 'Shuffle' node position #
						newShuffle.setPosition(rootDotPosition[0] - 45 , rootDotPosition[1] + 200)

						# set 'Shuffle' color #
						newShuffle.setColor(1, 0.5, 0.15)

						# connect 'Shuffle' to root dot #
						newShuffle.connectInput(0,newDot)




					##########################
					# SET SHUFFLE PARAMETERS #
					##########################

					newShuffleValue = 'B.' + str(layerName) + '.' + 'R'
					newShuffle.getParam('outputR').set(newShuffleValue)


					# increase counter #
					channelCounter += 1
