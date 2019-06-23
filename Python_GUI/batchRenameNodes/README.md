# batchRenameNodes

Renames selected node.

### HOW TO USE IT

* Select node(s).
* Tools -> Node Graph -> Batch rename
* Fill the fields
* Click 'OK.'

### RESULT

* Selected nodes are renamed.

### INSTALLATION

* Copy 'batchRenameNodes' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the path to the 'batchRenameNodes' folder.

```
from <path>.batchRenameNodes.batchRenameNodes import *
NatronGui.natron.addMenuCommand('Tools/Node Graph/Batch rename','batchRenameNodes')
```
