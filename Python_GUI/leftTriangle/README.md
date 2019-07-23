# leftTriangle

Create a left aligned triangle.

### HOW TO USE IT

* Tools -> Roto -> Left triangle

### RESULT

* A Roto node with a left aligned triangle is created.

### INSTALLATION

* Copy 'leftTriangle' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'leftTriangle' folder.

```
from <path>.leftTriangle.leftTriangle import *
NatronGui.natron.addMenuCommand('Tools/Roto/Left Triangle','leftTriangle()')
```