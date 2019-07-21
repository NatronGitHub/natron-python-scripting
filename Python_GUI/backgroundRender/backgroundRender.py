#WINDOWS : where natron -> trouver le dossier d'installation
#LINUX : which natron

#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 29/06/2019.


import os
import sys
import stat
import codecs
import string
import shutil
import datetime
import subprocess

import NatronEngine
from NatronGui import *
from PySide.QtGui import *


# BATCH RENDER #

def backgroundRender():

	app = natron.getGuiInstance(0)
	dialog = app.createModalDialog()

	# set dialog title #
	dialog.setWindowTitle("Batch render")

	# set dialog margins #
	dialog.setContentsMargins(0, 0, 10, 10)

	# set window size #
	dialog.setFixedSize( 340, 150 )

	########################### UI CREATION ###################################

	# separators #
	line01 = dialog.createStringParam("line01","")
	line01.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line02 = dialog.createStringParam("line02","")
	line02.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

	# CREATE CHOICE LIST #
	rangeList = dialog.createChoiceParam("rangeChoice","Frame Range : ")
	rangeList.addOption('Project','')
	rangeList.addOption('Custom','')

	# CREATE WRITE LIST #
	writeList = dialog.createChoiceParam("writeChoice","Write : ")
	writeList.setAddNewLine(False)

	# if a viewer exists in comp, add it to the choice list #
	app.selectAllNodes()
	selectedNodes = app.getSelectedNodes()

	for currentNode in selectedNodes:
		currentID = currentNode.getPluginID()

		if currentID == 'fr.inria.built-in.Viewer':
			currentLabel = currentNode.getLabel()
			rangeList.addOption(str(currentLabel),'')

		if currentID == 'fr.inria.built-in.Write':
			currentLabel = currentNode.getLabel()
			writeList.addOption(str(currentLabel),'')


	app.clearSelection()
	
	rangeList.setDefaultValue('Project')
	rangeList.restoreDefaultValue()

	# separators #
	line03 = dialog.createStringParam("line03","")
	line03.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
	line04 = dialog.createStringParam("line04","")
	line04.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

 	# IN parameter #
	inRange = dialog.createIntParam("inRange","Start Frame : ")

 	# OUT parameter #
	outRange = dialog.createIntParam("outRange","End Frame : ")
	outRange.setAddNewLine(False)

	###########################################################################

	dialog.refreshUserParamsGUI()


	# user press OK button 
	if dialog.exec_():

		################################################

		os.write( 1,'\n')
		os.write( 1,'###############################################')
		os.write( 1,'\n')
		os.write( 1,'#############  BACKGROUND RENDER  #############')
		os.write( 1,'\n')
		os.write( 1,'###############################################')
		os.write( 1,'\n')
		os.write( 1,'\n')

		# grab current project path #
		projectPath = app.getProjectParam('projectPath').get()

		if projectPath == '':
			warning = natron.warningDialog("Warning","Save project first.")

		else :

			#############################################################
			#####################  SAVE NEW PROJECT #####################
			#############################################################

			# go to project path #
			os.chdir(projectPath)
			cwd = os.getcwd()

			# grab current project name #
			projectName = app.getProjectParam('projectName').get()

			# grab current project name without the .ntp extension #
			projectNameNoExt = os.path.splitext(projectName)[0]

			# get date and time #
			currentDT = datetime.datetime.now()
			date = currentDT.strftime("%Y-%m-%d_%Hh-%Mmin-%Ssec")

			# set new project name #
			newProjectName = str(projectNameNoExt) + '_' + str(date) + '.ntp'

			os.write( 1,'\n')
			os.write( 1, 'Rendered project is : ' + str(newProjectName) )
			os.write( 1,'\n')
			os.write( 1,'\n')

			# create temp folder #
			tempFolder = str(projectPath) + 'bgRenderTemp'

			if os.path.exists(tempFolder):
				pass
			else:
				os.makedirs(tempFolder)

				os.write( 1,'\n')
				os.write( 1, 'Temp folder created : ' + str(tempFolder))
				os.write( 1,'\n')
				os.write( 1,'\n')

			# copy current project in temp folder #
			shutil.copy(projectName,tempFolder)

			# rename project in temp folder #
			newProjectOldName = str(tempFolder) + '/' + str(projectName)
			newProjectNewName = str(tempFolder) + '/' + str(newProjectName)

			os.rename(newProjectOldName,newProjectNewName)


			###############################################################
			##################  GET NATRON INSTALL FOLDER #################
			###############################################################

			natronFolder = os.path.dirname((sys.executable))

			###############################################################

			# get range user choice #
			rangeUserChoice = rangeList.get()
		
			# 'Project' is selected #
			if rangeUserChoice == 0 :

				# get project frame range #
				frameRange = app.getProjectParam('frameRange').get()
				inFrame = frameRange[0]
				outFrame = frameRange[1]

				renderRange = str(inFrame) + '-' + str(outFrame)

				os.write( 1,'\n')
				os.write( 1,'Project frame range selected : ' + str(inFrame) + '-' + str(outFrame) )
				os.write( 1,'\n')
				os.write( 1,'\n')

			# 'Custom' is selected #
			if rangeUserChoice == 1 :
				
				# get user frame range #
				inFrame = inRange.get()
				outFrame = outRange.get()

				renderRange = str(inFrame) + '-' + str(outFrame)

				os.write( 1,'\n')
				os.write( 1, 'Custom frame range selected : ' + str(inFrame) + '-' + str(outFrame) )
				os.write( 1,'\n')
				os.write( 1,'\n')

			# a 'Viewer' is selected #
			if rangeUserChoice >1 :

				# we grab selected 'viewer' #
				viewerChoice = rangeList.getOption(rangeUserChoice)

				# select all nodes in Node Graph #
				app.selectAllNodes()
				selectedNodes = app.getSelectedNodes()

				# cycle through every selected nodes #
				for currentNode in selectedNodes:

					# get current node ID #
					currentID = currentNode.getPluginID()

					# if the current node's ID is of 'viewer' type #
					if currentID == 'fr.inria.built-in.Viewer':

						# then we grab its 'label' #
						viewerLabel = currentNode.getLabel()

						# select it #
						myViewer = app.getViewer(viewerLabel)

						# get its frame range #
						currentRange = myViewer.getFrameRange()
						inFrame = currentRange[0]
						outFrame = currentRange[1]

						renderRange = str(inFrame) + '-' + str(outFrame)

						os.write( 1,'\n')
						os.write( 1, str(viewerLabel) + ' frame range selected : ' + str(inFrame) + '-' + str(outFrame) )
						os.write( 1,'\n')
						os.write( 1,'\n')

						app.clearSelection()

			# get Write user choice #
			writeUserChoiceIndex = writeList.get()

			if writeUserChoiceIndex == '':
				warning = natron.warningDialog("Warning","Create a 'Write' node first.")
			else:
				writeUserChoiceLabel = writeList.getOption(writeUserChoiceIndex)

				app.selectAllNodes()
				selectedNodes = app.getSelectedNodes()

				for currentNode in selectedNodes:
					currentLabel = currentNode.getLabel()

					if currentLabel == writeUserChoiceLabel:
						fileRenderPath = currentNode.getParam('filename').get()

				app.clearSelection()

				# go to temp folder #
				os.chdir(tempFolder)

				# Windows #
				if natron.isWindows() == 1 :

					# set batch file name #
					batchFileName = str(projectNameNoExt) + '_' + str(date) + '.bat'

					# create batch file #
					with codecs.open(batchFileName, 'w+', errors="ignore") as batchRender:

						# write instruction in batch file #
						renderInstruction = 'START ' + str(natronFolder) + '/' + 'NatronRenderer ' + str(newProjectNewName) + ' -w ' + str(writeUserChoiceLabel) + ' ' + str(fileRenderPath) + ' ' + str(renderRange)

						renderInstruction = renderInstruction.replace('/','\\')
						renderInstruction = renderInstruction.replace('Program Files','"Program Files"')

						batchRender.write('@echo off\n')
						batchRender.write(str(renderInstruction))

					# run batch file #
					currentRender = subprocess.call(batchFileName)

				# Linux/OSX #
				if natron.isLinux() == 1 or natron.isMacOSX() == 1:

					# set batch file name #
					batchFileName = str(projectNameNoExt) + '_' + str(date) + '.bash'

					# create batch file #
					with codecs.open(batchFileName, 'w+', errors="ignore") as batchRender:

						# write instruction in batch file #
						renderInstruction = './' + str(natronFolder) + '/' + 'NatronRenderer ' + str(newProjectNewName) + ' -w ' + str(writeUserChoiceLabel) + ' ' + str(fileRenderPath) + ' ' + str(renderRange)

						batchRender.write('#!/bin/bash\n')
						batchRender.write(str(renderInstruction))

						# make bash file executable #
						os.chmod(batchFileName,stat.S_IRWXU)

					# run batch file #
					currentRender = subprocess.call(batchFileName)

