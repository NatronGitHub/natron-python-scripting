# nodeChangeFPS

Sets FPS for selected 'Read' nodes.

### HOW TO USE IT

* Select 'Read' nodes.
* Tools -> Time -> Read FPS
* Set In and Out.
* Click 'OK.'

### RESULT

* Selected nodes have their FPS changed.

### INSTALLATION

* Copy 'nodeChangeFPS' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'nodeChangeFPS' folder.

```
from <path>.nodeChangeFPS.nodeChangeFPS import *
NatronGui.natron.addMenuCommand('Tools/Time/Read FPS','nodeChangeFPS()')