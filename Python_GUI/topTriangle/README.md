# topTriangle

Create a top aligned triangle.

### HOW TO USE IT

* Tools -> Roto -> Top triangle

### RESULT

* A Roto node with a top aligned triangle is created.

### INSTALLATION

* Copy 'topTriangle' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'topTriangle' folder.

```
from <path>.topTriangle.topTriangle import *
NatronGui.natron.addMenuCommand('Tools/Roto/Top Triangle','topTriangle()')
```