# bottomTriangle

Create a top aligned triangle.

### HOW TO USE IT

* Tools -> Roto -> Bottom triangle

### RESULT

* A Roto node with a bottom aligned triangle is created.

### INSTALLATION

* Copy 'bottomTriangle' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'bottomTriangle' folder.

```
from <path>.bottomTriangle.bottomTriangle import *
NatronGui.natron.addMenuCommand('Tools/Roto/Bottom Triangle','bottomTriangle()')
```