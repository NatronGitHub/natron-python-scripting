# fullEllipse

Create a full frame size ellipse.

### HOW TO USE IT

* Tools -> Roto -> Full ellipse

### RESULT

* A Roto node with a full frame size ellipse is created.

### INSTALLATION

* Copy 'fullEllipse' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'fullEllipse' folder.

```
from <path>.fullEllipse.fullEllipse import *
NatronGui.natron.addMenuCommand('Tools/Roto/Full ellipse','fullEllipse()')
```