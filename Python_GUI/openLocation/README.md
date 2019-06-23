# openLocation

Opens 'Read' or 'Write' location folder in explorer.

### HOW TO USE IT

* Select 'Read' nodes.
* Tools -> Node Graph -> Open Location

### RESULT

* Opens 'Read' or 'Write' location folder in explorer.

### SHORTCUT

* Alt+O

### INSTALLATION

* Copy 'openLocation' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'openLocation' folder.

```
from <path>.openLocation.openLocation import *
NatronGui.natron.addMenuCommand('Tools/Node Graph/Open Location','openLocation', QtCore.Qt.Key.Key_O, QtCore.Qt.KeyboardModifier.AltModifier)