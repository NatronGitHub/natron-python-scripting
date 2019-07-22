#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 22/07/2019.

import string
import NatronEngine
from NatronGui import *


# TRACKER TO ROTO #

def fullRectangle():

	# get current Natron instance running in memory
	app = natron.getGuiInstance(0)

	# create a 'Roto' node
	myRoto = app.createNode("fr.inria.built-in.Roto")

	# get input image size
	imageWidth = myRoto.getOutputFormat().width()

	imageHeight = myRoto.getOutputFormat().height()


	# set 'Roto' label
	myRoto.setLabel('full_Rectangle')

	# get roto context
	rotoContext = myRoto.getRotoContext()

	# get 'Base Layer'
	Layer1_layer = rotoContext.getBaseLayer()

	# create rectangle
	# 1st parameter : x position
	# 2nd parameter : y position
	# 3rd parameter : size
	# 4th parameter : frame
	fullRectangle = rotoContext.createRectangle(0,0,10,1)
	fullRectangle.setLabel('full_Rectangle')

	# set 1st point position
	fullRectangle.setPointAtIndex(0,1,0,imageHeight,0,imageHeight,0,imageHeight)
	fullRectangle.setFeatherPointAtIndex(0,1,0,imageHeight,0,imageHeight,0,imageHeight)

	# set 2nd point position
	fullRectangle.setPointAtIndex(1,1,imageWidth,imageHeight,imageWidth,imageHeight,imageWidth,imageHeight)
	fullRectangle.setFeatherPointAtIndex(1,1,imageWidth,imageHeight,imageWidth,imageHeight,imageWidth,imageHeight)

	# set 3rd point position
	fullRectangle.setPointAtIndex(2,1,imageWidth,0,imageWidth,0,imageWidth,0)
	fullRectangle.setFeatherPointAtIndex(2,1,imageWidth,0,imageWidth,0,imageWidth,0)

	# set 4th point position
	fullRectangle.setPointAtIndex(3,1,0,0,0,0,0,0)
	fullRectangle.setFeatherPointAtIndex(3,1,0,0,0,0,0,0)

	# set center position
	myRoto.getParam('center').setValue(imageWidth/2,0)
	myRoto.getParam('center').setValue(imageHeight/2,1)