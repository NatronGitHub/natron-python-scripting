# backgroundRender

Renders current project in background.

### HOW TO USE IT

* Tools -> Render -> Background Render

### RESULT

* Current project will be rendered in background.

### INSTALLATION

* Copy 'backgroundRender' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'backgroundRender' folder.

```
from <path>.backgroundRender.backgroundRender import *
NatronGui.natron.addMenuCommand('Tools/Render/Background Render','backgroundRender')
```
