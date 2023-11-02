# Environmental setup

* [venv](#venv)
* [VS Code](#vscode)
  * [.vscode/](#.vscode/)
  * [.for-vscode.env](#.for-vscode.env)

## venv

*See: [Official documentation and tutorial](https://docs.python.org/3/tutorial/venv.html)*

First, navigate to the directory that will contain the project repository or directories.

````shell
> cd project_folder_path
> python -m venv name-of-desired-venv
````

Then, in Windows, run:

````shell
> venv/Scripts/actibate.ps
````

or, in Mac or Unix, run:

````shell
source name-of-desired-venv/bin/activate
````

## VS Code

### `.vscode/`

For `.launch.json`, copy and paste...

````json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Rosevomit: Run",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/rosevomit/rosevomit.py",
            "console": "integratedTerminal"
        },
        {
            "name": "Rosevomit: Test",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/devtests/_runtests.py",
            "console": "integratedTerminal"
        },
        {
            "name": "Rosevomit: Deep Test",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/devtests/_runtests.py",
            "console": "integratedTerminal",
            "justMyCode": false
        },
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
    ]
}
````

For `.settings.json`, copy and paste:

````json
{
    "python.pythonPath": "venv\\Scripts\\python.exe",
    "python.envFile": "<SOMETHING>\\rosevomitrepo\\for-vscode.env", // <-- CHANGE to the appropriate absolute path
    "python.linting.pylintEnabled": true,
    "python.linting.pylintArgs": [
        "--argument-rgx=ARG_[a-z_][a-z0-9_]{2,30}$",
        "--enable=all",
        "--disable=C0301,C0326,R1705",
    ],
    "python.linting.pylintCategorySeverity.refactor": "Information",
    "python.linting.mypyEnabled": true,
}
````

### `for-vscode.env`

````text
# regarding VSCode issue 3840 https://github.com/Microsoft/vscode-python/issues/3840

PYTHONPATH = ./rosevomit

# Problem here: https://github.com/PyCQA/pylint/issues/859
# Solution here: https://stackoverflow.com/questions/4374455/how-to-set-sys-stdout-encoding-in-python-3
PYTHONIOENCODING = utf-8
````