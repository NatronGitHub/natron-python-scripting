#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 28/06/2019.

import os
import codecs
import string
import NatronEngine


# SET NATRON PREFERENCES #

def getParamFromFile(keyword,file):
	param = ''
	for line in file:
		if keyword in line:
			param = line.replace(keyword,'')
			return param


def setPreferences():

	# get user folder path #
	userPath = os.path.expanduser('~')

	# we go to the '.Natron' folder #
	os.chdir(userPath + '/.Natron')

	# if the 'preferences.txt' file exists #
	if os.path.exists('preferences.txt'):

		# print console message #
		print ('- User preferences loaded from : '+ userPath + '/.Natron/preferences.txt')

		# open the 'preferences.txt' file #
		with codecs.open('preferences.txt', 'r', errors="ignore") as preferencesFile:


			#########################################
			#										#
			#             SET  PREFERENCES          #
			#										#
			#########################################

			#----------------GENERAL----------------#

			# 'Always check for updates on start-up' #
			newParam = getParamFromFile('[Check updates]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('checkForUpdates')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Auto-save trigger delay' #
			newParam = getParamFromFile('[Auto-save delay]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('autoSaveDelay')
			currentParam.set(int(newParam))

			del newParam
			del currentParam


			# 'Enable Auto-save for unsaved projects' #
			newParam = getParamFromFile('[Enable Auto-save]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('autoSaveUnSavedProjects')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Appear to plug-ins as' #
			newParam = getParamFromFile('[Appear to plug-ins as]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('pluginHostName')

			if newParam == 'Natron':
				currentParam.set(0)

			if newParam == 'Nuke':
				currentParam.set(1)

			if newParam == 'Fusion':
				currentParam.set(2)

			if newParam == 'Sony Catalyst Edit':
				currentParam.set(3)

			if newParam == 'Sony Vegas':
				currentParam.set(4)

			if newParam == 'Toxik':
				currentParam.set(5)

			if newParam == 'Scratch':
				currentParam.set(6)

			if newParam == 'Dust Buster':
				currentParam.set(7)

			if newParam == 'Da Vinci Resolve':
				currentParam.set(8)

			if newParam == 'Da Vinci Resolve Lite':
				currentParam.set(9)

			if newParam == 'SGO Mistika':
				currentParam.set(10)

			if newParam == 'Quantel Pablo Rio':
				currentParam.set(11)

			if newParam == 'IDT Motion Studio':
				currentParam.set(12)

			if newParam == 'Shake':
				currentParam.set(13)

			if newParam == 'Baselight':
				currentParam.set(14)

			if newParam == 'FrameCycler':
				currentParam.set(15)

			if newParam == 'Nucoda Film Master':
				currentParam.set(16)

			if newParam == 'Avid DS':
				currentParam.set(17)

			if newParam == 'China Digital Video DX':
				currentParam.set(18)

			if newParam == 'NewBlueFX Titler Pro':
				currentParam.set(19)

			if newParam == 'NewBlueFX OFX Bridge':
				currentParam.set(20)

			if newParam == 'Ramen':
				currentParam.set(21)

			if newParam == 'TuttleOFX':
				currentParam.set(22)

			if newParam == 'Custom host name':
				currentParam.set(23)

			del newParam
			del currentParam


			#----------------THREADING----------------#

			# 'Number of render threads' #
			newParam = getParamFromFile('[Number render threads]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('noRenderThreads')
			currentParam.set(int(newParam))

			del newParam
			del currentParam


			# 'Number of parallel renders' #
			newParam = getParamFromFile('[Number parallel renders]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('nParallelRenders')
			currentParam.set(int(newParam))

			del newParam
			del currentParam


			# 'Effects use the thread-pool' #
			newParam = getParamFromFile('[Effect thread-pool]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('useThreadPool')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Max threads usable per effect' #
			newParam = getParamFromFile('[Max threads]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('nThreadsPerEffect')
			currentParam.set(int(newParam))

			del newParam
			del currentParam


			# 'Render in a separate process' #
			newParam = getParamFromFile('[Render separate process]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('renderNewProcess')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Append new renders to queue' #
			newParam = getParamFromFile('[Append render to queue]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('queueRenders')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			#----------------THREADING----------------#

			# 'Convert NaN values' #
			newParam = getParamFromFile('[Convert NaN values]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('convertNaNs')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Copy input image before rendering any plug-in' #
			newParam = getParamFromFile('[Copy input image]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('copyInputImage')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam



			# 'RGB components support' #
			newParam = getParamFromFile('[RGB components support]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('rgbSupport')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam



			# 'Transforms concatenation support' #
			newParam = getParamFromFile('[Concatenation support]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('transformCatSupport')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam



			#----------------GPU RENDERING----------------#


			# 'No. of OpenGL Contexts' #
			newParam = getParamFromFile('[No OpenGL contexts]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('maxOpenGLContexts')
			currentParam.set(int(newParam))

			del newParam
			del currentParam


			# 'OpenGL Rendering' #
			newParam = getParamFromFile('[OpenGL rendering]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('enableOpenGLRendering')

			if newParam == 'Enabled':
				currentParam.set(0)

			if newParam == 'Disabled':
				currentParam.set(1)

			if newParam == 'Disabled If Background':
				currentParam.set(2)


			del newParam
			del currentParam

			
			#----------------PROJECT SETUP----------------#

			# 'First image read set project format' #
			newParam = getParamFromFile('[First image read]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('autoProjectFormat')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Auto-preview enabled by default for new projects' #
			newParam = getParamFromFile('[Auto-preview]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('enableAutoPreviewNewProjects')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Auto fix relative file-paths' #
			newParam = getParamFromFile('[Fix file-paths]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('autoFixRelativePaths')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam



			# 'Use drive letters instead of server names (Windows only)' #
			if NatronEngine.natron.isWindows() == 1 :

				newParam = getParamFromFile('[Use drive letters]: ', preferencesFile)
				currentParam = NatronEngine.natron.getSettings().getParam('useDriveLetters')

				if 'False' in newParam:
					currentParam.set(0)
				if 'True' in newParam:
					currentParam.set(1)

				del newParam
				del currentParam


			#----------------DOCUMENTATION----------------#


			# 'Documentation source' #
			newParam = getParamFromFile('[Doc source]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('documentationSource')

			if newParam == 'Local':
				currentParam.set(0)

			if newParam == 'Online':
				currentParam.set(1)

			if newParam == 'None':
				currentParam.set(2)

			del newParam
			del currentParam


			# 'Documentation local port' #
			newParam = getParamFromFile('[Doc port]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('webserverPort')
			currentParam.set(int(newParam))

			del newParam
			del currentParam


			#----------------USER INTERFACE----------------#

			# 'Warn when a file changes externally' #
			newParam = getParamFromFile('[Warn file change]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('warnOnExternalChange')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Promp with file dialog when creating a Write node' #
			newParam = getParamFromFile('[Prompt Write node]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('writeUseDialog')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Refresh viewer only when editing is finished' #
			newParam = getParamFromFile('[Refresh viewer]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('renderOnEditingFinished')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Linear color pickers' #
			newParam = getParamFromFile('[Linear color pickers]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('linearPickers')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Maximum number of open settings panels' #
			newParam = getParamFromFile('[Max panels]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('maxPanels')
			currentParam.set(int(newParam))

			del newParam
			del currentParam


			# 'Value increments based on cursor position' #
			newParam = getParamFromFile('[Value increments]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('cursorPositionAwareFields')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Load workspace embedded within projects' #
			newParam = getParamFromFile('[Load workspace]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('loadProjectWorkspace')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			#----------------COLOR MANAGEMENT----------------#


			# 'Documentation source' #
			newParam = getParamFromFile('[OCIO config]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('ocioConfig')

			if newParam == 'blender':
				currentParam.set(0)

			if newParam == 'natron':
				currentParam.set(1)

			if newParam == 'nuke-default':
				currentParam.set(2)

			if newParam == 'Custom config':
				currentParam.set(3)

			del newParam
			del currentParam


			# 'Load workspace embedded within projects' #
			newParam = getParamFromFile('[OCIO changed]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('warnOCIOChanged')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Load workspace embedded within projects' #
			newParam = getParamFromFile('[OCIO not default]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('startupCheckOCIO')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			#----------------CACHING----------------#


			# 'Aggressive caching' #
			newParam = getParamFromFile('[Aggressive caching]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('aggressiveCaching')

			if 'False' in newParam:
				currentParam.set(0)
			if 'True' in newParam:
				currentParam.set(1)

			del newParam
			del currentParam


			# 'Maximum amount of RAM memory used for caching' #
			newParam = getParamFromFile('[Caching RAM]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('maxRAMPercent')
			currentParam.set(int(newParam))

			del newParam
			del currentParam



			# 'System RAM to keep free' #
			newParam = getParamFromFile('[Free RAM]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('unreachableRAMPercent')
			currentParam.set(int(newParam))

			del newParam
			del currentParam


			# 'System RAM to keep free' #
			newParam = getParamFromFile('[Max playback]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('maxViewerDiskCache')
			currentParam.set(int(newParam))

			del newParam
			del currentParam


			# 'System RAM to keep free' #
			newParam = getParamFromFile('[Max diskcache]: ', preferencesFile)
			currentParam = NatronEngine.natron.getSettings().getParam('maxDiskCacheNode')
			currentParam.set(int(newParam))

			del newParam
			del currentParam





















	else:
		pass

		# save settings #
	NatronEngine.natron.getSettings().saveSettings()