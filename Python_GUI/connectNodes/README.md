# connectNodes

Connects one or many nodes to another one in the Node Graph.

### HOW TO USE IT

* Select many nodes.
* Select a final node.
* Tools -> Node Graph -> Connect nodes

### RESULT

* Selected nodes get connected to the last one.

### SHORTCUT

* Alt+Y

### INSTALLATION

* Copy 'connectNodes' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'connectNodes' folder.

```
from <path>.connectNodes.connectNodes import *
NatronGui.natron.addMenuCommand('Tools/Render/Disk Cache','connectNodes()', QtCore.Qt.Key.Key_D, QtCore.Qt.KeyboardModifier.AltModifier)
```
