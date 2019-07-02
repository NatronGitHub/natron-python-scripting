#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 19/06/2019.

import os
import string
import shutil
import NatronEngine
from NatronGui import *

# SETS FRAMEHOLD DEFAULT VALUE #

def collectFiles():

	# get current Natron instance running in memory #
	app = natron.getGuiInstance(0)

	# we grab current project name #
	projectName = app.getProjectParam('projectName').get()
	projectName = os.path.splitext(projectName)[0]

	# Gives user's home directory
	myUserPath = os.path.expanduser('~')

	# Gives username by splitting path based on OS
	myUser = os.path.split(myUserPath)[-1]	


	# ---------------------------------------------------- #
	# ---------------------- Windows --------------------- #
	# ---------------------------------------------------- #

	if natron.isWindows() == 1 :

		# get diskCachePath from Preferences #
		userDiskCachePath = NatronEngine.natron.getSettings().getParam('diskCachePath').get()

		# build 'Localize' path #
		if userDiskCachePath == '':

			# if diskCachePath is empty (default) #
			localizeFolderPath = str(myUserPath) + '\\AppData\\Local\\INRIA\\Natron\\Localize\\'

		else :

			# if diskCachePath is set to a custom folder #
			localizeFolderPath = str(userDiskCachePath) + '\\Localize\\'


	# ---------------------------------------------------- #
	# --------------------- Linux/OSX -------------------- #
	# ---------------------------------------------------- #

	if natron.isLinux() == 1 or natron.isMacOSX() == 1 :

		# get diskCachePath from Preferences #
		userDiskCachePath = NatronEngine.natron.getSettings().getParam('diskCachePath').get()

		# build 'Localize' path #
		if userDiskCachePath == '':

			# if diskCachePath is empty (default) #
			localizeFolderPath = str(myUserPath) + '/.cache/INRIA/Natron/Localize/'

		else :
			# if diskCachePath is set to a custom folder #
			localizeFolderPath = str(userDiskCachePath) + '/Localize/'



	# check if output folder exists. If not, we create it #
	if not os.path.exists(localizeFolderPath):
		os.makedirs(localizeFolderPath)


	# we select all nodes #
	app.selectAllNodes()

	# we get selected nodes #
	selectedNodes = app.getSelectedNodes()

	# we cycle all selected nodes #
	for currentNode in selectedNodes:

		# get current node ID #
		nodeID = currentNode.getPluginID()

		# if node is not a 'Read' node #
		if nodeID == 'fr.inria.built-in.Read':

			# we grab the complete file path #
			fileCompletePath = currentNode.getParam('filename').get()

			# we grab the file name only #
			fileName = os.path.basename(fileCompletePath)

			# we grab the file path #
			filePath = fileCompletePath.replace(fileName,'')

			# file name without the extension #
			fileNameNoExt = os.path.splitext(fileName)[0]


			# ------------------------- #
			# IF FILE IS NOT A SEQUENCE #
			# ------------------------- #

			if '#' not in str(fileName):

				# a created folder will be named as the file #
				newFileFolder = str(localizeFolderPath) + str(projectName) + '_COLLECT' + '/Sources/' + str(fileNameNoExt)

				# we create the folder #
				if os.path.exists(newFileFolder):
					pass
				else:
					os.makedirs(newFileFolder)

				# we copy the file #
				shutil.copy(fileCompletePath,newFileFolder)

				# we get copied file path #
				newPath = './Sources/'+ str(fileNameNoExt) + '/' + str(fileName)

				# we grab the file path again #
				fileCompletePath = currentNode.getParam('filename')
			
				# we set the new file path #
				fileCompletePath.set(newPath)


			# --------------------- #
			# IF FILE IS A SEQUENCE #
			# --------------------- #

			if '#' in str(fileName):

				fileNameNoExt = fileNameNoExt.replace('#','')
				fileNameNoExt = fileNameNoExt[:-1]

				# a created folder will be named as the file #
				newFileFolder = str(localizeFolderPath) + str(projectName) + '_COLLECT' + '/Sources/' + str(fileNameNoExt)

				# we create the folder #
				if os.path.exists(newFileFolder):
					pass
				else:
					os.makedirs(newFileFolder)

				os.chdir(filePath)
				cwd = os.getcwd()
				
				for basename in os.listdir(cwd):
					if fileNameNoExt in basename:
						shutil.copy(basename,newFileFolder)

				# we get copied file path #
				newPath = './Sources/'+ str(fileNameNoExt) + '/' + str(fileName)

				# we grab the file path again #
				fileCompletePath = currentNode.getParam('filename')
			
				# we set the new file path #
				fileCompletePath.set(newPath)

	# we save the project #
	rootFolder = str(localizeFolderPath) + str(projectName) + '_COLLECT' + '/'
	newProjectName = str(projectName) + '_COLLECT'


	os.chdir(rootFolder)
	app.saveProjectAs(newProjectName)
	app.resetProject()

	newNatronProject = rootFolder + newProjectName + '.ntp'
	app.loadProject(newNatronProject)