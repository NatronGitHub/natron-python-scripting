#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 17/01/2018.

import os
import string
from NatronEngine import*
from os import*

# SET UP PROJECT DEFAULT SETTINGS #

def setProjectSettings(app):
	app.getProjectParam('outputFormat').setValue("HD 1920x1080")
	app.getProjectParam('autoPreviews').setValue(True)
	app.getProjectParam('frameRange').setValue(1, 25)
	app.getProjectParam('lockRange').setValue(True)
	app.getProjectParam('frameRate').setValue(25)
	app.getProjectParam('gpuRendering').setValue('Enabled')

setProjectSettings(app)