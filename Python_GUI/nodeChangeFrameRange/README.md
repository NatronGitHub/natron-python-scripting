# nodeChangeFrameRange

Sets frame range for selected 'Read' nodes.

### HOW TO USE IT

* Select 'Read' nodes.
* Tools -> Time -> Read Frame Range
* Set In and Out.
* Click 'OK.'

### RESULT

* Selected nodes have their frame range changed.

### INSTALLATION

* Copy 'nodeChangeFrameRange' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'nodeChangeFrameRange' folder.

```
from <path>.nodeChangeFrameRange.nodeChangeFrameRange import *
NatronGui.natron.addMenuCommand('Tools/Time/Read frame range','nodeChangeFrameRange()')
```
