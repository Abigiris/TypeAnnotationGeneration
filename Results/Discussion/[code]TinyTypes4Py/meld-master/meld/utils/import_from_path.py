import importlib.machinery
import importlib.machinery
from typing import Union, List
from types import ModuleType
from pathlib import Path

def _isPackage(path: Path, ignore_private: bool = True) -> bool:
    if ignore_private and path.stem[0] == '_':
        return False
    if path.is_dir() and path.joinpath('__init__.py') in path.iterdir():
        return True
    return False


def _isModule(path: Path, ignore_private: bool = True) -> bool:
    if ignore_private and path.stem[0] == '_':
        return False
    if path.is_file() and path.suffix == '.py':
        return True
    return False

def loadModulesFromDir(path: Union[str, Path]) -> List[ModuleType]:
    modules = []
    for p in Path(path).iterdir():
        if _isModule(p):
            loader = importlib.machinery.SourceFileLoader(p.stem, str(p))
        elif _isPackage(p):
            loader = importlib.machinery.SourceFileLoader(
                p.stem, str(p / '__init__.py'))
        else:
            continue
        # load_module is deprecated in favor of exec_module but it doesn't work
        # for packages... 
        module = loader.load_module()
        modules.append(module)
    return modules