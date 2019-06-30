#This Source Code Form is subject to the terms of the Mozilla Public
#License, v. 2.0. If a copy of the MPL was not distributed with this
#file, You can obtain one at http://mozilla.org/MPL/2.0/. */
#Created by Fabrice Fernandez on 30/06/2019.


import NatronEngine


# ADDS 'DEPTH' LAYER #

def addDepthLayer(app):

    depthPlane = NatronEngine.ImageLayer( "Depth" , "Depth" , "Z")
    app.addProjectLayer( depthPlane )