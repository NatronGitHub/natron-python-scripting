# fullCircle

Create a full frame size circle.

### HOW TO USE IT

* Tools -> Roto -> Full circle

### RESULT

* A Roto node with a full frame size circle is created.

### INSTALLATION

* Copy 'fullCircle' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'fullCircle' folder.

```
from <path>.fullCircle.fullCircle import *
NatronGui.natron.addMenuCommand('Tools/Roto/Full circle','fullCircle()')
```