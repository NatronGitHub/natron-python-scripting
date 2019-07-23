# rightTriangle

Create a right aligned triangle.

### HOW TO USE IT

* Tools -> Roto -> Right triangle

### RESULT

* A Roto node with a right aligned triangle is created.

### INSTALLATION

* Copy 'rightTriangle' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'rightTriangle' folder.

```
from <path>.rightTriangle.rightTriangle import *
NatronGui.natron.addMenuCommand('Tools/Roto/Right Triangle','rightTriangle()')
```