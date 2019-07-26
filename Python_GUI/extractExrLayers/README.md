# extractExrLayers

Split EXR Read node into shuffle nodes.

### HOW TO USE IT

* Select an EXR Read node.
* Tools -> Channel -> Extract EXR layers

### RESULT

* Split EXR Read node into shuffle nodes.

### INSTALLATION

* Copy 'extractExrLayers' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'extractExrLayers' folder.

```
from <path>.extractExrLayers.extractExrLayers import *
NatronGui.natron.addMenuCommand('Tools/Channel/Extract EXR layers','extractExrLayers')
```
