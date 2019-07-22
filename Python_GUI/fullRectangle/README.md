# fullRectangle

Create a full frame size rectangle.

### HOW TO USE IT

* Tools -> Roto -> Full rectangle

### RESULT

* A Roto node with a full frame size rectangle is created.

### INSTALLATION

* Copy 'fullRectangle' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'fullRectangle' folder.

```
from <path>.fullRectangle.fullRectangle import *
NatronGui.natron.addMenuCommand('Tools/Roto/Full rectangle','fullRectangle()')
```