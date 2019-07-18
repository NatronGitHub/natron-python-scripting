# rotoLink

Links a roto node to a tracker.

### HOW TO USE IT

* Select a Roto node.
* Tools -> Other -> Link roto to tracker

### RESULT

* Roto is linked to the tracker.

### INSTALLATION

* Copy 'rotoLink' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'rotoLink' folder.

```
from <path>.rotoLink.rotoLink import *
NatronGui.natron.addMenuCommand('Tools/Other/Link roto to tracker','rotoLink', QtCore.Qt.Key.Key_L, QtCore.Qt.KeyboardModifier.ControlModifier | QtCore.Qt.ShiftModifier)
```