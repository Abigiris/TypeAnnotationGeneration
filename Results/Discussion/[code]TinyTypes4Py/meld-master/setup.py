from setuptools import setup, find_packages
import meld

setup(
    name=meld.__title__,
    author=meld.__author__,
    version=meld.__version__,
    python_requires="~=3.6",
    packages=find_packages(),
    # package_dir={'meld':'./src/meld'},
    install_requires=["click", "Pillow", "appdirs"],
    include_package_data=True,
    entry_points={"console_scripts": ["meld = meld.app.cli:cli"]},
)
