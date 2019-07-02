# collectFiles

Identical to After Effects 'Collect Files' feature.
Used to backup a comp.

### HOW TO USE IT

* Tools -> Utils -> Collect Files

### RESULT

Comp and all files used in it are copied to one unique folder.
All 'Read' nodes are relinked to their new file location.
Opens new folder location.

### NOTE :

* Linux : Default explorer used in script is 'thunar'. Replace it in script (line 188) by the one of your Linux distro.

### INSTALLATION

* Copy 'collectFiles' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'collectFiles' folder.

```
from <path>.collectFiles.collectFiles import *
NatronGui.natron.addMenuCommand('Tools/Utils/Collect Files','collectFiles()')