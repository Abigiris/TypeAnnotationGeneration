# ***Rosevomit* changelog**

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), though I use a few extra catagories (`Development` and `Internal`) to help me track changes that don't directly impact the user. More information about this may be available in my repository's [styleguide](https://github.com/AlexLemna/rosevomit/blob/master/docs/styleguide.md#changelog).

This project will adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) once it reaches version 1.0. Until then, I'm using my own idiosyncratic versioning scheme where I use v0.0.0 and v0.10.0 for my first two development 'milestones' and then try to proceed normally-ish from there (i.e. v0.10.1, v0.11.0, v0.12.0, v0.12.1, and so on).

## [Contents](#contents)

* [Unreleased](#unreleased)
* [0.10.3 - 2019-10-02](#0103---2019-10-02)
* [0.10.2 - 2019-09-03](#0102---2019-09-03)
* [0.10.1 - 2019-05-11](#0101---2019-05-11)
* [0.10.0 - 2019-05-01](#0100---2019-05-01)
* [0.0.0 - 2019-04-23](#000---2019-04-23)

## [Unreleased]

This upcoming release is expected to be **0.11.0**.

### Added

* NEW FEATURE: Added ability to generate logs during Rosevomit's use. (issue [#27])
* NEW FEATURE: Added ability to see licensing information from within Rosevomit. (Issue [#47])

[#27]: https://github.com/AlexLemna/rosevomit/issues/27
[#47]: https://github.com/AlexLemna/rosevomit/issues/47

### Development

* TYPO: Fixed typo in 'rosevomit.core._dynamic_constants' module docstring.

## [0.10.3][0-10-3-compare] - 2019-10-02

*See [GitHub release][0-10-3-release] and [tag], see [diffs][0-10-3-compare], or return to the [table of contents](#contents).*

### Added

* NEW FEATURE: Added ability to change the settings from the CLI. (issue [#30]). Along the way, we discovered that the settings module didn't properly handle a corrupted file (issue [#41]) - which we fixed.

### Fixed

* BAD VERSIONING: Turns out we weren't updating the in-program version tracker. Fixed that. Also released a fix (commit [77c66b]) that corrected this for the previous version
* DEVELOPER TOOLS: Fixed the unexpected exit behavior of Pylint test (issue [#42]) and another testing bug that was introduced by other changes in this version (issue [#46])
* STANDARD PARAMETER NAMES: All the parameter names have been renamed according to my own convention ('ARG_name'). (issue [#40])

### Removed

* REMOVED TEMP DIRECTORY ACCESS: Removed the ability for the user to access the `/temp` directory from inside the program.

### Internal

* CLEANING UP THE LINT: Chased down a lot of bad habits with the help of [Pylint](https://www.pylint.org/) and [Better Code Hub](https://bettercodehub.com/), including...
  * ...using `type()` instead of `isinstance()` for typechecking.
  * ...using `!=` instead of `is not`.
* UNDER THE HOOD: Refactoring and rewriting the startup process, the filesave process, and the exit process so that they're both standardized and easier to understand at a glance.
* SOME THINGS NEVER CHANGE: Added constants file to `core` module (issue [#38]) and the `devtests` module

### Development

* DEVELOPER TOOLS: Added ability to choose which test to run (issue [#37]).
  * Also improved summary file? (???)
  * Added more sanity tests.
* PROCESS IS OUR VALENTINE: Added release checklist to docs folder (see first fix)
* WHEN I MET YOU I WAS BUT THE LEARNER: I learned how to instruct Pylint about my unusual parameter naming conventions, so now it *enforces* them rather than bugging me about them. (Issue [#40])
* DOCSTRINGS: Most functions and modules now have docstrings.

[#30]: https://github.com/AlexLemna/rosevomit/issues/30
[#37]: https://github.com/AlexLemna/rosevomit/issues/37
[#38]: https://github.com/AlexLemna/rosevomit/issues/38
[#40]: https://github.com/AlexLemna/rosevomit/issues/40
[#41]: https://github.com/AlexLemna/rosevomit/issues/41
[#42]: https://github.com/AlexLemna/rosevomit/issues/42
[#46]: https://github.com/AlexLemna/rosevomit/issues/46
[77c66b]: https://github.com/AlexLemna/rosevomit/commit/77c66b3f391ae7c3db6d436a31a4ee9dce538318

## [0.10.2][0-10-2-compare] - 2019-09-03

*See [GitHub release][0-10-2-release] and [tag], see [diffs][0-10-2-compare], or return to the [table of contents](#contents).*

### Added

* NEW FEATURE: *Rosevomit* can now generate a random timeline.
* NEW FEATURE: These random timelines can be saved!

### Changed

* UNDER THE HOOD: Lots of internal refactoring, revamping the internal heirarchy of this project's filesystem, revamping module names, etc.
* DEVELOPER TOOLS: Added automated code tests to help me catch bugs. I even figured out how to store the results in text files!

## [0.10.1][0-10-1-compare] - 2019-05-11

*See [GitHub release][0-10-1-release] and [tag], see [diffs][0-10-1-compare], or return to the [table of contents](#contents).*

Many of these changes were small changes. From a user's perspective, the largest change will be that the names generated are no longer from short name lists I wrote. Instead, they're from [old US Census data](https://www.census.gov/topics/population/genealogy/data/1990_census/1990_census_namefiles.html).

### Changed

* ENHANCEMENT: *Rosevomit* now uses real-world name lists from the [US Census](https://www.census.gov/topics/population/genealogy/data/1990_census/1990_census_namefiles.html).
* TYPO FIXED: [Whoops](https://github.com/AlexLemna/rosevomit/issues/18).
* UNDER THE HOOD: Better docstrings, more READMEs instead of the wiki, standardized naming convensions in line with [PEP8](https://www.python.org/dev/peps/pep-0008/), improved error handling, and added software version data.

## [0.10.0][0-10-0-compare] - 2019-05-01

*See [GitHub release][0-10-0-release] and [tag], see [diffs][0-10-0-compare], or return to the [table of contents](#contents).*

It turns out there's already a [rosa](https://pypi.org/project/rosa/) package on PyPI. Since the point of this project is to make some basic utility and publish it, I need a new name. There's lots of advice online about renaming projects - the name shouldn't have unpleasent connotations and it should maintains a sense of continuity with any previous names.

So, *Rosevomit* sounds like a good name to me.

This is version 0.10.0. I'm jumping straight to 10 because I used to think "version 0.1" meant a project was 10% done, and "0.4" meant 40%, and so on. It turns out that's not usually the case - especially not in this project. Each segment of the version number is an integer on it's own, and so I figured that calling something "version 0.10.0" would be a good reminder to myself not to focus on comparing version 0.10.0 to my plans for version 0.11.0, not a hypothetical perfect version 1.0.0. (Sounds stupid when I'm typing it out, but it made perfect sense in my head.)

Anyways, yeah: version 0.10.0. It can generate names.

### Added

* NEW FEATURE: This program can now generate random names. It can generate however many names you want, all in a row. It can generate male or female names only, or it can ignore gender. It can generate first names, last names, and full names (first + last).
* NAME CHANGE: *Project Rosa* is now *Rosevomit*.

## [0.0.0][0-0-0-release] - 2019-04-23

*See [GitHub release][0-0-0-release] and [tag], or return to the [table of contents](#contents).*

Created *"Project Rosa"*.

`rosa.py` can respond to user input via a CLI, and call `LogicController.py`. `LogicController.py` can, in turn, call `rlRandomName.py`. `rlRandomName.py` can then extract data randomly from a text file, and return it all the way up the chain for `rosa.py` to display.

[Unreleased]: https://github.com/AlexLemna/rosevomit/compare/0.10.3...HEAD
[0-10-3-compare]: https://github.com/AlexLemna/rosevomit/compare/0.10.2...0.10.3
[0-10-3-release]: https://github.com/AlexLemna/rosevomit/releases/tag/0.10.3
[0-10-2-compare]: https://github.com/AlexLemna/rosevomit/compare/0.10.1...0.10.2
[0-10-2-release]: https://github.com/AlexLemna/rosevomit/releases/tag/0.10.2
[0-10-1-compare]: https://github.com/AlexLemna/rosevomit/compare/0.10.0...0.10.1
[0-10-1-release]: https://github.com/AlexLemna/rosevomit/releases/tag/0.10.1
[0-10-0-compare]: https://github.com/AlexLemna/rosevomit/compare/0.0.0...0.10.0
[0-10-0-release]: https://github.com/AlexLemna/rosevomit/releases/tag/0.10.0
[0-0-0-release]: https://github.com/AlexLemna/rosevomit/releases/tag/0.0.0
[tag]: https://github.com/AlexLemna/rosevomit/tags
