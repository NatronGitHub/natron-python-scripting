#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 22/07/2019.

import string
import NatronEngine
from NatronGui import *


# CREATE A FULL FRAME SQUARE #

def fullSquare():

	# get current Natron instance running in memory
	app = natron.getGuiInstance(0)

	# create a 'Roto' node
	myRoto = app.createNode("fr.inria.built-in.Roto")

	# get input image size
	imageWidth = myRoto.getOutputFormat().width()

	imageHeight = myRoto.getOutputFormat().height()


	# set 'Roto' label
	myRoto.setLabel('full_Square1')

	# get roto context
	rotoContext = myRoto.getRotoContext()

	# get 'Base Layer'
	Layer1_layer = rotoContext.getBaseLayer()

	# create square
	# 1st parameter : x position
	# 2nd parameter : y position
	# 3rd parameter : size
	# 4th parameter : frame
	fullSquare = rotoContext.createRectangle(0,0,10,1)
	fullSquare.setLabel('full_Square1')

	# set 1st point position
	fullSquare.setPointAtIndex(0,1,(imageWidth/2)-(imageHeight/2),imageHeight,(imageWidth/2)-(imageHeight/2),imageHeight,(imageWidth/2)-(imageHeight/2),imageHeight)
	fullSquare.setFeatherPointAtIndex(0,1,(imageWidth/2)-(imageHeight/2),imageHeight,(imageWidth/2)-(imageHeight/2),imageHeight,(imageWidth/2)-(imageHeight/2),imageHeight)

	# set 2nd point position
	fullSquare.setPointAtIndex(1,1,(imageWidth/2)+(imageHeight/2),imageHeight,(imageWidth/2)+(imageHeight/2),imageHeight,(imageWidth/2)+(imageHeight/2),imageHeight)
	fullSquare.setFeatherPointAtIndex(1,1,(imageWidth/2)+(imageHeight/2),imageHeight,(imageWidth/2)+(imageHeight/2),imageHeight,(imageWidth/2)+(imageHeight/2),imageHeight)

	# set 3rd point position
	fullSquare.setPointAtIndex(2,1,(imageWidth/2)+(imageHeight/2),0,(imageWidth/2)+(imageHeight/2),0,(imageWidth/2)+(imageHeight/2),0)
	fullSquare.setFeatherPointAtIndex(2,1,(imageWidth/2)+(imageHeight/2),0,(imageWidth/2)+(imageHeight/2),0,(imageWidth/2)+(imageHeight/2),0)

	# set 4th point position
	fullSquare.setPointAtIndex(3,1,(imageWidth/2)-(imageHeight/2),0,(imageWidth/2)-(imageHeight/2),0,(imageWidth/2)-(imageHeight/2),0)
	fullSquare.setFeatherPointAtIndex(3,1,(imageWidth/2)-(imageHeight/2),0,(imageWidth/2)-(imageHeight/2),0,(imageWidth/2)-(imageHeight/2),0)

	# set center position
	myRoto.getParam('center').setValue(imageWidth/2,0)
	myRoto.getParam('center').setValue(imageHeight/2,1)