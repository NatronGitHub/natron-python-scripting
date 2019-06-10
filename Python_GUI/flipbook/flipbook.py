#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 09/06/2019.

import os
import sys
import subprocess

from NatronEngine import*
from NatronGui import *
from PySide.QtGui import *

import NatronGui
import NatronEngine


# RENDERS AND PLAYS THE SELECTED NODE IN AN EXTERNAL VIEWER #

def flipbook():

	# creates dialog window #
	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# creates UI #
	line01 = dialog.createStringParam("sep01","")
	line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line02 = dialog.createStringParam("sep02","")
	line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	sep01 = dialog.createSeparatorParam("line03","Flipbook")

	line03 = dialog.createStringParam("sep03","")
	line03.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line04 = dialog.createStringParam("sep04","")
	line04.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	
	# creates In/Out user parameters #
	firstFrame = dialog.createIntParam("firstFrame","In :")
	defaultFirstFrame = app.getProjectParam('frameRange').get()[0]
	firstFrame.set(defaultFirstFrame)

	lastFrame = dialog.createIntParam("lastFrame","Out :")
	defaultLastFrame = app.getProjectParam('frameRange').get()[1]
	lastFrame.set(defaultLastFrame)

	lastFrame.setAddNewLine(False)

	line05 = dialog.createStringParam("sep05","")
	line05.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	sep02 = dialog.createSeparatorParam("line02","")

	# creates formats list #
	formatList = dialog.createChoiceParam("choice01","Format : ")
	entries = [ ("exr", ""),("jpg", ""),("png", "") ]
	formatList.setOptions(entries)
	formatList.setDefaultValue("exr")
	formatList.restoreDefaultValue()

	# creates image viewers list #
	playerList = dialog.createChoiceParam("choice02","Players : ")
	playerList.setAddNewLine(False)
	entries = [ ("DJV", ""),("mrViewer", "") ]
	playerList.setOptions(entries)
	playerList.setDefaultValue("mrViewer")
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

			# if more than 1 node have been selected, stop the process #
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
				diskWrite.setLabel('diskWrite_' + str(parentLabel))

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

					# rebuild render path #
					folderPath = str(myUserPath) + '/' + '.Natron/' + 'Temp/' + str(parentLabel)

					# check if output folder exists #
					if not os.path.exists(folderPath):
						os.makedirs(folderPath)

					# rebuild full render path + filename #
					myPath = str(folderPath) + '/' + str(parentLabel) + '.######.' + str(extension)


				# ---------------------------------------------------- #
				# ---------------------- Windows --------------------- #
				# ---------------------------------------------------- #
				if natron.isWindows() == 1 :

					# get diskCachePath from Preferences #
					userDiskCachePath = NatronEngine.natron.getSettings().getParam('diskCachePath').get()

					# rebuild render path #
					if userDiskCachePath == '':
						# if diskCachePath is empty (default) #
						folderPath = str(myUserPath) + '\\AppData\\Local\\INRIA\\Natron\\flipbook_Cache\\' + str(parentLabel)
					else :
						# if diskCachePath is set to a custom folder #
						folderPath = str(userDiskCachePath) + '\\flipbook_Cache\\' + str(parentLabel)

					# check if output folder exists #
					if not os.path.exists(folderPath):
						os.makedirs(folderPath)

					# rebuild full render path + filename #
					myPath = str(folderPath) + '\\' + str(parentLabel) + '.######.' + str(extension)

					# select which player to use #
					myPlayer = playerList.getValue()
					if myPlayer == 0:
						viewerPath = ''.join(file( str(myUserPath) + '/.Natron/Python_GUI/flipbook/WIN_DJV.txt'))
						currentViewer = 'djv_view.exe'
					if myPlayer == 1:
						viewerPath = ''.join(file( str(myUserPath) + '/.Natron/Python_GUI/flipbook/WIN_mrViewer.txt'))
						currentViewer = 'mrViewer.exe'


				# ---------------------------------------------------- #
				# ---------------------- Mac OSX --------------------- #
				# ---------------------------------------------------- #
				if natron.isMacOSX() == 1 :


					# rebuild render path #
					folderPath = str(myUserPath) + '/' + '.Natron/' + 'Temp/' + str(parentLabel)

					# check if output folder exists #
					if not os.path.exists(folderPath):
						os.makedirs(folderPath)

					# rebuild full render path + filename #
					myPath = str(folderPath) + '/' + str(parentLabel) + '.######.' + str(extension)



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
				consoleMessage = str(parentLabel) + '.' + newDigits1 + str(newFirstFrame) + '-' + newDigits2 + str(newLastFrame) + '.' + str(extension)
				print 'Launching [ ' + str(consoleMessage) +  ' ] in DJV'
				print userDiskCachePath
				# go to viewer folder #
				os.chdir(viewerPath)

				# launch external viewer #
				subprocess.Popen( currentViewer + ' ' + str(folderPath) + '\\' + str(consoleMessage) , stdin = subprocess.PIPE, stdout = subprocess.PIPE)

				# suppress Write node #
				# diskWrite.destroy()