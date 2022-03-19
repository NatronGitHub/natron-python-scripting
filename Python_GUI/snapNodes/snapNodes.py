#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 06/07/2019.

import NatronEngine
from NatronGui import *


# SELECT SIMILAR NODES BY COLOR #
snapx = 100
snapy = 50

def snapNodes():

	# get current Natron instance running in memory #
	myApp = natron.getActiveInstance()
	app = natron.getGuiInstance( myApp.getAppID() )

	# check if at least one node has been selected #
	mysel= app.getSelectedNodes()
	if len(mysel) == 0:
		warning = natron.warningDialog("Snap Nodes","Select at least one node. \n This script snap nodes on the grid  \n ")
	else :
		# get selected nodes #
		for mynode in mysel:
			myPos = mynode.getPosition()	
			mynode.setPosition( round( float(myPos[0]) / float(snapx) )* snapx , round( float(myPos[1]) / float(snapy) )* snapy )


def alignNodes(axis):

	# get current Natron instance running in memory #
	myApp = natron.getActiveInstance()
	app = natron.getGuiInstance( myApp.getAppID() )

	# check if at least one node has been selected #
	mysel= app.getSelectedNodes()
	if len(mysel) == 0:
		warning = natron.warningDialog("Align Nodes","Select at least one node. \n \
			This script aligns the selected nodes horizontally or vertically  \n \
			if nodes get stacked use spreadNodes to separate them  \n")
	else :
		nodeCount=len(mysel)
		myPosSumX= 0
		myPosSumY= 0
		for mynode in mysel:
			myPos = mynode.getPosition()
			myPosSumX += myPos[0]
			myPosSumY += myPos[1]
		myPosAverageX=myPosSumX/nodeCount
		myPosAverageY=myPosSumY/nodeCount
		if axis in ['x','X']:
			for mynode in mysel:
				myPos = mynode.getPosition()
				mynode.setPosition(myPosAverageX,myPos[1])
		if axis in ['y','Y']:
			for mynode in mysel:
				myPos = mynode.getPosition()
				mynode.setPosition(myPos[0],myPosAverageY)

def spreadNodes(axis,snap):

	# get current Natron instance running in memory #
	myApp = natron.getActiveInstance()
	app = natron.getGuiInstance( myApp.getAppID() )

	# check if at least one node has been selected #
	mysel= app.getSelectedNodes()
	if len(mysel) == 0:
		warning = natron.warningDialog("Spread Nodes","Select at least one node. \n \
			This script regularly spaces nodes  between leftmost-rightmost nodes (or lowest-highest)\n \
			snapping to grid is optional\n")
	else :
		if snap in ['snap','SNAP']:
			doSnap=True
		nodeCount=len(mysel)

		# create a list of tuples (index in selection list,position x, position y)
		myList=[]
		counter=0
		for mynode in mysel:
			myPos = mynode.getPosition()
			myList.append( (counter,myPos[0],myPos[1]) )
			counter +=1

		if axis in ['x','X']:
			# sort the list in x position of the nodes
			myList.sort(key=lambda y: y[1])
			# now we know myList[0] is the left node
			myPosMinX= myList[0][1]
			myPosSpacingX=(myList[nodeCount-1][1]-myList[0][1])/nodeCount
			if myPosSpacingX<snapx:
				# prevent nodes to be all stacked
				myPosSpacingX=snapx
			if doSnap:
				myPosSpacingX=round( float(myPosSpacingX)/float(snapx) )*snapx
				myPosMinX= round( float(myPosMinX) / float(snapx) )* snapx

			# finally reposition the nodes
			for counter in range(0,nodeCount):
				mynode=mysel[myList[counter][0]]
				#print 'spreading' + mynode.getLabel()
				myPos = mynode.getPosition()
				mynode.setPosition(myPosMinX + (counter*myPosSpacingX),myPos[1])
		elif axis in ['y','Y']:
			# sort the list in y position of the nodes
			myList.sort(key=lambda y: y[2])
			# now we know myList[0] is the lowest node
			myPosMinY= myList[0][2]
			myPosSpacingY=(myList[nodeCount-1][2]-myList[0][2])/nodeCount
			if myPosSpacingY<snapy:
				# prevent nodes to be all stacked
				myPosSpacingY=snapy
			if doSnap:
				myPosSpacingY=round( float(myPosSpacingY)/float(snapy) )*snapy
				myPosMinY= round( float(myPosMinY) / float(snapy) )* snapy

			# finally reposition the nodes
			for counter in range(0,nodeCount):
				mynode=mysel[myList[counter][0]]
				#print 'spreading' + mynode.getLabel()
				myPos = mynode.getPosition()
				mynode.setPosition(myPos[0], myPosMinY + (counter*myPosSpacingY))
		

def alignNodesX():
	alignNodes('x')
	snapNodes()

def alignNodesY():
	alignNodes('y')
	snapNodes()

def spreadNodesX():
	spreadNodes('x','snap')
	alignNodes('y')
	#snapNodes()

def spreadNodesY():
	spreadNodes('y','snap')
	alignNodes('x')
	#snapNodes()