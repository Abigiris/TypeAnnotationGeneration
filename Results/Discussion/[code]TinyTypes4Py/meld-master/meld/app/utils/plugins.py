"""
This module offers utility functions for interacting with plugins
"""
from typing import Generator

import meld.plugins as plugins


def get_plugin_with_attr(attr: str) -> Generator:
    """
    Generates a plugin that has the attribute specified
    This function prioritizes user plugins over the builtins 
    """
    for plugin in plugins.user_plugins + plugins.builtin_plugins:
        if hasattr(plugin, attr):
            yield plugin
