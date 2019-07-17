# selectSimilar

Select similar nodes.

### HOW TO USE IT

* Select a node
* Tools -> Node Graph -> Select similar

### RESULT

* All nodes of the selected type will be selected in the Node Graph .

### INSTALLATION

* Copy 'selectSimilar' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'selectSimilar' folder.

```
from <path>.selectSimilar.selectSimilar import *
NatronGui.natron.addMenuCommand('Tools/Node Graph/Select similar','selectSimilar')
```