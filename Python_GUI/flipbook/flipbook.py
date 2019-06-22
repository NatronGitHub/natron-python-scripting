#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 09/06/2019.

import os
import sys
import subprocess

#from NatronEngine import *
from NatronGui import *
from PySide.QtGui import *

#import NatronGui
import NatronEngine


# RENDERS AND PLAYS THE SELECTED NODE IN AN EXTERNAL VIEWER #

def flipbook():

	# creates dialog window #
	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Flipbook")

	# set dialog margins #
	dialog.setContentsMargins(0, 0, 10, 10)


	# ------------------------------------------------------ #
	# --------------------- UI creation -------------------- #
	# ------------------------------------------------------ #

	line01 = dialog.createStringParam("sep01","")
	line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line02 = dialog.createStringParam("sep02","")
	line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	
	# creates In/Out user parameters #
	firstFrame = dialog.createIntParam("firstFrame","In :")
	defaultFirstFrame = app.getProjectParam('frameRange').get()[0]
	firstFrame.set(defaultFirstFrame)

	lastFrame = dialog.createIntParam("lastFrame","Out :")
	defaultLastFrame = app.getProjectParam('frameRange').get()[1]
	lastFrame.set(defaultLastFrame)
	lastFrame.setAddNewLine(False)

	line03 = dialog.createStringParam("sep03","")
	line03.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	sep01 = dialog.createSeparatorParam("line01","")

	# creates formats list #
	formatList = dialog.createChoiceParam("choice01","Format : ")
	entries = [ ("exr", ""),("jpg", ""),("png", "") ]
	formatList.setOptions(entries)
	formatList.setDefaultValue("exr")
	formatList.restoreDefaultValue()

	# creates players list #
	playerList = dialog.createChoiceParam("choice02","Players : ")
	playerList.setAddNewLine(False)
	entries = [ ("DJV", ""),("mrViewer", ""),("PDPLAYER", "") ]
	playerList.setOptions(entries)
	playerList.setDefaultValue("DJV")
	playerList.restoreDefaultValue()



	# Refresh UI #
	dialog.refreshUserParamsGUI()



	# code executed when OK button is pressed #
	if dialog.exec_():

		# retrieves values entered by user #
		newFirstFrame = dialog.getParam("firstFrame").getValue()
		newLastFrame = dialog.getParam("lastFrame").getValue()

		counter = 0
		selectedNodes = app.getSelectedNodes()


		# Gives user's home directory
		myUserPath = os.path.expanduser('~')

		# Gives username by splitting path based on OS
		myUser = os.path.split(myUserPath)[-1]


		for n in selectedNodes:

			# if more than 1 node is selected, stop the process #
			if len(selectedNodes) != 1 :
				break

			else :
				# creates a diskWrite node #
				parentPosition = n.getPosition()
				diskWrite = app.createNode("fr.inria.built-in.Write")

				# connects the Disk Cache node to the selected node, and set graph position. #
				diskWrite.connectInput(0, n)

				# set node position #
				diskWrite.setPosition(parentPosition[0]+150,parentPosition[1])

				# set node name #
				parentLabel = n.getLabel()
				diskWrite.setLabel('diskWrite_' + parentLabel)

				# retrieve format choice #
				myFormat = formatList.getValue()
				extension = ''

				if myFormat == 0 :
					extension = 'exr'
				if myFormat == 1 :
					extension = 'jpg'
				if myFormat == 2 :
					extension = 'png'


				# --------------------- check OS --------------------- #

				# ---------------------------------------------------- #
				# ----------------------- Linux ---------------------- #
				# ---------------------------------------------------- #
				if natron.isLinux() == 1 :

					# get diskCachePath from Preferences #
					userDiskCachePath = NatronEngine.natron.getSettings().getParam('diskCachePath').get()

					# rebuild render path #
					if userDiskCachePath == '':
						# if diskCachePath is empty (default) #
						folderPath = str(myUserPath) + '/.cache/INRIA/Natron/flipbook_Cache/' + parentLabel
					else :
						# if diskCachePath is set to a custom folder #
						folderPath = str(userDiskCachePath) + '/flipbook_Cache/' + parentLabel

					# check if output folder exists #
					if not os.path.exists(folderPath):
						os.makedirs(folderPath)

					# rebuild full render path + filename #
					myPath = str(folderPath) + '/' + parentLabel + '.######.' + str(extension)

					# select which player to use #
					myPlayer = playerList.getValue()
					if myPlayer == 0:
						viewerPath = ''.join(file( str(myUserPath) + '/.Natron/Python_GUI/flipbook/preferences/LINUX_DJV.txt'))
						currentViewer = 'djv_view.sh'
						viewerLabel = 'DJV'
						fullViewerPath = viewerPath + currentViewer
					if myPlayer == 1:
						viewerPath = ''.join(file( str(myUserPath) + '/.Natron/Python_GUI/flipbook/preferences/LINUX_mrViewer.txt'))
						viewerLabel = 'mrViewer'
						currentViewer = 'mrViewer.sh'
						fullViewerPath = viewerPath + currentViewer
					if myPlayer == 2:
						viewerPath = ''.join(file( str(myUserPath) + '/.Natron/Python_GUI/flipbook/preferences/LINUX_mrViewer.txt'))
						viewerLabel = 'PdPlayer'
						currentViewer = 'pdplayer64'
						fullViewerPath = viewerPath + currentViewer


				# ---------------------------------------------------- #
				# ---------------------- Windows --------------------- #
				# ---------------------------------------------------- #
				if natron.isWindows() == 1 :

					# get diskCachePath from Preferences #
					userDiskCachePath = NatronEngine.natron.getSettings().getParam('diskCachePath').get()

					# rebuild render path #
					if userDiskCachePath == '':
						# if diskCachePath is empty (default) #
						folderPath = str(myUserPath) + '\\AppData\\Local\\INRIA\\Natron\\flipbook_Cache\\' + parentLabel
					else :
						# if diskCachePath is set to a custom folder #
						folderPath = str(userDiskCachePath) + '\\flipbook_Cache\\' + parentLabel

					# check if output folder exists #
					if not os.path.exists(folderPath):
						os.makedirs(folderPath)

					# rebuild full render path + filename #
					myPath = str(folderPath) + '\\' + parentLabel + '.######.' + extension

					# select which player to use #
					myPlayer = playerList.getValue()
					if myPlayer == 0:
						viewerPath = ''.join(file( str(myUserPath) + '/.Natron/Python_GUI/flipbook/preferences/WIN_DJV.txt') )
						currentViewer = 'djv_view.exe'
						viewerLabel = 'DJV'
						fullViewerPath = viewerPath.replace('\\', '\\\\') + '\\' + currentViewer
					if myPlayer == 1:
						viewerPath = ''.join(file( str(myUserPath) + '/.Natron/Python_GUI/flipbook/preferences/WIN_mrViewer.txt'))
						currentViewer = 'mrViewer.exe'
						viewerLabel = 'mrViewer'
						fullViewerPath = viewerPath.replace('\\', '\\\\') + '\\' + currentViewer
					if myPlayer == 2:
						viewerPath = ''.join(file( str(myUserPath) + '/.Natron/Python_GUI/flipbook/preferences/WIN_PDPLAYER.txt'))
						currentViewer = 'pdplayer64.exe'
						viewerLabel = 'PdPlayer'
						fullViewerPath = viewerPath.replace('\\', '\\\\') + '\\' + currentViewer


				# ---------------------------------------------------- #
				# ---------------------- Mac OSX --------------------- #
				# ---------------------------------------------------- #
				if natron.isMacOSX() == 1 :

					# get diskCachePath from Preferences #
					userDiskCachePath = NatronEngine.natron.getSettings().getParam('diskCachePath').get()

					# rebuild render path #
					if userDiskCachePath == '':
						# if diskCachePath is empty (default) #
						folderPath = str(myUserPath) + '/.cache/INRIA/Natron/flipbook_Cache/' + parentLabel
					else :
						# if diskCachePath is set to a custom folder #
						folderPath = str(userDiskCachePath) + '/flipbook_Cache/' + parentLabel

					# check if output folder exists #
					if not os.path.exists(folderPath):
						os.makedirs(folderPath)

					# rebuild full render path + filename #
					myPath = str(folderPath) + '/' + parentLabel + '.######.' + str(extension)

					# select which player to use #
					myPlayer = playerList.getValue()
					if myPlayer == 0:
						viewerPath = ''.join(file( str(myUserPath) + '/.Natron/Python_GUI/flipbook/preferences/OSX_DJV.txt'))
						currentViewer = 'djv_view.app'
						viewerLabel = 'DJV'
						fullViewerPath = viewerPath + currentViewer
					if myPlayer == 1:
						viewerPath = ''.join(file( str(myUserPath) + '/.Natron/Python_GUI/flipbook/preferences/OSX.txt'))
						viewerLabel = 'mrViewer'
						currentViewer = 'mrViewer.app'
						fullViewerPath = viewerPath + currentViewer
					if myPlayer == 2:
						viewerPath = ''.join(file( str(myUserPath) + '/.Natron/Python_GUI/flipbook/preferences/OSX.txt'))
						viewerLabel = 'pdplayer64.app'
						currentViewer = 'PdPlayer'
						fullViewerPath = viewerPath + currentViewer


				# --------------------- setup 'Write' node --------------------- #

				# set Write render path #
				oldPath = diskWrite.getParam("filename").set(myPath)

				# set Write frame range to 'Manual' #
				myFrameRange = diskWrite.getParam("frameRange").set(2)

				# set Write first frame to render #
				myFirstFrame = diskWrite.getParam("firstFrame").set(newFirstFrame)

				# set Write last frame to render #
				myLastFrame = diskWrite.getParam("lastFrame").set(newLastFrame)

				# launch render #
				app.renderBlocking(diskWrite, newFirstFrame, newLastFrame)

				fLength = len(str(newFirstFrame))
				lLength = len(str(newLastFrame))

				# rebuild leading zeros #
				newDigits1 =''
				while fLength < 6:
					newDigits1 += '0'
					fLength += 1


				newDigits2 =''
				while lLength < 6:
					newDigits2 += '0'
					lLength += 1


				# print message in console #
				fullRenderName = parentLabel + '.' + newDigits1 + str(newFirstFrame) + '-' + newDigits2 + str(newLastFrame) + '.' + str(extension)
				if myPlayer == 2:
					fullRenderName = parentLabel + '.' + '######' + '.' + str(extension)

				os.write(1, '\n' 'Opening [ ' + fullRenderName +  ' ] in ' + viewerLabel + '\n' + '\n')


				# ---------------------- launch external viewer --------------------- #

				# go to viewer folder #
				os.chdir(viewerPath)

				# Windows #
				if natron.isWindows() == 1 :
					fullRenderPath = str(folderPath) + '\\' + str(fullRenderName)
					subprocess.Popen( [fullViewerPath, fullRenderPath] , stdin = subprocess.PIPE, stdout = subprocess.PIPE)

				# Linux #
				if natron.isLinux() == 1 :
					fullRenderPath = str(folderPath) + '/' + str(fullRenderName)
					subprocess.Popen( [fullViewerPath, fullRenderPath] , stdin = subprocess.PIPE, stdout = subprocess.PIPE)

				# OSX #
				if natron.isMacOSX() == 1 :
					fullRenderPath = str(folderPath) + '/' + str(fullRenderName)
					subprocess.Popen( [fullViewerPath, fullRenderPath] , stdin = subprocess.PIPE, stdout = subprocess.PIPE)