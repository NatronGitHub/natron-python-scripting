# timelineInOut

Sets timeline In/Out points.

### HOW TO USE IT

* Tools -> Time -> Timeline IO
* Set In and Out.
* Click 'OK.'

### RESULT

* Timeline In/Out points have been changed.

### INSTALLATION

* Copy 'timelineInOut' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'timelineInOut' folder.

```
from <path>.timelineInOut.timelineInOut import *
NatronGui.natron.addMenuCommand('Tools/Time/Timeline IO','timelineInOut()')
```