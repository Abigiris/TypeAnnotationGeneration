# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# about.py
# rosevomit.core.about
# ___________________________________________________________________
"""This file contains general information about Rosevomit, as well as information about the tools and programs it was developed with or depends on."""
from core import logs

_ABOUT_LOGGER = logs.BaseLogger(__name__)

LICENSE = (
    "MIT License",
    "Copyright (c) 2019 Alexander Lemna",
    'Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:',
    "The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.",
    'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.',
)
PROGRAM = (
    "Rosevomit exists primarily as a hobby/self-learning project for its original developer, Alex Lemna, and is only incidentally intended to be useful to others. The fact that it is open-source and (hopefully) well-documented doesn't mean that its developer knows what he is doing. If you have some spare time and see some mistakes or areas that could be improved - fork it and open a pull request!",
    "Rosevomit is written in Python 3, a free (like speech and beer) high-level programming language. A programming language is a specification of rules and syntax that makes it easier for humans to talk to computers, and most programming languages can have multiple 'implementations' or ways of translating their human-readable program into machine code. In my case, I used the CPython implementation of Python - but if you try to run this program's source code on another Python implementation like PyPy, it should be able to run just fine.",
)
