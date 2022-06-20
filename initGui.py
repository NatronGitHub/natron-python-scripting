#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 26/01/2018.


#####################################################################
#																	#
#				 		   IMPORT NATRON MODULES			 	    #
#																	#
#####################################################################

import os
import sys
from NatronEngine import *
from NatronGui import *
try:
    from qtpy.QtGui import *
except ImportError:
    from PySide.QtGui import *


#####################################################################
#																	#
#						IMPORT USER PYTHON TOOLS				    #
#																	#
#####################################################################

# Tools -> Channel
from Python_GUI.autoAlpha.autoAlpha import *
from Python_GUI.extractExrLayers.extractExrLayers import *
from Python_GUI.extractImageLayers.extractImageLayers import *

# Tools -> Generate
from Python_GUI.postageStamp.postageStamp import *
from Python_GUI.rotoToTracker.rotoToTracker import *
from Python_GUI.trackerToRoto.trackerToRoto import *

# Edit
from Python_GUI.batchRenameNodes.batchRenameNodes import *
from Python_GUI.connectNodes.connectNodes import *
from Python_GUI.reconnectNodes.reconnectNodes import *
from Python_GUI.autoReconnect.autoReconnect import *
from Python_GUI.forceCaching.forceCaching import *
from Python_GUI.invertSelection.invertSelection import *
from Python_GUI.nodeChangeColor.nodeChangeColor import *
from Python_GUI.nodeBold_HTML.nodeBold_HTML import *
from Python_GUI.nodeItalic_HTML.nodeItalic_HTML import *
from Python_GUI.openLocation.openLocation import *
from Python_GUI.removeInput.removeInput import *
from Python_GUI.selectSimilarByClass.selectSimilarByClass import *
from Python_GUI.selectSimilarByColor.selectSimilarByColor import *

# Tools -> Other
from Python_GUI.mergeBlendingDown.mergeBlendingDown import *
from Python_GUI.mergeBlendingUp.mergeBlendingUp import *
from Python_GUI.rotoLink.rotoLink import *

# Tools -> Roto
from Python_GUI.fullCircle.fullCircle import *
from Python_GUI.fullEllipse.fullEllipse import *
from Python_GUI.fullSquare.fullSquare import *
from Python_GUI.roundedSquare.roundedSquare import *
from Python_GUI.fullRectangle.fullRectangle import *
from Python_GUI.roundedRectangle.roundedRectangle import *

from Python_GUI.leftTriangle.leftTriangle import *
from Python_GUI.rightTriangle.rightTriangle import *
from Python_GUI.topTriangle.topTriangle import *
from Python_GUI.bottomTriangle.bottomTriangle import *

# Tools -> Time
from Python_GUI.nodeChangeFPS.nodeChangeFPS import *
from Python_GUI.nodeChangeFrameRange.nodeChangeFrameRange import *
from Python_GUI.timelineInOut.timelineInOut import *

# Tools -> Utils
from Python_GUI.collectFiles.collectFiles import *
from Python_GUI.replacePaths.replacePaths import *
from Python_GUI.batchSelectedNodes.batchSelectedNodes import *

# Render
from Python_GUI.backgroundRender.backgroundRender import *
from Python_GUI.diskCache.diskCache import *
from Python_GUI.flipbook.flipbook import *

#####################################################################
#																	#
#							USER MENUS CREATION				        #
#																	#
#####################################################################

NatronGui.natron.addMenuCommand('Tools/Channel/Auto alpha','autoAlpha')
NatronGui.natron.addMenuCommand('Tools/Channel/Extract EXR layers','extractExrLayers')
NatronGui.natron.addMenuCommand('Tools/Channel/Extract Image layers','extractImageLayers')

NatronGui.natron.addMenuCommand('Tools/Generate/PostageStamp','postageStamp', QtCore.Qt.Key.Key_P, QtCore.Qt.KeyboardModifier.ControlModifier | QtCore.Qt.AltModifier)
NatronGui.natron.addMenuCommand('Tools/Generate/Roto to tracker','rotoToTracker')
NatronGui.natron.addMenuCommand('Tools/Generate/Tracker to roto','trackerToRoto')

NatronGui.natron.addMenuCommand('Edit/Batch rename','batchRenameNodes')
NatronGui.natron.addMenuCommand('Edit/Connect nodes','connectNodes', QtCore.Qt.Key.Key_Y, QtCore.Qt.KeyboardModifier)
NatronGui.natron.addMenuCommand('Edit/Reconnect nodes','reconnectNodes', QtCore.Qt.Key.Key_Y, QtCore.Qt.KeyboardModifier.AltModifier)
NatronGui.natron.addMenuCommand('Edit/auto Reconnect Nodes','autoReconnect', QtCore.Qt.Key.Key_Y, QtCore.Qt.KeyboardModifier.ShiftModifier)
NatronGui.natron.addMenuCommand('Edit/Force caching','forceCaching', QtCore.Qt.Key.Key_B, QtCore.Qt.KeyboardModifier.ControlModifier)
NatronGui.natron.addMenuCommand('Edit/Color...','nodeChangeColor', QtCore.Qt.Key.Key_C, QtCore.Qt.KeyboardModifier.ControlModifier | QtCore.Qt.ShiftModifier)
NatronGui.natron.addMenuCommand('Edit/Bold node','nodeBold_HTML')
NatronGui.natron.addMenuCommand('Edit/Italic node','nodeItalic_HTML')
NatronGui.natron.addMenuCommand('Edit/Open location','openLocation', QtCore.Qt.Key.Key_O, QtCore.Qt.KeyboardModifier.AltModifier)
NatronGui.natron.addMenuCommand('Edit/Select similar/Class','selectSimilarByClass')
NatronGui.natron.addMenuCommand('Edit/Select similar/Color','selectSimilarByColor')
NatronGui.natron.addMenuCommand('Edit/Invert selection','invertSelection', QtCore.Qt.Key.Key_I, QtCore.Qt.KeyboardModifier.ControlModifier | QtCore.Qt.ShiftModifier)
NatronGui.natron.addMenuCommand('Edit/Remove input','removeInput', QtCore.Qt.Key.Key_D, QtCore.Qt.KeyboardModifier.ControlModifier)

NatronGui.natron.addMenuCommand('Tools/Other/Blending mode+','mergeBlendingDown', QtCore.Qt.Key.Key_Down, QtCore.Qt.AltModifier)
NatronGui.natron.addMenuCommand('Tools/Other/Blending mode-','mergeBlendingUp', QtCore.Qt.Key.Key_Up, QtCore.Qt.AltModifier)
NatronGui.natron.addMenuCommand('Tools/Other/Link roto to tracker','rotoLink', QtCore.Qt.Key.Key_L, QtCore.Qt.KeyboardModifier.ControlModifier | QtCore.Qt.ShiftModifier)

NatronGui.natron.addMenuCommand('Tools/Roto/Circle','fullCircle()')
NatronGui.natron.addMenuCommand('Tools/Roto/Ellipse','fullEllipse()')
NatronGui.natron.addMenuCommand('Tools/Roto/Square','fullSquare()')
NatronGui.natron.addMenuCommand('Tools/Roto/Rounded square','roundedSquare()')
NatronGui.natron.addMenuCommand('Tools/Roto/Rectangle','fullRectangle()')
NatronGui.natron.addMenuCommand('Tools/Roto/Rounded rectangle','roundedRectangle()')
NatronGui.natron.addMenuCommand('Tools/Roto/Left Triangle','leftTriangle()')
NatronGui.natron.addMenuCommand('Tools/Roto/Right Triangle','rightTriangle()')
NatronGui.natron.addMenuCommand('Tools/Roto/Top Triangle','topTriangle()')
NatronGui.natron.addMenuCommand('Tools/Roto/Bottom Triangle','bottomTriangle()')

NatronGui.natron.addMenuCommand('Tools/Time/Read FPS','nodeChangeFPS()')
NatronGui.natron.addMenuCommand('Tools/Time/Read frame range','nodeChangeFrameRange()')
NatronGui.natron.addMenuCommand('Tools/Time/Timeline IO','timelineInOut()')

NatronGui.natron.addMenuCommand('Tools/Utils/Collect files','collectFiles()')
NatronGui.natron.addMenuCommand('Tools/Utils/Replace paths','replacePaths()')
NatronGui.natron.addMenuCommand('Tools/Utils/Batch Selected Nodes','batchSelectedNodes')

NatronGui.natron.addMenuCommand('Render/Background render','backgroundRender()', QtCore.Qt.Key.Key_R, QtCore.Qt.KeyboardModifier.AltModifier)
NatronGui.natron.addMenuCommand('Render/Disk cache','diskCache()', QtCore.Qt.Key.Key_D, QtCore.Qt.KeyboardModifier.AltModifier)
NatronGui.natron.addMenuCommand('Render/Flipbook','flipbook()', QtCore.Qt.Key.Key_F, QtCore.Qt.KeyboardModifier.AltModifier)

# from Python_GUI.snapNodes.snapNodes import *
# NatronGui.natron.addMenuCommand('Tools/Node Graph/snap Nodes','snapNodes',  QtCore.Qt.Key.Key_A,QtCore.Qt.KeyboardModifier)
# NatronGui.natron.addMenuCommand('Tools/Node Graph/Align Nodes X','alignNodesX' )
# NatronGui.natron.addMenuCommand('Tools/Node Graph/Align Nodes Y','alignNodesY' )
# NatronGui.natron.addMenuCommand('Tools/Node Graph/Spread Nodes X','spreadNodesX' )
# NatronGui.natron.addMenuCommand('Tools/Node Graph/Spread Nodes Y','spreadNodesY' )

separator = ('------------------------------------------------------------')
print ('\n' + '\n' + separator)
print (separator)
print ('-------------------     INITGUI.PY     ---------------------')
print (separator)
print (separator)
print ('\n')

print ('- \'Tools\' user menu added')
print ('\n')
print ('   + Tools/Channel/Auto Alpha')
print ('   + Tools/Channel/Extract EXR layers')
print ('   + Tools/Channel/Extract Image layers')
print ('   +')
print ('   + Tools/Generate/PostageStamp')
print ('   + Tools/Generate/Roto to tracker')
print ('   + Tools/Generate/Tracker to roto')
print ('   +')
print ('   + Edit/Batch rename')
print ('   + Edit/Connect nodes')
print ('   + Edit/Reconnect nodes')
print ('   + Edit/Force caching')
print ('   + Edit/Invert selection')
print ('   + Edit/Node Color')
print ('   + Edit/Bold node')
print ('   + Edit/Italic node')
print ('   + Edit/Open location')
print ('   + Edit/Select similar/Class')
print ('   + Edit/Select similar/Color')
print ('   + Edit/Remove input')
print ('   +')
print ('   + Tools/Other/Blending mode+')
print ('   + Tools/Other/Blending mode-')
print ('   + Tools/Other/Link roto to tracker')
print ('   +')
print ('   + Tools/Roto/Circle')
print ('   + Tools/Roto/Ellipse')
print ('   + Tools/Roto/Square')
print ('   + Tools/Roto/Rounded square')
print ('   + Tools/Roto/Rectangle')
print ('   + Tools/Roto/Rounded rectangle')
print ('   + Tools/Roto/Left triangle')
print ('   + Tools/Roto/Right triangle')
print ('   + Tools/Roto/Top triangle')
print ('   + Tools/Roto/Bottom triangle')
print ('   +')
print ('   + Tools/Time/Read FPS')
print ('   + Tools/Time/Read frame range')
print ('   +')
print ('   + Tools/Utils/Collect files')
print ('   + Tools/Utils/Replace paths')
print ('   +')
print ('   + Render/Background render')
print ('   + Render/Disk cache')
print ('   + Render/Flipbook')


print ('\n' + '\n' + separator)
print (separator + '\n')