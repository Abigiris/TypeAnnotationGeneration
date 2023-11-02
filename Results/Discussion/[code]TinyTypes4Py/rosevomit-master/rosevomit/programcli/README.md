# ROSEVOMIT/rosevomit/projectcli/

The `rosevomit/projectcli/` directory (folder) contains the modules (files) necessary for Rosevomit's command-line interface. They are generally called by the main script, [`rosevomit.py`](https://github.com/AlexLemna/rosevomit/blob/master/rosevomit/rosevomit.py), which is in the [`rosevomit/`](https://github.com/AlexLemna/rosevomit/tree/master/rosevomit) directory. The files in this directory probably look something like this:

````text
+ __init__.py       <-- a file that Python needs
+ bettercli.py      <-- the main file for the replacement command line interface (WIP)
+ README.md         <-- the file you're reading now
+ worsecli.py       <-- the main file for the current command line interface
`````

***NOTE: The information below is not yet fully implemented.***

**Message** functions are bits of text that do not accept user input, other than sometimes asking the user to 'press enter' to advance the program. They are generally system-wide, and are defined in the `messages.py` file. In the future, we may divide up message functions into `messages.py` and `_messages.py` (in-use messages vs message templates, respectively) if things get complicated, but we're nowhere near that point.

**Dialog** functions are made up of prompt and menus (or sometimes displays). **Menu** functions, like messages, are static displays of text.  **Prompt** functions accept user input, and may "clean" it or validate it in some manner (low-level parsing). If a prompt offers the user the chance to exit the current dialog and the user makes that choice, it returns "None" to the dialog. **Display** functions are like menu functions in that they display information to the user and don't accept user input, but they don't have static pre-defined content. Instead, they get information (either from within Rosevomit or from an external file) and they display it to the user in a certain format. The base/templates menu, prompt, and display functions are defined in the `_dialog.py` file, while each dialog actually used by the program is in a 'dialog' file, like `dialogexit.py` or `dialogsave.py`.

The "business logic" associated with each dialog - that is, the actions that occur once a user has selected a valid option within a particular dialog - is not handled in this directory. Instead, it is handled by the `programlogic` modules.
