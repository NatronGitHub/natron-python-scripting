#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 22/07/2019.

import string
import NatronEngine
from NatronGui import *


# CREATE A FULL FRAME ELLIPSE #

def fullEllipse():

	# get current Natron instance running in memory
	app = natron.getGuiInstance(0)

	# create a 'Roto' node
	myRoto = app.createNode("fr.inria.built-in.Roto")

	# get input image size
	imageWidth = myRoto.getOutputFormat().width()

	imageHeight = myRoto.getOutputFormat().height()

	# set 'Roto' label
	myRoto.setLabel('full_Ellipse')

	# get roto context
	rotoContext = myRoto.getRotoContext()

	# get 'Base Layer'
	Layer1_layer = rotoContext.getBaseLayer()



	# create ellipse
	fullEllipse = rotoContext.createEllipse(imageWidth/2, imageHeight/2, imageWidth, True, 1)
	fullEllipse.setLabel('full_Ellipse')

	# set center position
	myRoto.getParam('center').setValue(imageWidth/2,0)
	myRoto.getParam('center').setValue(imageHeight/2,1)



	# get bottom point position
	bottomPointPosition = fullEllipse.getControlPointPosition(0,1)

	# set bottom point position
	fullEllipse.setPointAtIndex(0, 1, bottomPointPosition[0], 0, bottomPointPosition[2], 0, bottomPointPosition[4], 0)
	fullEllipse.setFeatherPointAtIndex(0, 1, bottomPointPosition[0], 0, bottomPointPosition[2], 0, bottomPointPosition[4], 0)

	# get top point position
	topPointPosition = fullEllipse.getControlPointPosition(2,1)

	# set top point position
	fullEllipse.setPointAtIndex(2, 1, topPointPosition[0], imageHeight, topPointPosition[2], imageHeight, topPointPosition[4], imageHeight)
	fullEllipse.setFeatherPointAtIndex(2, 1, topPointPosition[0], imageHeight, topPointPosition[2], imageHeight, topPointPosition[4], imageHeight)

	bbox = myRoto.getRegionOfDefinition(1,0)
	myWidth = bbox.width() -3
	myHeight = bbox.height() -3

	imageRatio = myHeight/myWidth

	# get right point position
	rightPointPosition = fullEllipse.getControlPointPosition(1,1)

	rightPointLeftTangentPosition = rightPointPosition[1] - rightPointPosition[3]
	rightPointLeftTangentPosition *= imageRatio


	rightPointRightTangentPosition = rightPointPosition[1] - rightPointPosition[5]
	rightPointRightTangentPosition *= imageRatio
	rightPointRightTangentPosition += myHeight


	fullEllipse.setPointAtIndex(1, 1, rightPointPosition[0], rightPointPosition[1], rightPointPosition[2], rightPointLeftTangentPosition, rightPointPosition[4], rightPointRightTangentPosition)
	fullEllipse.setFeatherPointAtIndex(1, 1, rightPointPosition[0], rightPointPosition[1], rightPointPosition[2], rightPointLeftTangentPosition, rightPointPosition[4], rightPointRightTangentPosition)


	# get left point position
	leftPointPosition = fullEllipse.getControlPointPosition(3,1)

	leftPointRightTangentPosition = leftPointPosition[1] - leftPointPosition[3]
	leftPointRightTangentPosition *= imageRatio
	leftPointRightTangentPosition += (myHeight/2)


	leftPointLeftTangentPosition = leftPointPosition[1] - leftPointPosition[5]
	leftPointLeftTangentPosition *= imageRatio
	leftPointLeftTangentPosition += (myHeight/2)


	fullEllipse.setPointAtIndex(3, 1, leftPointPosition[0], leftPointPosition[1], leftPointPosition[2], leftPointLeftTangentPosition, leftPointPosition[4], leftPointRightTangentPosition)
	fullEllipse.setFeatherPointAtIndex(3, 1, leftPointPosition[0], leftPointPosition[1], leftPointPosition[2], leftPointLeftTangentPosition, leftPointPosition[4], leftPointRightTangentPosition)