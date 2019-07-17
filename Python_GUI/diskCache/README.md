# diskCache

Creates and process a 'DiskCache' node for the selected node.

### HOW TO USE IT

* Select a node.
* Render -> Disk Cache
* Set In and Out.
* Click 'OK.'

### RESULT

* A DiskCache is connected to the selected node, and processed for the user frame range.

### SHORTCUT

* Alt+D

### INSTALLATION

* Copy 'diskCache' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'diskCache' folder.

```
from <path>.diskCache.diskCache import *
NatronGui.natron.addMenuCommand('Render/Disk cache','diskCache()', QtCore.Qt.Key.Key_D, QtCore.Qt.KeyboardModifier.AltModifier)
```
