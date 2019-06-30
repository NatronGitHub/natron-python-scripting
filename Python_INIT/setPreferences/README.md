# setPreferences

Setup Natron's preferences using an external text file.

### INSTALLATION

* Copy 'setPreferences' folder in your .Natron folder.
* Add following lines to your 'init.py' file, where ``<path>`` is the location of 'setPreferences' folder.

```
from <path>.setPreferences.setPreferences import *
setPreferences()
```

Move preferences.txt file to .Natron folder.
