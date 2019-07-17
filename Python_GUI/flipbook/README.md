# flipbook

Renders and plays the selected node in an external viewer.

### HOW TO USE IT

* Select a node.
* Tools -> Render -> flipbook
* Set In and Out.
* Select viewer app.
* Click 'OK.'

### RESULT

Creates and process a 'Write' node for the selected node. and send the result to an external image viewer.

### NOTE :

Frames are rendered in the folder specified in : Preferences -> Caching -> Disk cache path.
Default folder is :
```
- Windows : C:/Users/user/AppData/Local/INRIA/Natron/cache
- Linux : home/user/.cache/INRIA/Natron
- OSX : home/user/.cache/INRIA/Natron
```

## Windows :
* Supported viewers : djv_view - mrViewer - PdPlayer.
* paths to the .exe must be set in the WIN_DJV.txt, WIN_mrViewer.txt and WIN_PDPLAYER.txt

## Linux :
* Supported viewers : djv_view - mrViewer - PdPlayer.
* paths to binaries must be set in the LINUX_DJV.txt, LINUX_mrViewer.txt and LINUX_PDPLAYER.exe

## OSX :
* Not supported yet.

### SHORTCUT

* Alt+F


### DOWNLOADS :

* djv_view : http://djv.sourceforge.net/Download.html
* mrViewer : https://sourceforge.net/projects/mrviewer/files/
* PdPlayer : http://pdplayer.com/downloads.html

### INSTALLATION

* Copy 'flipbook' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'flipbook' folder.

```
from <path>.flipbook.flipbook import *
NatronGui.natron.addMenuCommand('Render/Flipbook','flipbook()', QtCore.Qt.Key.Key_F, QtCore.Qt.KeyboardModifier.AltModifier)
```