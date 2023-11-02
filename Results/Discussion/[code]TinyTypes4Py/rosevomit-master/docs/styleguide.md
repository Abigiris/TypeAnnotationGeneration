# Rosevomit's style guide

In general, Rosevomit's code should be written to whatever standards are generally accepted by the relevant language community. Since right now all of Rosevomit is written in Python, this is easy - Python's style guide, [PEP8](https://www.python.org/dev/peps/pep-0008/), is both official and widely accepted, so all of Rosevomit's code should be compared against it. There are a few areas where I do *not* follow PEP8 (yet) - these will be explored later.

## Contents

* [Python naming conventions](#Python-naming-conventions)
  * [tl;dr](#tl;dr)
* [Commit messages](#Commit-messages)
  * [Commit message formatting](#Commit-message-formatting)
    * [Acceptable ```<types>```](#Acceptable-```<types>```)
    * [Acceptable ```<scope>```](#Acceptable-```<scope>```)
    * [Acceptable ```<subject>``` text](#Acceptable-```<types>```-text)
  * [Commit message shorthand](#commit-message-shorthand)
  * [General rules](#GENERAL-RULES)
* [Changelog formatting](#changelog)
* [Versioning](#versioning)

## Python naming conventions

*SECTIONS: [Python naming conventions](#Python-naming-conventions) • [tl;dr](#tl;dr) • back to [top](#Rosevomit's-style-guide)*

**Functions**, **variables**, **methods**, and **instances** should be lowercase. Separating words with underscores to increase readibility is welcomed, especially if some of the words are abbreviations or acronyms. *See: [snake_case](https://en.wikipedia.org/wiki/Snake_case)*

In a departure from PEP 8, **parameters** (often called arguments) should follow the variable naming conventions while having an `ARG_` as a prefix. This is just for personal convenience, as I find it helpful when writing functions to be able to instantly distinguish between the value of a parameter as it was passed into the function and any similarly-named internal variables.

Since Python does not support **constants** natively, is it considered best practice to write variables you expect to be constant in all capital letters. Like all other variables, constants should be written with underscores when it improves readibility.

**Classes** should have the first letter of each word capitalized, and should have no spaces. *See: [CamelCase](https://en.wikipedia.org/wiki/Camel_case)*

**Modules** and **packages** intended for distribution on PyPI should be lowercase. Modules and packages *not* intended for distribution (which is most, if not all, Python files in this repository) should be written with the first letter capitalized and without underscores. *Again, see: [CamelCase](https://en.wikipedia.org/wiki/Camel_case)*

### tl;dr

* `menu_choice` and `menuchoice` might be variables or functions, but `MenuChoice` is definitely a class.
* `ARG_menuchoice` is a parameter/argument for a function.
* `MENU_CHOICE` and `MENUCHOICE` are constants.

## Commit messages

*SECTIONS: [Commit messages](#Commit-messages) • [Commit message formatting](#Commit-message-formatting) • [Commit message shorthand](#commit-message-shorthand) • [General rules](#GENERAL-RULES) • back to [top](#Rosevomit's-style-guide)*

### Commit message formatting

*Shamelessly stolen from Anderon Bravalheri [here](https://gist.github.com/abravalheri/34aeb7b18d61392251a2), who in turn got it from Stephen Parish [here](https://gist.github.com/stephenparish/9941e89d80e2bc58a153), all of which is based off of the system developed by AngularJS and described [here](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits)*.

Overall, the subject line format is ```<type>(<scope>): <subject> <#meta>``` with the ```<#meta>``` being optional. The full message format (including that subject line) is:

```text
<type>(<scope>): <subject> <#meta>

DETAILS
<body>

FOOTER
<footer>
```

with the ```DETAILS``` and ```FOOTER``` sections being optional. The ```FOOTER``` section should reference relevant issues, restate breaking changes, and link to mitigation/comments on tose breaking changes.

#### **Acceptable ```<type>```**

* **FEAT**: A new feature
* **FIX**: A bug fix
* **ADJ** or **REF**: My most common `<type>` - a code change that neither fixes a bug nor adds a feature. This includes anything that would be considered [refactoring](https://en.wikipedia.org/wiki/Code_refactoring). Basically, I use this for anything that's not covered by "FIX" or "FEAT".
* **STYLE**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)

Documentation and development changes

* **DOCS**: Documentation changes only
* **TEST**: Changes to the testing process
* **DEV** or **CHORE**: Changes that are related to the development process but NOT specific to testing. Changes to the build process or auxiliary tools and libraries such as documentation generation. This also sometimes shows up under the abbreviation or name of a paritcular tool, such as:
  * **GIT** for Git
  * **BCH** for Better Code Hub
  * If I ever start using them, I could conciebavly have **TRAVIS** for Travis and **DOCKER** for Docker.
* **REVRT** or **REVERT**: Reverting to an earlier commit

Related to releases,

* **RP**: Preperation for pushing to a release branch. Generally includes adding release notes and incrementing the version number. Use this on `rc` branches.
* **RELEASE**: A commit that pushes a new version to a release branch.
* **FIX for X.Y.Z**: Almost all commits to a release branch must, by definition, be a new version. However, sometimes a released version has documentation typos or some other problem that deserves to be fixed but doesn't involve the actual code. In this case, we use the "FIX for X.Y.Z" commit message, and we delete and recreate that version's git tag appropriately.

#### **Acceptable ```<scope>```**

Anything that specifies the place of the changes. In my case, it'll probably be directories, etc. One rule to remember is that **if the changed files are not noted in the subject, they must be noted in the body**.

#### **The ```<subject>``` text**

An alternate title for this section: *What's up with the imperitive tense?* I still think that it looks unnatural, but I'm long-winded so every character counts. I'll switch to the imperitive.

Oh, and the 50-character limit is useful. I'm wordy, though, so 56. That still beats the 72-character suggestion I'm currently using with GitKraken.

### Commit message shorthand

Some acceptable shortcuts in the :

* "+" for "added"
* "-" for "removed"
* "~" for "changed"

### General rules

*Shamelessly stolen from Romulo Oliveira [here](https://github.com/RomuloOliveira/commit-messages-guide)*.

Some rules:

1. Try to communicate what the change does without having to look at the source code.
1. Use the message body to explain "why", "for what", "how" and additional details.
1. Avoid generic messages or messages without context.
1. Use a single language.
1. Limit the subject message to 50 characters.

An example example template from Tim Pope's *Pro Git Book*:

```text
Summarize changes in around 50 characters or less

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of the commit and the rest of the text as the body. The
blank line separating the summary from the body is critical (unless
you omit the body entirely); various tools like `log`, `shortlog`
and `rebase` can get confused if you run the two together.

Explain the problem that this commit is solving. Focus on why you
are making this change as opposed to how (the code explains that).
Are there side effects or other unintuitive consequences of this
change? Here's the place to explain them.

Further paragraphs come after blank lines.

 - Bullet points are okay, too

 - Typically a hyphen or asterisk is used for the bullet, preceded
   by a single space, with blank lines in between, but conventions
   vary here

If you use an issue tracker, put references to them at the bottom,
like this:

Resolves: #123
See also: #456, #789
```

## [Changelog formatting](#changelog)

*SECTIONS: none • back to [top](#Rosevomit's-style-guide)*

I try to adhere to the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) recommendations. I use the recommended catagories of `Added` for new features, `Changed` for changes in existing functionality, `Deprecated` for soon-to-be removed reatures, `Removed` for removed features, `Fixed` for bug fixes, and `Security` for vulnerabilities. I also some additional catagories like `Development` to track changes in testing/development process, and `Internal` to track refactoring/changes that don't directly impact users.

## [Versioning](#versioning)

*SECTIONS: none • back to [top](#Rosevomit's-style-guide)*

To some extent, versioning on this project is meaningless because I'm not even sure what the end goal of this program **is**. It mostly just exists to help me learn Python (and, potentially, other languages) and I don't expect anyone besides myself to actually use this thing. To be honest, I think I added version numbers just to help me feel a sense of progress.

So far, my versioning has been a little unusual because I immediately jumped from `0.0.0` (my equivalent of a Hello World program) to `0.10.0`. My intent with this was just to remind myself that the "minor" number could be incremented liberally and I wasn't measuring my versions based on progress towards a goal - for instance, I didn't want to worry about whether or not `0.4.0` was 40% of the way to a viable release. Instead, I figured I'd have something like this:

````text
0.0.0 --> 0.10.0 --> 0.10.1 --> 0.11.0 --> 0.12.0 --> ...
````

Based on the fact that I've ended up with `0.0.0 --> 0.10.0 --> 0.10.1 --> 0.10.2 --> 0.10.3`, despite doing serious work adding new features that have no relation to each other, I could stand to be a little more aggressive when incrementing my minor version number.

If/when I ever feel like declaring this project 'feature-complete,' however, my plan is to stick to a public versioning scheme that is simultaneously consistent with [Semantic Versioning](https://semver.org/) and Python's [PEP 440](https://www.python.org/dev/peps/pep-0440/). I'll also probably have some sort of seperation between marketing version and technical version, like [here](https://www.fredonism.com/a-practical-take-on-gitflow-and-semantic-versioning).
