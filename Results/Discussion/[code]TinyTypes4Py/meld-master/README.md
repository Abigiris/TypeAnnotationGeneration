A command utility for organizing media

# Installation
Make sure to have Python (version >=3.6) installed. Open up this folder in your terminal and install using pip.

To install for all users, run
``` bash
$ pip install .
```
or for a single-user, run
``` bash
$ pip install --user .
```

You can check if the installation was succcessful by running
``` bash
$ meld -h
```

Command completion is avaliable thanks to the python `click` library. For bash users, add this line to `.bashrc`
```
eval "$(_MELD_COMPLETE=source meld)"
```
For zsh users, add this line to `.zshrc`
```
eval "$(_MELD_COMPLETE=source_zsh meld)"
```
Note that only the bash command completion has only been tested.

# Usage
Commands follow the syntax
```
meld [OPTIONS] COMMAND [ARGS]
```
For a list of commands, run `meld -h`. Commands are extendable via plugins. For more information on plugins, see the plugins section below. Meld ships with a few basic plugins. To import your media into it's database, run
```
meld import path/to/media
```
Your media can then be organized by running
```
meld move --set-id 123456 --format "~/Pictures/{set_name}/{file_name}"
```
The plugin will fill in the values for `set_name` and `file_name`.

# Configuration
Command options can be prepopulated using a user config. You can specify the config file using `meld --config /path/to/config` or you can place the config in `~/.config/meld/config.json`. Supported config formats are `.json` and `.py`. Note that for Python configurations, the config must be exported as the variable `config` as a dictionary.

An example configuration can be found in this folder. The basic format is as follows:
``` json
{
	"database": "/path/to/db.sqlite",
	"plugins": {
		"plugin1": {
			"setting1": "value1",
			"setting2": "value2"
		},
		"plugin2": {
			"settingA": 1
		}
	}
}
```
All of the top-level keys are required except for the `plugins` key.

For the builtin plugins, the command line arguments will override the option found in the config file.

# Plugins
For MacOS/Linux systems, the plugin directory is
```
~/.local/share/meld/plugins
```
For Windows, the plugin directory is
```
%LOCALAPPDATA%/meld/plugins
```
Installation of a plugin is simply a drag-and-drop of a python package into the plugin directory. Plugins that have an underscore (_) at the start of their filename will NOT be imported.

# Plugin Development
Plugins can be written as either python modules or packages. The entry points for the plugins are the global variables for the module. At the moment the only supported variables are:

- `cli`
- `tables`

A template can be found in `meld/plugins/_template`. Copy this template to your plugin folder and modify from there.

## CLI
NEED TO WRITE

## Database Tables
NEED TO WRITE

# Issues
The command line functionality is provided by the python `click` library. If you are seeing this RuntimeError
```
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment. Either switch to Python 2 or consult the Python 3 section of the docs for mitigation steps.
```
then you need to setup the locale of your system. This can be done by setting the following environmental variables.
``` 
LC_ALL=C.UTF-8
LANG=C.UTF-8
```
See the [Click documentation](https://click.palletsprojects.com/en/7.x/python3/#python-3-surrogate-handling) for additional details.