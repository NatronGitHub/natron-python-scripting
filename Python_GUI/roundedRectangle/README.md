# roundedRectangle

Create a full frame size rounded rectangle.

### HOW TO USE IT

* Tools -> Roto -> Rounded rectangle
* Enter hardness value

### RESULT

* A Roto node with a full frame size rounded rectangle.

### INSTALLATION

* Copy 'roundedRectangle' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'roundedRectangle' folder.

```
from <path>.roundedRectangle.roundedRectangle import *
NatronGui.natron.addMenuCommand('Tools/Roto/Rounded rectangle','roundedRectangle()')
```