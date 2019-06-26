# trackerToRoto

Generates a 'Roto' out of a selected 'Tracker' node.

### HOW TO USE IT

* Tools -> Generate -> Tracker to roto
* Select 'All' or 'Selected'.
* Click 'OK.'

### RESULT

* Roto following the exact shape a move of tracks.

### INSTALLATION

* Copy 'trackerToRoto' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'trackerToRoto' folder.

```
from <path>.trackerToRoto.trackerToRoto import *
NatronGui.natron.addMenuCommand('Tools/Generate/Tracker to roto','trackerToRoto')
```