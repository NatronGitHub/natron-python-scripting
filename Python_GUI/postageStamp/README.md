# postageStamp

Create a PostageStamp from any node.

### HOW TO USE IT

* Select node(s)
* Tools -> Generate -> PostageStamp

### RESULT

* Create a PostageStamp for any node.

### SHORTCUT

* Ctrl+Alt+P

### INSTALLATION

* Copy 'postageStamp' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'postageStamp' folder.

```
from <path>.postageStamp.postageStamp import *
NatronGui.natron.addMenuCommand('Tools/Generate/PostageStamp','postageStamp', QtCore.Qt.Key.Key_P, QtCore.Qt.KeyboardModifier.ControlModifier | QtCore.Qt.AltModifier)