# 1 Overview. Installation. Basic Language Syntax

## Overview.

Python is a general-purpose, interpreted, high-level, dynamic programming language.
It's design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines 
of code compared to languages such as C++ or Java. The language provides constructs intended to enable writing clear 
programs on both a small and large scale.

### Advantages of Python

Most of the advantage of **Python** involves his _interpreted_ nature, but at the same time it offers a big set of 
options to develop:

* It's Interpreted
* It's Interactive
* It's Object-Oriented
* It's for Beginners
* It can work as a Functional Language

Also the language by itself offers other advantages, being _interpreted_ allows the language to be:

* Dynamic typed
* Able to use _type inference_
* Explicit type definition as well as *implicit* typing
* OS Independent

But not all can be sugar and honey, Python also has his disadvantages and they are explained next.

### Disadvantages

Being _interpreted_ makes the language great, but also makes the language to be slower or "interpreter dependant", which
means that the language will work as fast as the interpreter do. However, let's add that you can fix this issue/problem
recompiling the full interpreter to have better performance. Also, the interpreter by itself makes optimization on the 
fly like _caching_, making the language faster.

Another issue with the language are the versions. Even if the language has not changed so much, **Python 3** is a refactor
from version 2 with no compatibility, motivated by a clean-up of issues that were beyond a simple deprecation. To 
get a better understanding of this change, I recommend [Nick Coghland notes about why was Python 3 made incompatible
with Python 2](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#why-was-python-3-made-incompatible-with-python-2)
and also [What's New in Python 3](https://docs.python.org/3/whatsnew/3.0.html), the release notes from the official documentation.
 
This version subject makes you to decide about if you are going to work with **Python 2**, **Python 3**, a flavor of 
Python (like Jython or Cython) or some hybrid beast that allows you to run pseudo python code mixed with other stuff. 
In general, Python 3 is encouraged, unless you are deploying to an environment you don't control, or working with a 
certain package not yet compatible with Python 3. And once you decide, you cannot mix ~~(well, actually you can but is 
messy)~~ _Python 2_ with _Python 3 code_, as per the controversy detailed above.

## Installing Python

If your OS doesn't provide you with a Python installation, you can get it from multiple sources.

* Windows: Install it using an executable file, obtained from [Python Website](https://python.org/downloads). 
* *NIX: Install using the package manager, get the commands and guides from [Python Documentation](https://docs.python.org/3/using/unix.html).
* MacOS: MacOS comes with Python 2.7 installed. [Download](https://www.python.org/downloads/mac-osx/) a pkg file or 
use **Mac Ports** or **Homebrew** if you want to install Python 3.

You can have both Python 2 and 3 living in your operating system. You can set aliases to make _python_ command to point
to either version 2 or 3, as per your convenience. 

## Modules

Finding and installing new modules is a very straightforward operation in Python with tools like _pip_ and _easy_install_.
Pip is a package manager tool that allows you to install external modules/libraries onto the Python installation (global). 
Pip comes installed with Python or can be installed using get-pip tools.

For a full documentation about pip, see the [official documentation](https://pip.pypa.io/en/stable/quickstart/).

An alternative to pip is easy_install. Easy_install came into the scene before pip did, and both of them are built on
*setuptools* components, which is a library to maintain and create Python packages for projects. For more information
about these tools you can go to [easy_install official site](http://peak.telecommunity.com/DevCenter/EasyInstall) and
[setuptools official documentation](https://setuptools.readthedocs.io/en/latest/).

The main difference between pip and easy_install are listed below:

| Feature | pip | easy_install |
|---------|-----|--------------|
| Installation format | _Flat_ packages with _egg-info_ metadata | Encapsulated _Egg_ format (more information below) |
| Operations for installed packages | Uninstall, List, Freeze | Multi-version installs, sys.path modification |
| Special operations | Dependency overriding via requirements files | pylauncher support, install from Egg files |

### pip

Pip command supports installing from [PyPi (Python Package Index)](https://pypi.python.org/pypi/), from version control,
local projects and distribution files.

| Operation | Command | Notes |
|-----------|---------|-------|
| Install a package | pip install package-name | pip as of version 6.1.0 install dependencies before their dependents |
| Install a specific version | pip install package==1.0.1 | Minimum and maximum versions can be specified |
| Uninstall a package | pip uninstall package-name | When upgrading perform an automatic uninstall in backwards |
| List installed packages | pip list | Add --outdated to include outdated installed packages |
| Show details about a package | pip show package-name | Add -f to show the full list of installed files |
| Search for a package | pip search _query_ | Search for PyPI packages whose name or summary contains _query_ |
| Export installed packages | pip freeze | Generates output suitable for a _requirements file_ | 

For an extensive guide on installation packages, look at [pip installation guide](https://pip.pypa.io/en/stable/user_guide/).

#### Installation from a requirements file

Requirements files are files containing a list of packages/libraries to be installed using pip. They hold the result from
a pip freeze command execution to achieve repeatable installations. These files also force pip to resolve dependencies. 

Sample of a requirements file:

```
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

For more information about the requirements file format, see the [full reference](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format).

### easy_install

## Version Tools

### pyenv

### virtualenv

* * * * * *

And that's it for just an introduction, now let's get real with the Labs and the Homework before getting into the 
second part of this course.
