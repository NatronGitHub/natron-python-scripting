# mergeBlendingDown

Cycles through 'Merge' blending nodes.

### HOW TO USE IT

* Select 'Merge' nodes.
* Tools -> Node Graph -> Blending mode+

### RESULT

* Cycles through 'Merge' blending nodes.

### INSTALLATION

* Copy 'mergeBlendingDown' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'mergeBlendingDown' folder.

```
from <path>.mergeBlendingDown.mergeBlendingDown import *
NatronGui.natron.addMenuCommand('Tools/Other/Blending mode+','mergeBlendingDown')