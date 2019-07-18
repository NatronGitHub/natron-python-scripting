#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 17/01/2018.

import string
from NatronEngine import*
from NatronGui import *


# ROTO TO TRACKER #

def rotoToTracker():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# we store selected node(s) in a list #
	selectedNodes = app.getSelectedNodes()

	# check if at least one node has been selected #
	if len(selectedNodes) == 0 :
		warning = natron.warningDialog("Warning","Select at least one node.")

	else:
		# cycle every selected node #
		for node in selectedNodes :

			# get node type #
			nodeID = node.getPluginID()

			# get node label #
			nodeLabel = node.getLabel()

			# get node position in the Node Graph for later use #
			nodePosition = node.getPosition()

			# initialize a counter #
			nodeCounter = 1

			# check if selected node(s) are of 'Roto' class #
			if nodeID == "fr.inria.built-in.RotoPaint" or nodeID == "fr.inria.built-in.Roto" :

				# grab 'Roto context' #
				rotoContext = node.getRotoContext()

				# get 'Base layer' in 'Roto context'  #
				baseLayer = rotoContext.getBaseLayer()

				# get all items in 'Base layer'
				allBaseLayerItems = baseLayer.getChildren()

				# we initialize an offset value for new created 'Tracker' position in the Node Graph #
				newNodeYPosOffset = 0

				# cycle every item in 'Base layer' #
				for item in allBaseLayerItems:

					# get current item 'Label' #
					itemName = item.getLabel()

					# retrieve current 'Item' using its name #
					currentBezier = rotoContext.getItemByName(itemName)

					# check if 'Item' is of 'BezierCurve' class #
					currentClass = type(currentBezier)
					

					if 'BezierCurve' in str(currentClass):

						pointNumber = currentBezier.getNumControlPoints()


						# -----------------------------------------------------------#
						#                  CREATE 'TRACKER' NODE                     #
						# -----------------------------------------------------------#

						# create a 'Tracker' node #
						newTracker = app.createNode("fr.inria.built-in.Tracker")

						# set 'Tracker' label #
						newTracker.setLabel(str(itemName) + '_Tracker')

						# set node position in Node Graph #
						
						newTracker.setPosition( nodePosition[0] + 120 ,nodePosition[1] + newNodeYPosOffset )

						# set 'Motion type' to 'Match-Move' #
						newTracker.getParam('motionType').set('Match-Move')

						# recursive creation of tracks #
						trackNumber = 0

						while trackNumber < pointNumber:

							# get 'Tracker context' #
							newTrackerContext = newTracker.getTrackerContext()

							# create new 'Track' #
							newTrack = newTrackerContext.createTrack()

							# get current 'Track' label #
							trackName = newTrack.getScriptName()

							# retrieve current 'Track' #
							currentTrack = newTrackerContext.getTrackByName(trackName)

							currentTrack.getParam('motionModel').set('Trans.+Rot.+Scale')
							
							# get 'currentBezier' all keyframes #
							currentBezierKeyframes = currentBezier.getKeyframes()

							# get number of 'currentBezier' keyframes #
							keyframesNumber = len(currentBezierKeyframes)

							# cycle every 'currentBezier' keyframes #
							for currentTime in currentBezierKeyframes:

								# get current point position at current keyframe #
								currentPointPosition = currentBezier.getControlPointPosition(trackNumber,currentTime)
								pointXPos = currentPointPosition[0]
								pointYPos = currentPointPosition[1]

								# get the 'Track'center point parameter #
								trackPosition = currentTrack.getParam('centerPoint')

								# set the 'Track' position to current point position #
								trackPosition.set(pointXPos,pointYPos,currentTime)
								
							# go to next 'Track' #
							trackNumber += 1

					newNodeYPosOffset += 100

				# go to next node #
				nodeCounter += 1

			else:
				warning = natron.warningDialog("Warning","Select Roto node(s).")

		# deselect all nodes #
		app.clearSelection()