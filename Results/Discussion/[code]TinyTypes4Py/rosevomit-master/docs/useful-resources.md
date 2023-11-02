# My useful references

## Contents

* [Versioning and development](#devstuff)
  * [Changelogs](#changelogs)
  * [Commits](#commits)
  * [Git](#git)
  * [Semantic Versioning](#semantic-versioning)
* [Programming languages](#languages)
  * [Python](#python)
* [Other languages](#otherlanguages)
  * [Markdown](#markdown)

## Versioning and development

This section contains my notes and useful links regarding software development tools and best practices.

### Changelogs

I like the "Keep a Changelog" standard, presented [here](https://keepachangelog.com/en/1.0.0/). It doesn't give a strict format, but it does offer a few helpful rules: keep the lastest version at the top, keep an `Unreleased` section so you have a place to keep track of changes as you make them, make sure each version's date is prominantly displayed, etc. It also offers standard terminology to help catagorize changes: `Added` for new features, `Changed` for changes in existing functionality, `Deprecated` for soon-to-be removed reatures, `Removed` for removed features, `Fixed` for bug fixes, and `Security` for vulnerabilities.

### Commits

There's a set of guidelines for human- and machine-readable commit messages over at [Conventional Commits](https://www.conventionalcommits.org), along with lists of useful tools for enforcing commit message style.

### Git

For general notes on four of the best-known Git workflows, check out [Gitflow vs. Github Flow vs. Gitlab Flow vs. OneFlow](https://medium.com/@patrickporto/4-branching-workflows-for-git-30d0aaee7bf), a Medium post by Patric Porto. For detailed dives into each workflow, see:

* [Gitflow](https://nvie.com/posts/a-successful-git-branching-model/), from Vincent Driessen
* [GitHub Flow](http://scottchacon.com/2011/08/31/github-flow.html), from Scott Chacon.
* [GitLab Flow](https://docs.gitlab.com/ee/workflow/gitlab_flow.html), from GitLab (original post [here](https://about.gitlab.com/2014/09/29/gitlab-flow/)).
* [OneFlow](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow), from Adam Ruka

These four well-known workflows are obviously only suggestions, and there are other, potentially lesser known models:

* [MojoTech's Git Workflow](https://www.mojotech.com/blog/mojotech-git-workflow/).

Finally, some really useful advice and links (including browser extensions) can be found here: [15 recommendations to enhance your GitHub flow](https://gaboesquivel.com/blog/2018/15-recommendations-to-enhance-your-github-flow/)

### PEP 440

The standard practice for Python projects is to use the versioning guidelines from [PEP 440](https://www.python.org/dev/peps/pep-0440/). I'm not going to mention them too much here, because [Semantic Versioning](#semantic-versioning) is stricter and valid semantic versions can be a subset of valid PEP 440 versions.

### Semantic Versioning

One widely adopted versioning scheme is [Semantic Versioning](https://semver.org/), which has strict rules for when major, minor, and patch numbers are incremented, namely,

````text
SEMANTIC VERSIONING
    Given a version number MAJOR.MINOR.PATCH, increment the:

        MAJOR version when you make incompatible API changes,
        MINOR version when you add functionality in a backwards compatible manner, and
        PATCH version when you make backwards compatible bug fixes.

    Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.
````

While this versioning scheme has no practical purpose for this project because we have neither a userbase nor an API, thinking of my project in Semantic Versioning terms seems like a good habit to get into.

## Programming languages

### Python

* What's up with modules? [Modules in the Python docs](https://docs.python.org/3/tutorial/modules.html)
* Regarding [importing in Python](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#basics-of-the-python-import-and-syspath)

## Other languages

### Markdown

* The spec sheet for [Github-flavored Markdown](https://github.github.com/gfm/)
* The general spec sheet(s) for [Markdown](https://spec.commonmark.org/)
* [Tips on using Visual Studio Code and Pandoc to edit Markdown](https://thisdavej.com/build-an-amazing-markdown-editor-using-visual-studio-code-and-pandoc/)
