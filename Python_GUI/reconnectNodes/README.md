# reconnectNodes

Reconnects nodes to another one in the Node Graph.

### HOW TO USE IT

* Select node(s).
* Edit -> Reconnect nodes

### RESULT

* Reconnect selected node(s).

### SHORTCUT

* Alt+Y

### INSTALLATION

* Copy 'reconnectNodes' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'reconnectNodes' folder.

```
from <path>.reconnectNodes.reconnectNodes import *
NatronGui.natron.addMenuCommand('Edit/Reconnect nodes','reconnectNodes', QtCore.Qt.Key.Key_Y, QtCore.Qt.KeyboardModifier.AltModifier)
```
