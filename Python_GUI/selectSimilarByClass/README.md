# selectSimilarByClass

All nodes of the selected type will be selected in the Node Graph.

### HOW TO USE IT

* Select a node
* Tools -> Edit -> Select similar -> Class

### RESULT

* All nodes of the same type in the Node Graph will be selected.

### INSTALLATION

* Copy 'selectSimilarByClass' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'selectSimilarByClass' folder.

```
from <path>.selectSimilarByClass.selectSimilarByClass import *
NatronGui.natron.addMenuCommand('Tools/Edit/Select similar/Class','selectSimilarByClass()')
```