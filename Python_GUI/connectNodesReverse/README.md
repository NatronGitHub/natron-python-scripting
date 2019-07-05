# connectNodesReverse

Connects one node to another in the Node Graph.

### HOW TO USE IT

* Select many nodes.
* Select a final node.
* Tools -> Node Graph -> Connect nodes Reverse

### RESULT

* Selected nodes get connected to the last one.

### SHORTCUT

* Alt+Y

### INSTALLATION

* Copy 'connectNodesReverse' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'connectNodesReverse' folder.

```
from <path>.connectNodesReverse.connectNodesReverse import *
NatronGui.natron.addMenuCommand('Tools/Node Graph/Connect nodes reverse','connectNodesReverse()', QtCore.Qt.Key.Key_D, QtCore.Qt.KeyboardModifier.AltModifier)
```
