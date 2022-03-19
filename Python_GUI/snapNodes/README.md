# snapNodes
contains multiple nodegraph cleaning scripts

snapNodes:
snap Nodes on a grid in the nodegraph

alignNodes:
align Nodes on on their average x or y position

spreadNodes:
This script regularly spaces nodes  between leftmost-rightmost nodes (or lowest-highest)
It can optionally snap them onto the same grid as snapNodes
This script can be used to separate nodes that are stacked one onto the other.


### HOW TO USE IT

* Select node(s)
* Tools -> Node Graph -> snap Nodes or shortcut 'A'
* Tools -> Node Graph -> align Nodes X
* Tools -> Node Graph -> align Nodes Y
* Tools -> Node Graph -> Spread Nodes X
* Tools -> Node Graph -> Spread Nodes Y

### RESULT

* All selected nodes are aligned on an invisible grid

### INSTALLATION

* Copy 'snapNodes' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'snapNodes' folder.

```
from <path>.snapNodes.snapNodes import *
NatronGui.natron.addMenuCommand('Tools/Node Graph/snap Nodes','snapNodes',  QtCore.Qt.Key.Key_A,QtCore.Qt.KeyboardModifier)
NatronGui.natron.addMenuCommand('Tools/Node Graph/Align Nodes X','alignNodesX' )
NatronGui.natron.addMenuCommand('Tools/Node Graph/Align Nodes Y','alignNodesY' )
NatronGui.natron.addMenuCommand('Tools/Node Graph/Spread Nodes X','spreadNodesX' )
NatronGui.natron.addMenuCommand('Tools/Node Graph/Spread Nodes Y','spreadNodesY' )
```