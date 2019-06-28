# rotoToTracker

Generates a 'Roto' out of one or multiple 'Tracker' node(s).

### HOW TO USE IT

* Select one or more 'Roto' node(s).
* Tools -> Generate -> Roto to Tracker

### RESULT

* Trackers are generated for every bezier curve within selected 'Roto' node(s).

### INSTALLATION

* Copy 'rotoToTracker' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'rotoToTracker' folder.

```
from <path>.rotoToTracker.rotoToTracker import *
NatronGui.natron.addMenuCommand('Tools/Generate/Roto to tracker','rotoToTracker')
```