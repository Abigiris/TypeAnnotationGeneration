"""
This file dynamically imports all plugins within this folder as well as the 
app data folder
"""

from pathlib import Path

from meld.utils import app_data_dir as _app_data_dir, loadModulesFromDir


app_plugins_dir = Path(_app_data_dir, 'plugins')
app_plugins_dir.mkdir(parents=True, exist_ok=True)

builtin_plugins = loadModulesFromDir(Path(__file__).parent)
user_plugins = loadModulesFromDir(app_plugins_dir)
