# forceCaching

Enable/disable force caching for selected nodes.

### HOW TO USE IT

* Select node(s).
* Tools -> Node Graph ->Force Caching

### RESULT

Enable/disable force caching for selected nodes.

### SHORTCUT

* Ctrl+B

### INSTALLATION

* Copy 'forceCaching' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'forceCaching' folder.

```
from <path>.forceCaching.forceCaching import *
NatronGui.natron.addMenuCommand('Tools/Node Graph/Force caching','forceCaching', QtCore.Qt.Key.Key_B, QtCore.Qt.KeyboardModifier.ControlModifier)
```