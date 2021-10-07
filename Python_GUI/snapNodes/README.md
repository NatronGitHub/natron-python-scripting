# snapNodes

snap Nodes on a grid in the nodegraph

### HOW TO USE IT

* Select node(s)
* Tools -> Node Graph -> snap Nodes or shortcut 'A'

### RESULT

* All selected nodes are aligned on an invisible grid

### INSTALLATION

* Copy 'snapNodes' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'snapNodes' folder.

```
from <path>.snapNodes.snapNodes import *
NatronGui.natron.addMenuCommand('Tools/Node Graph/snap Nodes','snapNodes',  QtCore.Qt.Key.Key_A,QtCore.Qt.KeyboardModifier)
```