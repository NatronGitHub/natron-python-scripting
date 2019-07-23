#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 22/07/2019.

import string
import NatronEngine
from NatronGui import *
from PySide.QtGui import *


# CREATE A FULL FRAME ROUNDED RECTANGLE #

def roundedRectangle():

	# get current Natron instance running in memory
	app = natron.getGuiInstance(0)

	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Rounded rectangle")

	# set dialog margins #
	dialog.setContentsMargins(0, 0, 10, 10)

	# set window size #
	dialog.resize( 400, 100 )

	# UI creation #
	line01 = dialog.createStringParam("line01","")
	line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line02 = dialog.createStringParam("line02","")
	line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	hardnessParameter = dialog.createDoubleParam("userHardness","Hardness : ")
	hardnessParameter.setDefaultValue(10)
	hardnessParameter.restoreDefaultValue()

	hardnessParameter.setMinimum(3)
	hardnessParameter.setDisplayMinimum(3)
	hardnessParameter.setDisplayMaximum(20)


	#################################################

	# Refresh UI #
	dialog.refreshUserParamsGUI()



	# if user press 'OK' #
	if dialog.exec_():


		# create a 'Roto' node
		myRoto = app.createNode("fr.inria.built-in.Roto")

		# set 'Roto' label
		myRoto.setLabel('rounded_Rectangle1')

		# get input image size
		imageWidth = myRoto.getOutputFormat().width()

		imageHeight = myRoto.getOutputFormat().height()

		roundness = imageHeight / hardnessParameter.get()
		tangentRoundness = roundness / 2


		# get roto context
		rotoContext = myRoto.getRotoContext()

		# get 'Base Layer'
		rootLayer = rotoContext.getBaseLayer()




		# create one point bezier curve at frame 1

		# point 0
		newRectangle = rotoContext.createBezier( roundness , 0 , 1 )
		newRectangle.setPointAtIndex( 0 , 1 , roundness , 0 , tangentRoundness , 0 , roundness + tangentRoundness , 0 )
		newRectangle.setFeatherPointAtIndex( 0 , 1 , roundness , 0 , tangentRoundness , 0 , roundness + tangentRoundness , 0 )

		newRectangle.setScriptName("rounded_Rectangle1")
		newRectangle.setLabel("rounded_Rectangle1")
		newRectangle.setLocked(False)
		newRectangle.setVisible(True)


		# add created bezier to 'Base Layer'
		rootLayer.addItem(newRectangle)

		# point 1
		newRectangle.addControlPoint( imageWidth - roundness , 0 )
		newRectangle.setPointAtIndex( 1 , 1 , imageWidth - roundness , 0 , imageWidth - (roundness*2) + tangentRoundness , 0 , imageWidth - roundness + tangentRoundness , 0 )
		newRectangle.setFeatherPointAtIndex( 1 , 1 , imageWidth - roundness , 0 , imageWidth - (roundness*2) + tangentRoundness , 0 , imageWidth - roundness + tangentRoundness , 0 )

		# point 2
		newRectangle.addControlPoint( imageWidth , roundness )
		newRectangle.setPointAtIndex( 2 , 1 , imageWidth , roundness , imageWidth , roundness - tangentRoundness , imageWidth , roundness + tangentRoundness )
		newRectangle.setFeatherPointAtIndex( 2 , 1 , imageWidth , roundness , imageWidth , roundness - tangentRoundness , imageWidth , roundness + tangentRoundness )

		# point 3
		newRectangle.addControlPoint( imageWidth , imageHeight - roundness )
		newRectangle.setPointAtIndex( 3 , 1 , imageWidth , imageHeight - roundness , imageWidth , imageHeight - roundness - tangentRoundness , imageWidth , imageHeight - roundness + tangentRoundness )
		newRectangle.setFeatherPointAtIndex( 3 , 1 , imageWidth , imageHeight - roundness , imageWidth , imageHeight - roundness - tangentRoundness , imageWidth , imageHeight - roundness + tangentRoundness )

		# point 4
		newRectangle.addControlPoint( imageWidth - roundness , imageHeight )
		newRectangle.setPointAtIndex( 4 , 1 , imageWidth - roundness , imageHeight , imageWidth - roundness + tangentRoundness , imageHeight , imageWidth - roundness - tangentRoundness , imageHeight )
		newRectangle.setFeatherPointAtIndex( 4 , 1 , imageWidth - roundness , imageHeight , imageWidth - roundness + tangentRoundness , imageHeight , imageWidth - roundness - tangentRoundness , imageHeight )

		# point 5
		newRectangle.addControlPoint( roundness , imageHeight )
		newRectangle.setPointAtIndex( 5 , 1 , roundness , imageHeight , roundness + tangentRoundness , imageHeight , roundness - tangentRoundness , imageHeight )
		newRectangle.setFeatherPointAtIndex( 5 , 1 , roundness , imageHeight , roundness + tangentRoundness , imageHeight , roundness - tangentRoundness , imageHeight )

		# point 6
		newRectangle.addControlPoint( 0 , imageHeight - roundness )
		newRectangle.setPointAtIndex( 6 , 1 , 0 , imageHeight - roundness , 0 , imageHeight - roundness + tangentRoundness , 0 , imageHeight - roundness - tangentRoundness )
		newRectangle.setFeatherPointAtIndex( 6 , 1 , 0 , imageHeight - roundness , 0 , imageHeight - roundness + tangentRoundness , 0 , imageHeight - roundness - tangentRoundness )

		# point 7
		newRectangle.addControlPoint( 0 , roundness )
		newRectangle.setPointAtIndex( 7 , 1 , 0 , roundness , 0 , roundness + tangentRoundness , 0 , roundness - tangentRoundness )
		newRectangle.setFeatherPointAtIndex( 7 , 1 , 0 , roundness , 0 , roundness + tangentRoundness , 0 , roundness - tangentRoundness )


		newRectangle.setCurveFinished(1)