		#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 17/01/2018.


#####################################################################
#																	#
#				 		   IMPORT NATRON MODULES			 	    #
#																	#
#####################################################################

import os
import string
from NatronEngine import*
from os import*


#####################################################################
#																	#
#						IMPORT USER PYTHON TOOLS				    #
#																	#
#####################################################################

from Python_INIT.listNatronPath.listNatronPath import *
from Python_INIT.listPyPlugs.listPyPlugs import *
from Python_INIT.natronLogo.natronLogo import *




# CREATES A NEW 'DEEP' LAYER #
#----------------------------#
def addDeepLayer(app):
	depthPlane = NatronEngine.ImageLayer( "Deep" , "Deep" , "FB")
	app.addProjectLayer( depthPlane )

# CREATES A NEW 'DEPTH' LAYER #
#-----------------------------#
def addDepthLayer(app):
	depthPlane = NatronEngine.ImageLayer( "Depth" , "Depth" , "Z")
	app.addProjectLayer( depthPlane )

# CREATES A NEW 'MASK' LAYER #
#----------------------------#
def addMaskLayer(app):
	depthPlane = NatronEngine.ImageLayer( "Mask" , "Mask" , "A")
	app.addProjectLayer( depthPlane )

# CREATES A NEW 'MOTION' LAYER #
#------------------------------#
def addMotionLayer(app):
    depthPlane = NatronEngine.ImageLayer( "Motion" , "Motion" , "UV" )
    app.addProjectLayer( depthPlane )


# SET UP DEFAULT PROJECT SETTINGS #
#------------------------------#
def setProjectSettings(app):
	app.getProjectParam('outputFormat').setValue("HD 1920x1080")
	app.getProjectParam('autoPreviews').setValue(True)
	app.getProjectParam('frameRange').set(1, 25)
	app.getProjectParam('lockRange').setValue(True)
	app.getProjectParam('frameRate').setValue(25)
	app.getProjectParam('gpuRendering').setValue('Enabled')


# DEFINES WHAT HAPPENS AFTER SPECIFIC NODES CREATION #
#-----------------------------------------------#
def Node_Callback(thisNode, app, userEdited):

	if thisNode.getPluginID() == "net.sf.openfx.ConstantPlugin" :
		thisNode.enablePreview.setValue(1)
		thisNode.hideInputs.setValue(1)

	if thisNode.getPluginID() == "net.sf.openfx.Solid" :
		thisNode.enablePreview.setValue(1)
		thisNode.hideInputs.setValue(1)

	if thisNode.getPluginID() == "net.sf.openfx.FrameHold":
		currentFrame = app.timelineGetTime()
		thisNode.firstFrame.setValue(currentFrame)

	#elif thisNode.getPluginID() == "net.sf.openfx.MergePlugin" :
		#thisNode.bbox.set('b')

	if thisNode.getPluginID() == "fr.inria.built-in.Read" :
		#thisNode.outputComponents.set('RGBA')
		thisNode.hideInputs.setValue(1)
		thisNode.outputLayer.set('Color.RGBA')

	elif thisNode.getPluginID() == "fr.inria.built-in.Write" :
		thisNode.formatType.set('Input Format')
		thisNode.frameRange.set('Manual')

	elif thisNode.getPluginID() == "net.sf.openfx.CheckerBoardPlugin" :
		thisNode.enablePreview.setValue(1)
		thisNode.hideInputs.setValue(1)

	elif thisNode.getPluginID() == "fr.inria.built-in.Roto" :
		thisNode.setColor(0.16,0.56,0.16)
		thisNode.enablePreview.setValue(1)

	elif thisNode.getPluginID() == "fr.inria.built-in.RotoPaint" :
		thisNode.setColor(0.16,0.56,0.16)
		thisNode.enablePreview.setValue(1)



def setNodeDefaults(app):
    app.afterNodeCreated.set("Node_Callback")



# SETUP CALLBACKS #
#-----------------#
def Project_Callback(app):
	addDeepLayer(app)
	addDepthLayer(app)
	addMaskLayer(app)
	addMotionLayer(app)
	setNodeDefaults(app)
	setProjectSettings(app)


NatronEngine.natron.setOnProjectCreatedCallback("Project_Callback")
NatronEngine.natron.setOnProjectLoadedCallback("Project_Callback")


#-----------------------------------------------------------------#
#################### STARTING CONSOLE MESSAGES ####################
#-----------------------------------------------------------------#


separator = ('------------------------------------------------------------')
print '\n' + '\n' + separator
print separator
print '\n'

natronLogo()


print '\n' + '\n' + separator
print separator
print '--------------------     INIT.PY     -----------------------'
print separator
print separator


# check Natron's version status, version number, x32 or x64 version #
#-------------------------------------------------------------------#
print '\n'
NatronStatus = natron.getNatronDevelopmentStatus()
NatronVersion = natron.getNatronVersionString()
binary = 'x64'
x32_64 = natron.is64Bit()
if x32_64 == 0 :
	binary = 'x32'

print ('- NATRON ') + 'version ' + NatronVersion + ' ' + str(NatronStatus) + ' (' + binary + ')'
print '\n'
print separator

print '\n'
CPUs = natron.getNumCpus()
print ('- ') + str(CPUs) + (' CPUs available on the system')
print '\n'
print separator

print '\n'
print '- Deep layer added to the viewer'
print '- Depth layer added to the viewer'
print '- Mask layer added to the viewer'
print '- Motion layer added to the viewer'
print '\n'
print separator


##################################################################

PathMessage = ("- NATRON PLUGINS SEARCH PATH :")
print ('\n' + PathMessage + '\n')

#################### print NATRON search path ####################
listNatronPath()

print '\n' + separator

PyPlugMessage = ("- PYPLUG(S) LOADED :")
print separator
print '\n' + PyPlugMessage

#################### print PYPLUG list ####################
listPyPlugs()

print '\n' + separator
print separator