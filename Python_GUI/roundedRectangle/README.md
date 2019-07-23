# roundedRectangle

Create a full frame size rounded triangle.

### HOW TO USE IT

* Tools -> Roto -> Rounded rectangle
* Enter hardness value

### RESULT

* A Roto node with a full frame size rounded triangle.

### INSTALLATION

* Copy 'roundedRectangle' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'roundedRectangle' folder.

```
from <path>.roundedRectangle.roundedRectangle import *
NatronGui.natron.addMenuCommand('Tools/Roto/Rounded rectangle','roundedRectangle()')
```