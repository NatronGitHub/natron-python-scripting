#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 26/07/2019.
#Modified by alexandre bon on 2021/09/02: reliable appGui retrievement / reduce spacing / add postage stamps
# TODO remove unused channels (with a merge node)

import os
import string
import NatronEngine
from NatronGui import *
from Python_GUI.postageStamp.postageStamp import * # from the community scripts



# EXTRACT EXR LAYERS #

def extractExrLayers():
	layer_spacing = 20
	nodes_spacing_y = 10
	mergeOffsetY = 50
	constantOffsetX = 100

	# get current Natron instance running in memory #
	# app = natron.getGuiInstance(0)	# more reliable method below
	#myNoGUIApp = natron.getActiveInstance()
	#myNoGUIAppID = natron.getActiveInstance().getAppID()
	#myAppGui = natron.getGuiInstance(myNoGUIAppID)
	#app = myAppGui

	myApp = natron.getActiveInstance()
	app = natron.getGuiInstance( myApp.getAppID() )

	# get selected nodes # 
	selectedNodes = app.getSelectedNodes()

	# check if at least one node has been selected #
	if len(selectedNodes) == 0:
		warning = natron.warningDialog("Extract EXR","Select at least one node. \n This script extract multilayer EXR files  \n ")
	else :
		# create dialog window #
		dialog = app.createModalDialog()
		# set dialog title #
		dialog.setWindowTitle("ExtractEXR")
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
		line02Param.set("Your reader will be expanded into each of its layers:")
		prefixUnderscoreParam = dialog.createBooleanParam("choice03","add _ prefix to output nodes")
		prefixUnderscoreParam.set(True)
		removeChannelsParam = dialog.createBooleanParam("choice04","Keep only RGBA for each layer")
		removeChannelsParam.set(True)
		sizeMultParam = dialog.createIntParam("int01","Size Multiplyer")
		sizeMultParam.set(10)
		# Refresh UI #
		dialog.refreshUserParamsGUI()

		################################################
		#                   SHOW UI                    #
		################################################

		# if user press OK #
		dialogResult = dialog.exec_()
		if dialogResult == True :
			# retrieve user choices #
			prefixUnderscore = prefixUnderscoreParam.get()
			removeChannels = removeChannelsParam.get()
			sizeMult = sizeMultParam.get()
			sizeMult = min (40, max(4 , sizeMult))
			layer_spacing *= sizeMult
			nodes_spacing_y *= sizeMult

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

							print (layerName)

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
								# set 'Shuffle' node position #
								newShuffle.setPosition(rootDotPosition[0] - 45 , rootDotPosition[1] + nodes_spacing_y )
								# connect 'Shuffle' to root dot #
								newShuffle.connectInput(0,rootDot)

								# create constant to use for the remove layers operation
								if removeChannels:
									sizeRefName = newShuffle.getScriptName()
									myConstant = app.createNode('net.sf.openfx.ConstantPlugin')
									myConstant.setPosition(rootDotPosition[0] - 200 , rootDotPosition[1])
									myConstant.getParam('extent').set('size')
									bottomLeftParam = myConstant.getParam('bottomLeft')
									sizeParam = myConstant.getParam('size')
									storeExpression =sizeRefName+".getOutputFormat().bottom()"
									bottomLeftParam.setExpression(storeExpression,False, dimension=0 )
									storeExpression =sizeRefName+".getOutputFormat().left()"
									bottomLeftParam.setExpression(storeExpression,False, dimension=1 )
									storeExpression=sizeRefName+".getOutputFormat().width()"
									sizeParam.setExpression(storeExpression,False, dimension=0)
									storeExpression=sizeRefName+".getOutputFormat().height()"
									sizeParam.setExpression(storeExpression,False, dimension=1 )

									# create merge for remove operation
									myMerge = app.createNode('net.sf.openfx.MergePlugin')
									myMerge.connectInput(1,newShuffle)
									myMerge.connectInput(0,myConstant)
									myMerge.setPosition(newShuffle.getPosition()[0] , newShuffle.getPosition()[1]+mergeOffsetY)

								# create a 'Backdrop' #
								newBackdrop = app.createNode('fr.inria.built-in.BackDrop')
								newBackdrop.setPosition(rootDotPosition[0] - layer_spacing - constantOffsetX , rootDotPosition[1] - 60)
								newBackdrop.setSize( (backdropLength +1 )*layer_spacing + constantOffsetX , nodes_spacing_y*4 + 20)
								newBackdrop.setColor(0.5, 0.35, 0.12)


							# create all the other 'Shuffle' nodes #
							if channelCounter != 0 :

								# create a new dot #
								newDot = app.createNode('fr.inria.built-in.Dot')

								# set root dot position #
								newDot.setPosition(rootDotPosition[0] + layer_spacing , rootDotPosition[1])

								# connect root dot to previous dot #
								newDot.connectInput(0,rootDot)

								# replace old Dot position value
								rootDotPosition = newDot.getPosition()


								###################
								# CREATE SHUFFLE  #
								###################

								# create a 'Shuffle' node #
								newShuffle = app.createNode('net.sf.openfx.ShufflePlugin')

								# set 'Shuffle' node position #
								newShuffle.setPosition(rootDotPosition[0] - 45 , rootDotPosition[1] + nodes_spacing_y )

								# connect 'Shuffle' to root dot #
								newShuffle.connectInput(0,newDot)
								
								if removeChannels:
									# create merge for remove operation
									myMerge = app.createNode('net.sf.openfx.MergePlugin')
									myMerge.connectInput(1,newShuffle)
									myMerge.connectInput(0,myConstant)
									myMerge.setPosition(newShuffle.getPosition()[0] , newShuffle.getPosition()[1]+mergeOffsetY)
							# ADD POSTAGE STAMP
							stamp_spacing_y = 100
							hideInput = False
							preview = True
							if prefixUnderscore :
								nodeLabel = '_'+ layerName
							else :
								nodeLabel = layerName
							if removeChannels:
								app.selectNode(myMerge,True)
							else:	
								app.selectNode(newShuffle, True)
							postageStamp(stamp_spacing_y , hideInput , preview , nodeLabel)


							##########################
							# SET SHUFFLE PARAMETERS #
							##########################
							
							# set 'Shuffle' label #
							newShuffle.setLabel(str(layerName))

							# enable preview (deprecated with postage stamp addition)#
							#newShuffle.getParam('enablePreview').setValue(1)
							#newShuffle.getParam('enablePreview').setValue(0)
							#newShuffle.getParam('enablePreview').setValue(1)

							# set 'Shuffle' color #
							newShuffle.setColor(1, 0.5, 0.15)

							# modified by AB to correctly handle non RGB channels

							# if layer has 4 channels #
							if len(layerChannels) == 4 :
								newShuffleValue = 'B.' + str(layerName) + '.' + str(layerChannels[0:1])
								newShuffle.getParam('outputR').set(newShuffleValue)
								newShuffleValue = 'B.' + str(layerName) + '.' + str(layerChannels[1:2])
								newShuffle.getParam('outputG').set(newShuffleValue)
								newShuffleValue = 'B.' + str(layerName) + '.' + str(layerChannels[2:3])
								newShuffle.getParam('outputB').set(newShuffleValue)
								newShuffleValue = 'B.' + str(layerName) + '.' + str(layerChannels[3:4])
								newShuffle.getParam('outputA').set(newShuffleValue)


							# if layer has 3 channels #
							if len(layerChannels) == 3 :
								newShuffleValue = 'B.' + str(layerName) + '.' + str(layerChannels[0:1])
								newShuffle.getParam('outputR').set(newShuffleValue)
								newShuffleValue = 'B.' + str(layerName) + '.' + str(layerChannels[1:2])
								newShuffle.getParam('outputG').set(newShuffleValue)
								newShuffleValue = 'B.' + str(layerName) + '.' + str(layerChannels[2:3])
								newShuffle.getParam('outputB').set(newShuffleValue)
								newShuffle.getParam('outputA').setValue(4)


							# if layer has 2 channels #
							if len(layerChannels) == 2 :
								newShuffleValue = 'B.' + str(layerName) + '.' + str(layerChannels[0:1])
								newShuffle.getParam('outputR').set(newShuffleValue)
								newShuffleValue = 'B.' + str(layerName) + '.' + str(layerChannels[1:2])
								newShuffle.getParam('outputG').set(newShuffleValue)
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
			app.setSelection(selectedNodes)

# launch inside Natron Script Editor
# extractExrLayers()