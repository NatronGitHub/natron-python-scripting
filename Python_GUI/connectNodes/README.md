# connectNodes

Connects one node to another in the Node Graph.

### HOW TO USE IT

* Select the first node.
* Select the second node.
* Tools -> Node Graph -> Connect nodes

### RESULT

* First node is connected to the second if possible.

### SHORTCUT

* Y

### INSTALLATION

* Copy 'connectNodes' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'connectNodes' folder.

```
from <path>.connectNodes.connectNodes import *
NatronGui.natron.addMenuCommand('Tools/Render/Disk Cache','connectNodes()', QtCore.Qt.Key.Key_D, QtCore.Qt.KeyboardModifier.AltModifier)
```
