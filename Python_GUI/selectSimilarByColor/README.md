# selectSimilarByColor

All nodes of the selected color will be selected in the Node Graph.

### HOW TO USE IT

* Select a node
* Edit -> Select similar -> Color

### RESULT

* All nodes of the same color will be selected in the Node Graph.

### INSTALLATION

* Copy 'selectSimilarByColor' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'selectSimilarByColor' folder.

```
from <path>.selectSimilarByColor.selectSimilarByColor import *
NatronGui.natron.addMenuCommand('Tools/Edit/Select similar/Color','selectSimilarByColor()')
```