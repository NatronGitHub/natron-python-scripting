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
- **[autoAlpha](/Python_GUI/autoAlpha)** : Set alpha to 1 (full white) for selected 'Read' nodes.

### Generate
- **[rotoToTracker](/Python_GUI/rotoToTracker)** : Generate a 'Tracker' out of a selected 'Roto' node(s).

- **[trackerToRoto](/Python_GUI/trackerToRoto)** : Generate a 'Roto' out of a selected 'Tracker' node(s).

### Edit
- **[batchRenameNodes](/Python_GUI/batchRenameNodes)** : Rename selected nodes.

- **[connectNodes](/Python_GUI/connectNodes)** : Connect nodes to another one in the Node Graph.

- **[forceCaching](/Python_GUI/connectNodes)** : Connect nodes to another one in the Node Graph.

- **[invertSelection](/Python_GUI/invertSelection)** : Invert selection in the Node Graph.

- **[nodeChangeColor](/Python_GUI/forceCaching)** : Enable/disable force caching for selected nodes.

- **[nodeBold_HTML](/Python_GUI/nodeBold_HTML)** : Set selected nodes to be displayed in bold in the Node Graph.

- **[nodeItalic_HTML](/Python_GUI/nodeItalic_HTML)** : Set selected nodes to be displayed in italic in the Node Graph.

- **[openLocation](/Python_GUI/openLocation)** : Opens 'Read' or 'Write' location folder in explorer.

- **[removeInput](/Python_GUI/removeInput)** : Disconnect nodes input in the Node Graph.

- **[selectSimilar](/Python_GUI/selectSimilar)** : All nodes of the selected type will be selected in the Node Graph .

### Other
- **[mergeBlendingDown](/Python_GUI/mergeBlendingDown)** : Cycles through 'Merge' blending modes downward.

- **[mergeBlendingUp](/Python_GUI/mergeBlendingUp)** : Cycles through 'Merge' blending modes upward.

### Roto
- **[fullCircle](/Python_GUI/fullCircle)** : Create a full frame size circle.

- **[fullEllipse](/Python_GUI/fullEllipse)** : Create a full frame size ellipse.

- **[fullSquare](/Python_GUI/fullSquare)** : Create a full frame size square.

- **[fullRectangle](/Python_GUI/fullRectangle)** : Create a full frame size rectangle.

- **[leftTriangle](/Python_GUI/leftTriangle)** : Create a left aligned triangle.

- **[rightTriangle](/Python_GUI/leftTriangle)** : Create a right aligned triangle.

- **[topTriangle](/Python_GUI/leftTriangle)** : Create a top aligned triangle.

- **[bottomTriangle](/Python_GUI/leftTriangle)** : Create a bottom aligned triangle.

### Time
- **[nodeChangeFPS](/Python_GUI/nodeChangeFPS)** : Sets FPS for selected 'Read' nodes.

- **[nodeChangeFrameRange](/Python_GUI/nodeChangeFrameRange)** : Sets frame range for selected 'Read' nodes.

### Utils
- **[collectFiles](/Python_GUI/collectFiles)** : Identical to After Effects 'Collect Files' feature. Used to backup a comp.

- **[replacePaths](/Python_GUI/replacePaths)** : Replace path in 'Read' nodes.

### Render
- **[backgroundRender](/Python_GUI/backgroundRender)** : Render current project in background.

- **[diskCache](/Python_GUI/diskCache)** : Create and process a 'DiskCache' node for the selected node.

- **[flipbook](/Python_GUI/flipbook)** : Render and plays the selected node in an external viewer. (Win/Linux)

## Natron snippets
- **[addDeepLayer](/Python_INIT/addDeepLayer)** : Add 'Deep' layer to Natron.

- **[addDepthLayer](/Python_INIT/addDepthLayer)** : Add 'Depth' layer to Natron.

- **[addMaskLayer](/Python_INIT/addMaskLayer)** : Add 'Mask' layer to Natron.

- **[addMotionLayer](/Python_INIT/addMotionLayer)** : Add 'Motion' layer to Natron.

- **[listNatronPath](/Python_INIT/listNatronPath)** : List paths scanned by Natron at startup.

- **[listPyPlugs](/Python_INIT/listPyPlugs)** : List PyPlugs installed on the system.

- **[natronLogo](/Python_INIT/natronLogo)** : Display a nice Natron logo in the console. ;)

- **[setPreferences](/Python_INIT/setPreferences)** : Setup Natron's preferences using an external text file.

- **[setProjectSettings](/Python_INIT/setProjectSettings)** : Set up project default settings.

## Natron stylesheets

- **[mainstyle_NUKE](/Stylesheet/mainstyle_NUKE)** : Mimics Nuke look.

