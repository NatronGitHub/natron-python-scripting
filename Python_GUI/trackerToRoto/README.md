# trackerToRoto

Generates a 'Roto' out of a selected 'Tracker' node(s).

### HOW TO USE IT

* Select one or more 'Tracker' node(s).
* Tools -> Generate -> Tracker to roto
* Select 'All' or 'Selected'.
  - All : generates a roto out of all tracks
  - Selected : generates a roto out of selected tracks ( at least 3 must be selected )
* Click 'OK.'

#### Overall

* Tracks :
  - All
  - Selected

### RESULT

* Roto following the exact shape a move of tracks.

### INSTALLATION

* Copy 'trackerToRoto' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'trackerToRoto' folder.

```
from <path>.trackerToRoto.trackerToRoto import *
NatronGui.natron.addMenuCommand('Tools/Generate/Tracker to roto','trackerToRoto')
```