# nodeBold_HTML

Set selected nodes to be displayed in bold in the Node Graph.

### HOW TO USE IT

* Select nodes.
* Edit -> Bold Nodes <HTML>

### RESULT

* Selected nodes are displayed in bold in the Node Graph.

### INSTALLATION

* Copy 'nodeBold_HTML' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'nodeBold_HTML' folder.

```
from <path>.nodeBold_HTML.nodeBold_HTML import *
NatronGui.natron.addMenuCommand('Edit/Bold node','nodeBold_HTML')
```