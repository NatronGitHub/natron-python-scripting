#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 22/07/2019.

import string
import NatronEngine
from NatronGui import *


# CREATE A FULL FRAME CIRCLE #

def fullCircle():

	# get current Natron instance running in memory
	app = natron.getGuiInstance(0)

	# create a 'Roto' node
	myRoto = app.createNode("fr.inria.built-in.Roto")

	# get input image size
	imageWidth = myRoto.getOutputFormat().width()

	imageHeight = myRoto.getOutputFormat().height()


	# set 'Roto' label
	myRoto.setLabel('full_Circle1')

	# get roto context
	rotoContext = myRoto.getRotoContext()

	# get 'Base Layer'
	Layer1_layer = rotoContext.getBaseLayer()

	# create square
	fullCircle = rotoContext.createEllipse(imageWidth/2,imageHeight/2,imageHeight,True,1)
	fullCircle.setLabel('full_Circle1')

	# set center position
	myRoto.getParam('center').setValue(imageWidth/2,0)
	myRoto.getParam('center').setValue(imageHeight/2,1)