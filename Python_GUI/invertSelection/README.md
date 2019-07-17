# invertSelection

Invert selection in the Node Graph.

### HOW TO USE IT

* Select node(s).
* Edit -> Invert selection

### RESULT

* Node selection gets inverted.

### INSTALLATION

* Copy 'invertSelection' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'invertSelection' folder.

```
from <path>.invertSelection.invertSelection import *
NatronGui.natron.addMenuCommand('Edit/Invert selection','invertSelection')
```
