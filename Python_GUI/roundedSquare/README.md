# roundedSquare

Create a full frame size rounded square.

### HOW TO USE IT

* Tools -> Roto -> Rounded rectangle
* Enter hardness value

### RESULT

* A Roto node with a full frame size rounded square.

### INSTALLATION

* Copy 'roundedSquare' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'roundedSquare' folder.

```
from <path>.roundedSquare.roundedSquare import *
NatronGui.natron.addMenuCommand('Tools/Roto/Rounded square','roundedSquare()')
```