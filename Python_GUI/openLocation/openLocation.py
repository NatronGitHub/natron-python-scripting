#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 22/06/2019.

import os, io
import string
import subprocess
from NatronEngine import*
from NatronGui import *


# OPEN 'READ' OR 'WRITE' LOCATION FOLDER IN EXPLORER. #

def openLocation():
	app = natron.getGuiInstance(0)
	selectedNodes = app.getSelectedNodes()
	
	for n in selectedNodes:
		myID = n.getPluginID()

		if myID == "fr.inria.built-in.Read" or myID == "fr.inria.built-in.Write" :
			myPath = n.getParam('filename').get()
			myFolder = os.path.split(myPath)[-2]
	

			# ---------------------------------------------------- #
			# ---------------------- Windows --------------------- #
			# ---------------------------------------------------- #
			if natron.isWindows() == 1 :
				print (myFolder)
				os.chdir(myFolder)
				subprocess.Popen( ['explorer', '.'] , stdin = subprocess.PIPE, stdout = subprocess.PIPE)

			# ---------------------------------------------------- #
			# ----------------------- Linux ---------------------- #
			# ---------------------------------------------------- #
			if natron.isLinux() == 1 :
				print (myFolder)
				# subprocess.Popen( ['thunar', myFolder] , stdin = subprocess.PIPE, stdout = subprocess.PIPE)
				subprocess.Popen(['xdg-open',myFolder] , stdin = subprocess.PIPE, stdout = subprocess.PIPE) # dont depend on a specific explorer

			# ---------------------------------------------------- #
			# ------------------------ OSX ----------------------- #
			# ---------------------------------------------------- #
			if natron.isMacOSX() == 1 :
				print (myFolder)
				subprocess.Popen( ['open', myFolder] , stdin = subprocess.PIPE, stdout = subprocess.PIPE)
