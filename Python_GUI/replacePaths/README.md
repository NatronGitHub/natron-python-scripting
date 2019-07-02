# replacePaths

Replace path in 'Read' nodes.

### HOW TO USE IT

* Select 'Read' nodes.
* Tools -> Utils -> Replace Paths
* Select 'All' or 'Selected'

### RESULT

* Paths are replaced.

### INSTALLATION

* Copy 'replacePaths' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'replacePaths' folder.

```
from <path>.replacePaths.replacePaths import *
NatronGui.natron.addMenuCommand('Tools/Utils/Replace Paths','replacePaths()')