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

from Python_GUI.nodeBold_HTML.nodeBold_HTML import *
from Python_GUI.nodeItalic_HTML.nodeItalic_HTML import *
from Python_GUI.nodeColorChange.nodeColorChange import *
from Python_GUI.nodeChangeFPS.nodeChangeFPS import *
from Python_GUI.nodeChangeFrameRange.nodeChangeFrameRange import *
from Python_GUI.autoAlpha.autoAlpha import *
from Python_GUI.diskCache.diskCache import *
from Python_GUI.flipbook.flipbook import *

#####################################################################
#																	#
#							USER MENUS CREATION				        #
#																	#
#####################################################################


NatronGui.natron.addMenuCommand('Tools/Channel/Auto Alpha','autoAlpha')

NatronGui.natron.addMenuCommand('Tools/Node Graph/Node(s) Color','nodeColorChange')
NatronGui.natron.addMenuCommand('Tools/Node Graph/Bold Nodes <HTML>','nodeBold_HTML')
NatronGui.natron.addMenuCommand('Tools/Node Graph/Italic Nodes <HTML>','nodeItalic_HTML')

NatronGui.natron.addMenuCommand('Tools/Time/Read FPS','nodeChangeFPS()')
NatronGui.natron.addMenuCommand('Tools/Time/Read Frame Range','nodeChangeFrameRange()')

NatronGui.natron.addMenuCommand('Tools/Render/Disk Cache','diskCache()')
NatronGui.natron.addMenuCommand('Tools/Render/Flipbook','flipbook()')


separator = ('------------------------------------------------------------')
print '\n' + '\n' + separator
print separator
print '-------------------     INITGUI.PY     ---------------------'
print separator
print separator
print '\n'

print '- \'Tools\' user menu added'
print '\n' + '\n' + separator
print separator + '\n'