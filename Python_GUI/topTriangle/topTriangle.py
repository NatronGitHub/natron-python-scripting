#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 22/07/2019.

import string
import NatronEngine
from NatronGui import *


# CREATE A TOP ALIGNED TRIANGLE #

def topTriangle():

	# get current Natron instance running in memory
	app = natron.getGuiInstance(0)

	# create a 'Roto' node
	myRoto = app.createNode("fr.inria.built-in.Roto")

	# set 'Roto' label
	myRoto.setLabel('top_Triangle1')

	# get input image size
	imageWidth = myRoto.getOutputFormat().width()

	imageHeight = myRoto.getOutputFormat().height()




	# get roto context
	rotoContext = myRoto.getRotoContext()

	# get 'Base Layer'
	rootLayer = rotoContext.getBaseLayer()




	# create one point bezier curve at frame 1
	newTriangle = rotoContext.createBezier( 0.0 , imageHeight , 1 )

	newTriangle.setScriptName("top_Triangle1")
	newTriangle.setLabel("top_Triangle1")
	newTriangle.setLocked(False)
	newTriangle.setVisible(True)


	# add created bezier to 'Base Layer'
	rootLayer.addItem(newTriangle)

	newTriangle.addControlPoint( imageWidth , imageHeight )
	newTriangle.addControlPoint( imageWidth/2 , imageHeight/2 )
	newTriangle.setCurveFinished(1)