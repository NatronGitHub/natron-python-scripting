# nodeItalic_HTML

Sets selected nodes to be displayed in italic in the Node Graph.

### HOW TO USE IT

* Select nodes.
* Tools -> Node Graph -> Italic Nodes <HTML>

### RESULT

* Selected nodes are displayed in italic in the Node Graph.

### INSTALLATION

* Copy 'nodeItalic_HTML' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'nodeItalic_HTML' folder.

```
from <path>.nodeItalic_HTML.nodeItalic_HTML import *
NatronGui.natron.addMenuCommand('Edit/Italic nodes <HTML>','nodeItalic_HTML')
```
