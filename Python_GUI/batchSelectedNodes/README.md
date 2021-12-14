# batchSelectedNodes

batch action on selected nodes

### HOW TO USE IT

* Select node(s).
* Edit -> batch selected nodes

### RESULT

* apply the same action to each selected node

### SHORTCUT

* none

### INSTALLATION

* Copy 'batchSelectedNodes' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'batchSelectedNodes' folder.

```
from <path>.batchSelectedNodes.batchSelectedNodes import *
NatronGui.natron.addMenuCommand('Tools/Utils/Batch Selected Nodes','batchSelectedNodes')
```
