# autoReconnect

Reconnects node "foo" to the node "bar" when the Label (or userTextArea) of "foo" is the text string "bar"
This is useful for 3D compositing to copy paste parts of the node tree while keeping connections with the various 3D passes

### HOW TO USE IT

* Select node(s) with proper Labels corresponding to existing node names.
* Edit -> Reconnect nodes

### RESULT

* Reconnect selected node(s) to their "parent".

### SHORTCUT

* Shift+Y

### INSTALLATION

* Copy 'autoReconnect' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'reconnectNodes' folder.

```
from <path>.autoReconnect.autoReconnect import *
NatronGui.natron.addMenuCommand('Edit/Auto Reconnect Nodes','reconnectNodes', QtCore.Qt.Key.Key_Y, QtCore.Qt.KeyboardModifier.AltModifier)
```
