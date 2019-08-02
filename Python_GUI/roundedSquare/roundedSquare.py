#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 22/07/2019.

import string
import NatronEngine
from NatronGui import *
from PySide.QtGui import *


# CREATE A FULL FRAME ROUNDED SQUARE #

def roundedSquare():

	# get current Natron instance running in memory
	app = natron.getGuiInstance(0)

	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Rounded square")

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
		myRoto.setLabel('rounded_Square1')

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
		newSquare = rotoContext.createBezier( (imageWidth / 2) - (imageHeight/2) + roundness , 0 , 1 )
		currentPoint = newSquare.getControlPointPosition( 0 , 1 )
		newSquare.setPointAtIndex( 0 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] - tangentRoundness , 0 , currentPoint[0] + tangentRoundness , 0 )
		newSquare.setFeatherPointAtIndex( 0 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] - tangentRoundness , 0 , currentPoint[0] + tangentRoundness , 0 )

		newSquare.setScriptName("rounded_Square1")
		newSquare.setLabel("rounded_Square1")
		newSquare.setLocked(False)
		newSquare.setVisible(True)



		# point 1
		newSquare.addControlPoint( (imageWidth / 2) + (imageHeight/2) - roundness , 0 )
		currentPoint = newSquare.getControlPointPosition( 1 , 1 )
		newSquare.setPointAtIndex( 1 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] - tangentRoundness , 0 , currentPoint[0] + tangentRoundness , 0 )
		newSquare.setFeatherPointAtIndex( 1 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] - tangentRoundness , 0 , currentPoint[0] + tangentRoundness , 0 )

		# point 2
		newSquare.addControlPoint( (imageWidth / 2) + (imageHeight/2) , roundness )
		currentPoint = newSquare.getControlPointPosition( 2 , 1 )
		newSquare.setPointAtIndex( 2 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] , currentPoint[1] - tangentRoundness , currentPoint[0] , currentPoint[1] + tangentRoundness )
		newSquare.setFeatherPointAtIndex( 2 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] , currentPoint[1] - tangentRoundness , currentPoint[0] , currentPoint[1] + tangentRoundness )

		# point 3
		newSquare.addControlPoint( (imageWidth / 2) + (imageHeight/2) , imageHeight - roundness )
		currentPoint = newSquare.getControlPointPosition( 3 , 1 )
		newSquare.setPointAtIndex( 3 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] , currentPoint[1] - tangentRoundness , currentPoint[0] , currentPoint[1] + tangentRoundness )
		newSquare.setFeatherPointAtIndex( 3 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] , currentPoint[1] - tangentRoundness , currentPoint[0] , currentPoint[1] + tangentRoundness )

		# point 4
		newSquare.addControlPoint( (imageWidth / 2) + (imageHeight/2) - roundness , imageHeight )
		currentPoint = newSquare.getControlPointPosition( 4 , 1 )
		newSquare.setPointAtIndex( 4 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] + tangentRoundness , imageHeight , currentPoint[0] - tangentRoundness , imageHeight )
		newSquare.setFeatherPointAtIndex( 4 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] + tangentRoundness , imageHeight , currentPoint[0] - tangentRoundness , imageHeight )

		# point 5
		newSquare.addControlPoint( (imageWidth / 2) - (imageHeight/2) + roundness , imageHeight )
		currentPoint = newSquare.getControlPointPosition( 5 , 1 )
		newSquare.setPointAtIndex( 5 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] + tangentRoundness , imageHeight , currentPoint[0] - tangentRoundness , imageHeight )
		newSquare.setFeatherPointAtIndex( 5 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] + tangentRoundness , imageHeight , currentPoint[0] - tangentRoundness , imageHeight )

		# point 6
		newSquare.addControlPoint( (imageWidth / 2) - (imageHeight/2) , imageHeight - roundness )
		currentPoint = newSquare.getControlPointPosition( 6 , 1 )
		newSquare.setPointAtIndex( 6 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] , currentPoint[1] + tangentRoundness , currentPoint[0] , currentPoint[1] - tangentRoundness )
		newSquare.setFeatherPointAtIndex( 6 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] , currentPoint[1] + tangentRoundness , currentPoint[0] , currentPoint[1] - tangentRoundness )

		# point 7
		newSquare.addControlPoint( (imageWidth / 2) - (imageHeight/2) , roundness )
		currentPoint = newSquare.getControlPointPosition( 7 , 1 )
		newSquare.setPointAtIndex( 7 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] , currentPoint[1] + tangentRoundness , currentPoint[0] , currentPoint[1] - tangentRoundness )
		newSquare.setFeatherPointAtIndex( 7 , 1 , currentPoint[0] , currentPoint[1] , currentPoint[0] , currentPoint[1] + tangentRoundness , currentPoint[0] , currentPoint[1] - tangentRoundness )


		# close the curve
		newSquare.setCurveFinished(1)

		# add created bezier to 'Base Layer'
		rootLayer.addItem(newSquare)

		# set center position
		myRoto.getParam('center').setValue(imageWidth/2,0)
		myRoto.getParam('center').setValue(imageHeight/2,1)