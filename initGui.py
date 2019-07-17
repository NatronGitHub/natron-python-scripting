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
from PySide.QtGui import *


#####################################################################
#																	#
#						IMPORT USER PYTHON TOOLS				    #
#																	#
#####################################################################

# Tools -> Channel
from Python_GUI.autoAlpha.autoAlpha import *

# Tools -> Generate
from Python_GUI.rotoToTracker.rotoToTracker import *
from Python_GUI.trackerToRoto.trackerToRoto import *

# Edit
from Python_GUI.batchRenameNodes.batchRenameNodes import *
from Python_GUI.connectNodes.connectNodes import *
from Python_GUI.forceCaching.forceCaching import *
from Python_GUI.invertSelection.invertSelection import *
from Python_GUI.nodeChangeColor.nodeChangeColor import *
from Python_GUI.nodeBold_HTML.nodeBold_HTML import *
from Python_GUI.nodeItalic_HTML.nodeItalic_HTML import *
from Python_GUI.openLocation.openLocation import *
from Python_GUI.selectSimilar.selectSimilar import *

# Tools -> Other
from Python_GUI.mergeBlendingDown.mergeBlendingDown import *
from Python_GUI.mergeBlendingUp.mergeBlendingUp import *

# Tools -> Time
from Python_GUI.nodeChangeFPS.nodeChangeFPS import *
from Python_GUI.nodeChangeFrameRange.nodeChangeFrameRange import *
from Python_GUI.timelineInOut.timelineInOut import *

# Tools -> Utils
from Python_GUI.collectFiles.collectFiles import *
from Python_GUI.replacePaths.replacePaths import *

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

NatronGui.natron.addMenuCommand('Tools/Generate/Roto to tracker','rotoToTracker')
NatronGui.natron.addMenuCommand('Tools/Generate/Tracker to roto','trackerToRoto')

NatronGui.natron.addMenuCommand('Edit/Batch rename','batchRenameNodes')
NatronGui.natron.addMenuCommand('Edit/Connect nodes','connectNodes', QtCore.Qt.Key.Key_Y, QtCore.Qt.KeyboardModifier)
NatronGui.natron.addMenuCommand('Edit/Force caching','forceCaching', QtCore.Qt.Key.Key_B, QtCore.Qt.KeyboardModifier.ControlModifier)
NatronGui.natron.addMenuCommand('Edit/Invert selection','invertSelection')
NatronGui.natron.addMenuCommand('Edit/Node(s) color','nodeChangeColor')
NatronGui.natron.addMenuCommand('Edit/Bold nodes <HTML>','nodeBold_HTML')
NatronGui.natron.addMenuCommand('Edit/Italic nodes <HTML>','nodeItalic_HTML')
NatronGui.natron.addMenuCommand('Edit/Open location','openLocation', QtCore.Qt.Key.Key_O, QtCore.Qt.KeyboardModifier.AltModifier)
NatronGui.natron.addMenuCommand('Edit/Select similar','selectSimilar')

NatronGui.natron.addMenuCommand('Tools/Other/Blending mode+','mergeBlendingDown', QtCore.Qt.Key.Key_Down, QtCore.Qt.KeyboardModifier)
NatronGui.natron.addMenuCommand('Tools/Other/Blending mode-','mergeBlendingUp', QtCore.Qt.Key.Key_Up, QtCore.Qt.KeyboardModifier)

NatronGui.natron.addMenuCommand('Tools/Time/Read FPS','nodeChangeFPS()')
NatronGui.natron.addMenuCommand('Tools/Time/Read frame range','nodeChangeFrameRange()')
NatronGui.natron.addMenuCommand('Tools/Time/Timeline IO','timelineInOut()')

NatronGui.natron.addMenuCommand('Tools/Utils/Collect files','collectFiles()')
NatronGui.natron.addMenuCommand('Tools/Utils/Replace paths','replacePaths()')

NatronGui.natron.addMenuCommand('Render/Background render','backgroundRender()', QtCore.Qt.Key.Key_R, QtCore.Qt.KeyboardModifier.AltModifier)
NatronGui.natron.addMenuCommand('Render/Disk cache','diskCache()', QtCore.Qt.Key.Key_D, QtCore.Qt.KeyboardModifier.AltModifier)
NatronGui.natron.addMenuCommand('Render/Flipbook','flipbook()', QtCore.Qt.Key.Key_F, QtCore.Qt.KeyboardModifier.AltModifier)


separator = ('------------------------------------------------------------')
print '\n' + '\n' + separator
print separator
print '-------------------     INITGUI.PY     ---------------------'
print separator
print separator
print '\n'

print '- \'Tools\' user menu added'
print '\n'
print '   + Tools/Channel/Auto Alpha'
print '   +'
print '   + Tools/Generate/Roto to tracker'
print '   + Tools/Generate/Tracker to roto'
print '   +'
print '   + Edit/Batch rename'
print '   + Edit/Connect nodes'
print '   + Edit/Force caching'
print '   + Edit/Invert selection'
print '   + Edit/Node(s) Color'
print '   + Edit/Bold nodes <HTML>'
print '   + Edit/Italic nodes <HTML>'
print '   + Edit/Open location'
print '   + Edit/Select similar'
print '   +'
print '   + Tools/Other/Blending mode+'
print '   + Tools/Other/Blending mode-'
print '   +'
print '   + Tools/Time/Read FPS'
print '   + Tools/Time/Read frame range'
print '   +'
print '   + Tools/Utils/Collect files'
print '   + Tools/Utils/Replace paths'
print '   +'
print '   + Render/Background render'
print '   + Render/Disk cache'
print '   + Render/Flipbook'


print '\n' + '\n' + separator
print separator + '\n'