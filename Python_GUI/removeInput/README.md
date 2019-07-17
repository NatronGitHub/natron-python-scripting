# removeInput

Disconnect nodes in the Node Graph.

### HOW TO USE IT

* Select node(s).
* Edit -> Remove input

### RESULT

* Selected nodes get disconnected in the Node Graph.

### SHORTCUT

* Ctrl+D

### INSTALLATION

* Copy 'removeInput' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'removeInput' folder.

```
from <path>.removeInput.removeInput import *
NatronGui.natron.addMenuCommand('Edit/Remove input','removeInput', QtCore.Qt.Key.Key_D, QtCore.Qt.KeyboardModifier.ControlModifier)
```
