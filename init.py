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

from Python_INIT.listNatronPath import *
from Python_INIT.listPyPlugs import *
from Python_INIT.natronLogo import *

			

# CREATES A NEW DEPTH LAYER #
#---------------------------#
def addDepthLayer(app):
    depthPlane = NatronEngine.ImageLayer( "Depth" , "Depth" , "Z")
    app.addProjectLayer( depthPlane )




# DEFINES WHAT HAPPENS AFTER SOME NODE CREATION #
#-----------------------------------------------#
def Node_Callback(thisNode, app, userEdited):

	if thisNode.getPluginID() == "net.sf.openfx.ConstantPlugin" :
		thisNode.enablePreview.setValue(1)
		thisNode.hideInputs.setValue(1)

	elif thisNode.getPluginID() == "net.sf.openfx.Solid" :
		thisNode.enablePreview.setValue(1)
		thisNode.hideInputs.setValue(1)

	elif  thisNode.getPluginID() == "net.sf.openfx.FrameHold":
		currentFrame = app.timelineGetTime()
		thisNode.firstFrame.setValue(currentFrame)

	#elif thisNode.getPluginID() == "net.sf.openfx.MergePlugin" :
		#thisNode.bbox.set('b')

	elif thisNode.getPluginID() == "fr.inria.built-in.Read" :
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
    addDepthLayer(app)
    setNodeDefaults(app)


NatronEngine.natron.setOnProjectCreatedCallback("Project_Callback")
NatronEngine.natron.setOnProjectLoadedCallback("Project_Callback")


#################### STARTING CONSOLE MESSAGES ####################
#-----------------------------------------------------------------#
#natronLogo()




separator = ('------------------------------------------------------------')
print '\n' + '\n' + separator
print separator
print '--------------------     INIT.PY     -----------------------'
print separator
print separator
print '\n'


# check Natron's version status, version number, x32 or x64 version #
#-------------------------------------------------------------------#
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
print '- Depth layer added to the viewer'
print '\n'
print separator


##################################################################

PathMessage = ("- NATRON PLUGINS SEARCH PATH :")
print ('\n' + PathMessage + '\n')

#################### print NATRON search path ####################
listNatronPath()

print '\n' + separator

PyPlugMessage = ("- PYPLUGs LOADED :")
print separator
print '\n' + PyPlugMessage

#################### print PYPLUG list ####################
listPyPlugs()

print '\n' + separator
print separator