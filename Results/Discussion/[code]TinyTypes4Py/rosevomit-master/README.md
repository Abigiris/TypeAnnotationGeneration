# ROSEVOMIT: a name generator

[![BCH compliance](https://bettercodehub.com/edge/badge/AlexLemna/rosevomit?branch=master)](https://bettercodehub.com/)
[![](https://pyup.io/repos/github/AlexLemna/rosevomit/shield.svg)](https://pyup.io)

If you've stumbled across this project in search of an actually functional name generator, I highly recommend checking out [faker](https://github.com/joke2k/faker). This is a personal project to teach myself some programming basics. You can see my changelog [here](https://github.com/AlexLemna/rosevomit/blob/master/docs/changelog.md) and my roadmap [here](https://github.com/AlexLemna/rosevomit/blob/master/docs/roadmap.md). The roadmap is probably better viewed through this project's "Glo" kanban board [here](https://app.gitkraken.com/glo/board/XW-3b9aSlAAPAWps), which is also linked to this project's issue boards.

New to coding? You and me both, buddy. If you've viewing this on GitHub, you probably see this README underneath a bunch of files and folders. The file structure should be something like this:

````text
+ dev-tests/          <-- scripts/files for testing purposes
+ docs/               <-- additional documentation
+ rosevomit/          <-- ROSEVOMIT's main directory
+     core/
+     projectcli/
+     projectdata/
+     projectlogic/
+     rosevomit.py        <-- ROSEVOMIT's main file
+ .bettercodehub.yml  <-- a config file for Better Code Hub's automatic tests
+ .gitattributes      <-- a file Git needs for stats
+ .gitignore          <-- a file Git needs
+ LICENSE
+ README.md           <-- the file you're reading now
````

Don't freak out - it can look intimidating, but you can see that there's only a few places you actually need to look if you want to start looking Rosevomit's code: the [`rosevomit.py`](https://github.com/AlexLemna/rosevomit/blob/master/core/rosevomit.py) file and the contents of the [`core/`](https://github.com/AlexLemna/rosevomit/tree/master/core) directory. If you're like me and like to see an expandable "file tree" instead navigating through seperate webpages for each folder, I recommend using the browser extension [Octotree](https://www.octotree.io/).
