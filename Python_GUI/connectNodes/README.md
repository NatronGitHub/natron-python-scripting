# connectNodes

Connects nodes to another one in the Node Graph.

### HOW TO USE IT

* Select node(s).
* Select a final node.
* Edit -> Connect nodes

### RESULT

* Selected node(s) get connected to the last selected one.

### SHORTCUT

* Y

### INSTALLATION

* Copy 'connectNodes' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'connectNodes' folder.

```
from <path>.connectNodes.connectNodes import *
NatronGui.natron.addMenuCommand('Edit/Connect nodes','connectNodes', QtCore.Qt.Key.Key_Y, QtCore.Qt.KeyboardModifier)
```
