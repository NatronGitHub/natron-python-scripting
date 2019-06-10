#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 17/01/2018.

import os
import string
from NatronEngine import*
from os import*

# LISTS NATRON PYPLUGS #

def listPyPlugs():
	fileList = []
	folderCount = 0
	fileCount = 0

	myPath = natron.getNatronPath()
	listIndex = 0

	for p in myPath:
		currentPath = myPath[listIndex]
		folderCount += 1
		fileList.append('\n' + '\n' + '- IN [ ' + p + ' ] :' + '\n')	

		for root, subFolders, files in os.walk(currentPath):
			for file in files:
				filename1 ="init.py"
				filename2 = 'initGui.py'
				filename3 = "__init__.py"
				if file != filename1 :
					if file != filename2 :
						if file != filename3 :
							fileList = sorted(fileList)
							if file.endswith(".py") :
								file = file[:-3]
								fileList.append( '   + ' + file )
								fileCount +=1
		listIndex += 1
		

	print ('\n'.join(fileList))
	pyplugCount = fileCount - folderCount
	print ('\n' + '\n' + '- ' + str(pyplugCount) + ' PYPLUGs AVAILABLE ON THE SYSTEM')

