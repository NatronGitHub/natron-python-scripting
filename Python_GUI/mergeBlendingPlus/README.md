# mergeBlendingPlus

Cycles through 'Merge' blending modes downward.

### HOW TO USE IT

* Select 'Merge' nodes.
* Tools -> Node Graph -> Blending mode+

### RESULT

* Cycles through 'Merge' blending nodes.

### INSTALLATION

* Copy 'mergeBlendingPlus' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'mergeBlendingPlus' folder.

```
from <path>.mergeBlendingPlus.mergeBlendingPlus import *
NatronGui.natron.addMenuCommand('Tools/Other/Blending mode+','mergeBlendingPlus')