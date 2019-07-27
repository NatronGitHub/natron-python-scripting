#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 23/06/2019.

import string
import NatronEngine
from NatronGui import *


# TRACKER TO ROTO #

def rotoLink():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# get selected nodes # 
	selectedNodes = app.getSelectedNodes()

	# if 2 nodes have been selected #
	if len(selectedNodes) == 2 :
		rotoID = selectedNodes[0].getPluginID()
		
		# if first selected node is a Roto or a RotoPaint #
		if rotoID == 'fr.inria.built-in.Roto' or rotoID == 'fr.inria.built-in.RotoPaint':
			trackerID = selectedNodes[1].getPluginID()

			# if second selected node is not a Tracker #
			if trackerID != 'fr.inria.built-in.Tracker':
				warning = natron.warningDialog("Warning","Select a Roto and a Tracker.")

			# if second selected node is a Tracker #
			else :
				# get Roto context #
				rotoContext = selectedNodes[0].getRotoContext()

				# get base layer #
				Layer1_layer = rotoContext.getBaseLayer()

				# set Tracker Motion Type to Match-Move #
				selectedNodes[1].getParam('motionType').set('Match-Move')

				# set Tracker Transform Type to Transform #
				selectedNodes[1].getParam('transformType').set('Transform')



				# GET ROTO TRANSFORM PARAMETERS #

				# get Roto Translate parameters #
				rotoTranslate = selectedNodes[0].getParam('translate')

				# get Roto Rotate parameter #
				rotoRotate = selectedNodes[0].getParam('rotate')

				# get Roto Scale parameters #
				rotoScale = selectedNodes[0].getParam('scale')

				# get Roto Center parameters #
				rotoCenter = selectedNodes[0].getParam('center')



				# GET TRACKER TRANSFORM PARAMETERS #

				# get Tracker Translate parameters #
				trackerTranslate = selectedNodes[1].getParam('translate')

				# get Tracker Rotate parameter #
				trackerRotate = selectedNodes[1].getParam('rotate')

				# get Tracker Scale parameters #
				trackerScale = selectedNodes[1].getParam('scale')

				# get Tracker Center parameters #
				trackerCenter = selectedNodes[1].getParam('center')



				# LINKING PARAMETERS FROM TRACKER TO ROTO #

				rotoTranslate.slaveTo(trackerTranslate,0,0)
				rotoTranslate.slaveTo(trackerTranslate,1,1)

				rotoRotate.slaveTo(trackerRotate,0,0)

				rotoScale.slaveTo(trackerScale,0,0)
				rotoScale.slaveTo(trackerScale,1,1)

				rotoCenter.slaveTo(trackerCenter,0,0)
				rotoCenter.slaveTo(trackerCenter,1,1)


		# if first selected node is a Roto or a RotoPaint #
		else :
			warning = natron.warningDialog("Warning","Select a Roto first.")

	# if more or less than 2 nodes have been selected #
	else :
		warning = natron.warningDialog("Warning","Select 2 nodes.")