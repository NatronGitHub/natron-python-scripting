#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 26/06/2019.

#import os
#import string
import os
import string
from NatronEngine import*
from NatronGui import *
from PySide.QtGui import *
import NatronEngine


# TRACKER TO ROTO #

def trackerToRoto():

	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Tracker to roto")

	# set dialog margins #
	dialog.setContentsMargins(0, 0, 10, 10)

	# UI creation #
	line01 = dialog.createStringParam("sep01","")
	line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line02 = dialog.createStringParam("sep02","")
	line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	# pulldown menu creation #
	trackChoice = 	dialog.createChoiceParam("tracksOption", "Tracks : ")
	entries = [ ("All", ""),("Selected", "")]
	trackChoice.setOptions(entries)
	trackChoice.setDefaultValue("All")
	trackChoice.restoreDefaultValue()

	dialog.refreshUserParamsGUI()


	if dialog.exec_():

		currentNode = app.getSelectedNodes()

		# check if more than one node is selected #
		if len(currentNode) <1 :
			warning = natron.warningDialog("Warning","Select a node.")

		else:
			for n in currentNode :
				myID = n.getPluginID()

				# check if the selected node is a Tracker #
				if myID != "fr.inria.built-in.Tracker" :
					warning = natron.warningDialog("Warning","Select a Tracker.")
					break

				else:					
					# get 'Tracker' context, that holds all informations about tracks #
					whichTracks  = n.getTrackerContext()

					# if choice is set to 'Selected', then use selected tracks #
					if trackChoice.get() == 1:
						myTracks = whichTracks.getSelectedTracks()

						# if less than 3 tracks is selected, display warning message #
						if len(myTracks) < 3:
							warning = natron.warningDialog("Warning","Select at least 3 tracks.")
							break

					# if choice is set to 'All', then use all tracks #
					else :
						myTracks = whichTracks.getAllTracks()

						# if less than 3 tracks is selected, display warning message #
						if len(myTracks) < 3:
							warning = natron.warningDialog("Warning","There must be at least 3 tracks.")
					
					numTracks = str(len(myTracks))
					print (numTracks + ' tracks used.' + '\n')

					for currentTrack in myTracks:
						xPos = currentTrack.getParam('centerPoint').getNumKeys(0)
						print (str(xPos) + ' keyframes')


					# ------------------------ #
					#   'ROTO' NODE CREATION   #
					# ------------------------ #

					# get 'Tracker' name #
					myTrackerName = n.getLabel()

					# get 'Tracker' position #
					myTrackerPosition = n.getPosition()

					# create a 'Roto' node #
					myRoto = app.createNode("fr.inria.built-in.Roto")

					# 'Roto' node name #
					myRoto.setLabel(myTrackerName + '_To_Roto1')

					# 'Roto' node position #
					myRoto.setPosition(myTrackerPosition[0] + 200 ,myTrackerPosition[1] )




					# get roto context #
					rotoContext = myRoto.getRotoContext()
					Layer1_layer = rotoContext.getBaseLayer()


					# ---------------------------- #
					#   'BEZIER SPLINE' CREATION   #
					# ---------------------------- #

					# create one point bezier curve at frame 0 #
					newBezier = rotoContext.createBezier(0.0,0.0,1)
					newBezier.setScriptName("Roto_from_track1")
					newBezier.setLabel("Roto_from_track1")
					newBezier.setLocked(False)
					newBezier.setVisible(True)

					# add created bezier to base layer #
					Layer1_layer.addItem(newBezier)

					# creating other points default position (could be anything) #
					# setup point counter #
					pointCounter = 1

					atCreationXPointPosition = 0
					atCreationYPointPosition = 100

					for pointCounter in range(1,int(numTracks)):
						if pointCounter == numTracks:
							newBezier.addControlPoint(atCreationYPointPosition,0)
							
						else:
							newBezier.addControlPoint(atCreationXPointPosition,atCreationYPointPosition)

						atCreationXPointPosition += 100
						atCreationYPointPosition += 100

						pointCounter += 1

					# closing the generated bezier #
					newBezier.setCurveFinished(1)



					# ----------- KEYFRAME GENERATION IF 'LINK' IS UNCHECKED --------- #
					
					pointIndex = 0

					# loop every track #
					for currentTrack in myTracks:

						# -------------------------------------------------------#
						# get the number of keyframes for the X and Y dimensions #
						# -------------------------------------------------------#

						# get centerPoint x keyframes (same as centerPoint y) #
						nXKeys = currentTrack.getParam("centerPoint").getNumKeys(0)
						myTrackName = currentTrack.getScriptName()

						# LOOPING EVERY FOUND KEYFRAME # 

						keyCounter = 0

						print ('point ' +  str(pointIndex) + ' :')
						print '---------------------------------------------------------------'

						while keyCounter < (nXKeys):

							# getKeyTime returns a tuple with a boolean value indicating if it succeeded and the keyframe time #

							# returns x keyframe exact time in timeline #
							gotXKeyTuple = currentTrack.getParam("centerPoint").getKeyTime(keyCounter, 0)
							# 'xFrame' stores keyframe time found in timeline, second term in the tupple #
							xFrame = gotXKeyTuple[1]

							# returns y keyframe exact time in timeline #
							gotYKeyTuple = currentTrack.getParam("centerPoint").getKeyTime(keyCounter, 1)
							# 'yFrame' stores keyframe time found in timeline, second term in the tupple #
							yFrame = gotYKeyTuple[1]

							# get the X keyframe value at 'frame' time #
							xValue = currentTrack.getParam("centerPoint").getValueAtTime(xFrame, 0)
							# get the Y keyframe value at 'frame' time #
							yValue = currentTrack.getParam("centerPoint").getValueAtTime(yFrame, 1)

							# -------------------------------------------------------#
							#    set all bezier curve points position across time    #
							# -------------------------------------------------------#

							# LOOPING EVERY BEZIER POINT #
							pointsNumber = newBezier.getNumControlPoints()
							newBezier.setPointAtIndex(pointIndex, xFrame, xValue, yValue, xValue, yValue, xValue, yValue)
							newBezier.setFeatherPointAtIndex(pointIndex, xFrame, xValue, yValue, xValue, yValue, xValue, yValue)

							print ('x = ' + str(xValue) + '     y = ' + str(yValue) + ' at frame ' + str(int(xFrame)) )
							#print '\n'
							#print ('set point ' +  str(pointIndex) + ' y value at ' + str(yValue) + ' at frame ' + str(int(yFrame)) )

							keyCounter += 1

						print '---------------------------------------------------------------'
						print '\n'
						#print '---------------------------------------------------------------'
						#print '***************************************************************'

						pointIndex += 1