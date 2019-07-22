#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 22/07/2019.

import string
import NatronEngine
from NatronGui import *


# TRACKER TO ROTO #

def fullSquare():

	# get current Natron instance running in memory
	app = natron.getGuiInstance(0)

	# create a 'Roto' node
	myRoto = app.createNode("fr.inria.built-in.Roto")

	# get input image size
	imageWidth = myRoto.getOutputFormat().width()

	imageHeight = myRoto.getOutputFormat().height()


	# set 'Roto' label
	myRoto.setLabel('full_Square')

	# get roto context
	rotoContext = myRoto.getRotoContext()

	# get 'Base Layer'
	Layer1_layer = rotoContext.getBaseLayer()

	# create square
	# 1st parameter : x position
	# 2nd parameter : y position
	# 3rd parameter : size
	# 4th parameter : frame
	fullRectangle = rotoContext.createRectangle(0,0,10,1)
	fullRectangle.setLabel('full_Square')

	# set 1st point position
	fullRectangle.setPointAtIndex(0,1,(imageWidth/2)-(imageHeight/2),imageHeight,(imageWidth/2)-(imageHeight/2),imageHeight,(imageWidth/2)-(imageHeight/2),imageHeight)
	fullRectangle.setFeatherPointAtIndex(0,1,(imageWidth/2)-(imageHeight/2),imageHeight,(imageWidth/2)-(imageHeight/2),imageHeight,(imageWidth/2)-(imageHeight/2),imageHeight)

	# set 2nd point position
	fullRectangle.setPointAtIndex(1,1,(imageWidth/2)+(imageHeight/2),imageHeight,(imageWidth/2)+(imageHeight/2),imageHeight,(imageWidth/2)+(imageHeight/2),imageHeight)
	fullRectangle.setFeatherPointAtIndex(1,1,(imageWidth/2)+(imageHeight/2),imageHeight,(imageWidth/2)+(imageHeight/2),imageHeight,(imageWidth/2)+(imageHeight/2),imageHeight)

	# set 3rd point position
	fullRectangle.setPointAtIndex(2,1,(imageWidth/2)+(imageHeight/2),0,(imageWidth/2)+(imageHeight/2),0,(imageWidth/2)+(imageHeight/2),0)
	fullRectangle.setFeatherPointAtIndex(2,1,(imageWidth/2)+(imageHeight/2),0,(imageWidth/2)+(imageHeight/2),0,(imageWidth/2)+(imageHeight/2),0)

	# set 4th point position
	fullRectangle.setPointAtIndex(3,1,(imageWidth/2)-(imageHeight/2),0,(imageWidth/2)-(imageHeight/2),0,(imageWidth/2)-(imageHeight/2),0)
	fullRectangle.setFeatherPointAtIndex(3,1,(imageWidth/2)-(imageHeight/2),0,(imageWidth/2)-(imageHeight/2),0,(imageWidth/2)-(imageHeight/2),0)