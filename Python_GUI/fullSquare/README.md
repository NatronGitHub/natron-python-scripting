# fullSquare

Create a full frame size rectangle.

### HOW TO USE IT

* Tools -> Roto -> Full square

### RESULT

* A Roto node with a full frame size square is created.

### INSTALLATION

* Copy 'fullSquare' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'fullSquare' folder.

```
from <path>.fullSquare.fullSquare import *
NatronGui.natron.addMenuCommand('Tools/Roto/Full square','fullSquare()')
```