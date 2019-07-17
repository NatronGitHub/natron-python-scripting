# nodeBold_HTML

Sets selected nodes to be displayed in bold in the Node Graph.

### HOW TO USE IT

* Select nodes.
* Tools -> Node Graph -> Bold Nodes <HTML>

### RESULT

* Selected nodes are displayed in bold in the Node Graph.

### INSTALLATION

* Copy 'nodeBold_HTML' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'nodeBold_HTML' folder.

```
from <path>.nodeBold_HTML.nodeBold_HTML import *
NatronGui.natron.addMenuCommand('Tools/Node Graph/Bold nodes <HTML>','nodeBold_HTML')
```