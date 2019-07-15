![Image](Resources/community-scripting-logo.png)
# Natron python scripts
### A collection of Natron python scripts made by the community
## Installation
The scripts can be installed by simply cloning the github repository, or download it as a ZIP file, by clicking on the top-right green button 'Clone or download'.

Unzip the content to your .Natron folder.


    Windows: "C:\Users\<username>\.Natron"

    OSX:     "[~/.Natron]"

    Linux:   "[~/.Natron]"

Restart Natron.

## Natron tools

### Channel
- **[autoAlpha](/Python_GUI/autoAlpha)** : Sets alpha to 1 (full white) for selected 'Read' nodes.

### Generate
- **[rotoToTracker](/Python_GUI/rotoToTracker)** : Generates a 'Tracker' out of a selected 'Roto' node(s).

- **[trackerToRoto](/Python_GUI/trackerToRoto)** : Generates a 'Roto' out of a selected 'Tracker' node(s).

### Node Graph
- **[batchRenameNodes](/Python_GUI/batchRenameNodes)** : Renames selected nodes.

- **[connectNodes](/Python_GUI/connectNodes)** : Connects nodes to another one in the Node Graph.

- **[connectNodesList](/Python_GUI/connectNodesList)** : Connects nodes to one choosen in the list.

- **[nodeChangeColor](/Python_GUI/nodeChangeColor)** : Sets node color for selected nodes.

- **[nodeBold_HTML](/Python_GUI/nodeBold_HTML)** : Sets selected nodes to be displayed in bold in the Node Graph.

- **[nodeItalic_HTML](/Python_GUI/nodeItalic_HTML)** : Sets selected nodes to be displayed in italic in the Node Graph.

- **[openLocation](/Python_GUI/openLocation)** : Opens 'Read' or 'Write' location folder in explorer.

### Other
- **[mergeBlendingDown](/Python_GUI/mergeBlendingDown)** : Cycles through 'Merge' blending modes downward.

- **[mergeBlendingUp](/Python_GUI/mergeBlendingUp)** : Cycles through 'Merge' blending modes upward.

### Time
- **[nodeChangeFPS](/Python_GUI/nodeChangeFPS)** : Sets FPS for selected 'Read' nodes.

- **[nodeChangeFrameRange](/Python_GUI/nodeChangeFrameRange)** : Sets frame range for selected 'Read' nodes.

### Utils
- **[collectFiles](/Python_GUI/collectFiles)** : Identical to After Effects 'Collect Files' feature. Used to backup a comp.

- **[replacePaths](/Python_GUI/replacePaths)** : Replace path in 'Read' nodes.

### Render
- **[backgroundRender](/Python_GUI/backgroundRender)** : Launch render of current project in background.

- **[diskCache](/Python_GUI/diskCache)** : Creates and process a 'DiskCache' node for the selected node.

- **[flipbook](/Python_GUI/flipbook)** : Renders and plays the selected node in an external viewer. (Win/Linux)

## Natron snippets
- **[addDeepLayer](/Python_INIT/addDeepLayer)** : Adds 'Deep' layer to Natron.

- **[addDepthLayer](/Python_INIT/addDepthLayer)** : Adds 'Depth' layer to Natron.

- **[addMaskLayer](/Python_INIT/addMaskLayer)** : Adds 'Mask' layer to Natron.

- **[addMotionLayer](/Python_INIT/addMotionLayer)** : Adds 'Motion' layer to Natron.

- **[listNatronPath](/Python_INIT/listNatronPath)** : Lists paths scanned by Natron at startup.

- **[listPyPlugs](/Python_INIT/listPyPlugs)** : Lists PyPlugs installed on the system.

- **[natronLogo](/Python_INIT/natronLogo)** : Displays a nice Natron logo in the console. ;)

- **[setPreferences](/Python_INIT/setPreferences)** : Setup Natron's preferences using an external text file.

- **[setProjectSettings](/Python_INIT/setProjectSettings)** : Set up project default settings.

## Natron stylesheets

- **[mainstyle_NUKE](/Stylesheet/mainstyle_NUKE)** : Mimics Nuke look.

