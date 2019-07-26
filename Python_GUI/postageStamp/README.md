# postageStamp

Create a PostageStamp for any node.

### HOW TO USE IT

* Tools -> Generate -> PostageStamp

### RESULT

* Create a PostageStamp for any node.

### INSTALLATION

* Copy 'postageStamp' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'postageStamp' folder.

```
from <path>.postageStamp.postageStamp import *
NatronGui.natron.addMenuCommand('Tools/Generate/PostageStamp','postageStamp')