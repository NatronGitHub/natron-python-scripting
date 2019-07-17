# connectNodes

Connects nodes to another one in the Node Graph.

### HOW TO USE IT

* Select many nodes.
* Select a final node.
* Edit -> Connect nodes

### RESULT

* Selected nodes get connected to the last one.

### SHORTCUT

* Alt+Y

### INSTALLATION

* Copy 'connectNodes' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'connectNodes' folder.

```
from <path>.connectNodes.connectNodes import *
NatronGui.natron.addMenuCommand('Edit/Connect nodes','connectNodes', QtCore.Qt.Key.Key_Y, QtCore.Qt.KeyboardModifier)
```
