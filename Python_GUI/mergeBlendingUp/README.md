# mergeBlendingUp

Cycles through 'Merge' blending modes upward.

### HOW TO USE IT

* Select 'Merge' nodes.
* Tools -> Node Graph -> Blending mode-

### RESULT

* Cycles through 'Merge' blending nodes.

### INSTALLATION

* Copy 'mergeBlendingUp' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'mergeBlendingUp' folder.

```
from <path>.mergeBlendingUp.mergeBlendingUp import *
NatronGui.natron.addMenuCommand('Tools/Other/Blending mode+','mergeBlendingUp')