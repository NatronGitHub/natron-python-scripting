#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 06/07/2019.

import NatronEngine
from NatronGui import *


# SELECT SIMILAR NODES BY COLOR #

def snapNodes():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# get selected nodes #
	snapx = 100
	snapy = 50
	mysel= app.getSelectedNodes()
	for mynode in mysel:
		mypos = mynode.getPosition()
		mynode.setPosition( round( float(mypos[0]) / float(snapx) )* snapx , round( float(mypos[1]) / float(snapy) )* snapy )
