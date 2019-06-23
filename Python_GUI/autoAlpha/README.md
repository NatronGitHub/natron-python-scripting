# autoAlpha

Sets alpha to 1 (full white) for selected 'Read' nodes.

### HOW TO USE IT

* Select read nodes.
* Tools -> Channel -> Auto Alpha

### RESULT

* Selected 'Read' nodes have their alpha channel set to 1 (full white).

### INSTALLATION

* Copy 'autoAlpha' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file.

```
from Python_GUI.autoAlpha.autoAlpha import *
NatronGui.natron.addMenuCommand('Tools/Channel/Auto Alpha','autoAlpha')
```
