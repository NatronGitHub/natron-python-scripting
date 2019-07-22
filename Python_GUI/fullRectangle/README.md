# fullRectangle

Sets alpha to 1 (full white) for selected 'Read' nodes.

### HOW TO USE IT

* Tools -> Roto -> Full rectangle

### RESULT

* Selected 'Read' nodes have their alpha channel set to 1 (full white).

### INSTALLATION

* Copy 'fullRectangle' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'fullRectangle' folder.

```
from <path>.fullRectangle.fullRectangle import *
NatronGui.natron.addMenuCommand('Tools/Roto/Full rectangle','fullRectangle()')
```