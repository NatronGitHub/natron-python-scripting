# nodeColorChange

Sets node color for selected nodes.

### HOW TO USE IT

* Select nodes.
* Tools -> Node Graph -> Node(s) Color
* Choose a color in the color dialog box.
* Click 'OK'.

### RESULT

* Selected nodes have their color changed.

### INSTALLATION

* Copy 'nodeColorChange' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'nodeColorChange' folder.

```
from <path>.nodeColorChange.nodeColorChange import *
NatronGui.natron.addMenuCommand('Edit/Node(s) color','nodeChangeColor')
```
