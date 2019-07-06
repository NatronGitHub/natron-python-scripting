# connectNodesList

Connects node()s to one choosen in the list.

### HOW TO USE IT

* Select many nodes.
* Tools -> Node Graph -> Connect nodes list

### RESULT

* Selected nodes get connected to the one choosen in the list.

### SHORTCUT

* Alt+Y

### INSTALLATION

* Copy 'connectNodesList' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'connectNodesList' folder.

```
from <path>.connectNodesList.connectNodesList import *
NatronGui.natron.addMenuCommand('Tools/Render/Disk Cache','connectNodesList()', QtCore.Qt.Key.Key_D, QtCore.Qt.KeyboardModifier.AltModifier)
```
