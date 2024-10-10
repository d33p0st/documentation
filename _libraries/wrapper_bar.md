---
layout: page
title: Wrapper Bar
description: Wrap actual commands behind a progress bar.
order: 1
---

# {{ page.title }}
{:.no_toc}

<span> {% include icon.liquid id='info-circle' %} <b>Badges</b></span><br>
![PyPI - Version](https://img.shields.io/pypi/v/wrapper-bar)
![PyPI - License](https://img.shields.io/pypi/l/wrapper-bar)
[![Downloads](https://static.pepy.tech/badge/wrapper-bar)](https://pepy.tech/project/wrapper-bar)
{:.ui.big.success.message}

`Wrapper-Bar` is a python module to help wrap commands behind a progress bar. `Wrapper-Bar` helps in wrapping shell commands, or python codes (both independent and dependent) and downloads with a progress bar and time.

<span> {% include icon.liquid id='info-circle' %} <b>Info</b></span><br>
`Wrapper-Bar >= 0.1.5` supports wrapping file downloads.
{:.ui.info.message}

## Table of Contents
{:.no_toc}

- TOC
{::options toc_levels="2,3" /}
{:toc}

## Installation

To install `wrapper-bar`, use pip.
Open a terminal or CMD and run:

```python
pip install wrapper-bar
```

## Usage

To start creating progress bar with commands we need to import the `Wrapper` class from the `wrapper-bar` package.

Import the `Wrapper` class.

```python
>>> from wrapper_bar import Wrapper
# before v0.1.6, use
# from wrapper_bar.wrapper import Wrapper
```

The `Wrapper` class has the following usage doc

```python
# the Wrapper Class takes one argument - 'marker'
# the default is '▓', which will simulate a loading bar element.

wrapControl = Wrapper()
# let us just create the wrapControl with Default settings
```

Now we can perform the following tasks with it:

- **Create a fake progress bar for aesthetics.**

  Use the _`decoy`_ method. The _decoy_ method has these parameters -- 

  - `label`: (str) type parameter. Set the Label to be shown at the left of the loading bar.

  - `delay`: (float) type parameter. Set the delay between each update of the loading bar.

  - `width`: (float) type parameter. Set the width of the loading bar. Default is `50`.

  - `timer`: (Literal[str]) type parameter. This can be either `ETA` or `ElapsedTime`. Default is `ETA`.

  ```python
  wrapControl.decoy(
    label='Loading',
    delay=0.5,
    width=70,
    timer='ElapsedTime'
  )
  ```

  This will output the following:

  ```console
  Loading |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|Elapsed Time: 0:00:50
  ```

- **Create a progress bar and run shell commands behind it.**

  Use the _shellWrapper_ method. The _shellWrapper_ method has the following parameters --

  - `shellcommands`: (List[str]) type parameter. Set the commands to be run in the shell in order. Create a list of string with each string representing a full single command.

  - `label`: (str) type parameter. Set the Label to be shown at the left of the loading bar.

  - `delay`: (float) type parameter. Set the delay between each update of the loading bar.

  - `width`: (float) type parameter. Set the width of the loading bar. Default is `50`.

  - `timer`: (Literal[str]) type parameter. This can be either `ETA` or `ElapsedTime`. Default is `ETA`.

  - `logger`: (bool) type parameter. Set it to `True` if the outputs need to be logged.

  - `logfile`: (TextIOWrapper) type parameter. Set the log file ref if `logger` is set to `True`.

  - `logfile_auto_close`: (bool) type parameter. Setting it to `True` will close the log file ref.

  ```python
  # let us take an example list of shell codes
  shell_codes = [
    """sudo apt-get update""",
    """sudo apt-get upgrade""",
  ]

  # let us open a file ref for logging
  logfile = open('logfile.log', 'w+')

  # now let us create a progress bar that ends after
  # completely running these codes in order.
  wrapControl.shellWrapper(
    label='Shell Codes Running:',
    width=80,
    timer='ElapsedTime',
    logger=True,
    logfile=logfile,
    logfile_auto_close=True, # this will auto close the logfile
  )
  ```

  This will output the following:

  ```console
  Shell Codes Running: |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|Elapsed Time: 0:00:10
  ```

- **Create a progress bar and run python scripts behind it.**

  Use the _pyWrapper_ method. The _pyWrapper_ method has the following parameters -- 

  - `pythonscripts`: (List[str]) type parameter. Set the list of script names.

  - `label`: (str) type parameter. Set the Label to be shown at the left of the loading bar.

  - `delay`: (float) type parameter. Set the delay between each update of the loading bar.

  - `width`: (float) type parameter. Set the width of the loading bar. Default is `50`.

  - `timer`: (Literal[str]) type parameter. This can be either `ETA` or `ElapsedTime`. Default is `ETA`.

  - `logger`: (bool) type parameter. Set it to `True` if the outputs need to be logged.

  - `logfile`: (TextIOWrapper) type parameter. Set the log file ref if `logger` is set to `True`.

  - `logfile_auto_close`: (bool) type parameter. Setting it to `True` will close the log file ref.

  ```python
  # let us take two different python scripts
  pyscripts = [
    'abc.py',
    'xyz.py'
  ]

  # let us create a logfile ref
  log_ref = open('log.logs', 'w+')

  # now the progress bar
  wrapControl.pyWrapper(
    label='Processing'
    pythonscripts=pyscripts,
  )
  ```

  The will output the following:

  ```console
  Processing: |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|ETA: 0:00:00
  ```

- **create a progress bar and run python codes behind it that are dependent on the current script/project or just inline codes**

  Use _pyShellWrapper_ method. The _pyShellWrapper_ has the following parameters --

  - `pythoncodes`: (List[str]) type parameter. Set the actual processing codes here.

  - `dependencies`: (List[str]) type parameter. All the dependencies to run any of the codes listed in `pythoncodes` goes here.

  - `label`: (str) type parameter. Set the Label to be shown at the left of the loading bar.

  - `delay`: (float) type parameter. Set the delay between each update of the loading bar.

  - `width`: (float) type parameter. Set the width of the loading bar. Default is `50`.

  - `timer`: (Literal[str]) type parameter. This can be either `ETA` or `ElapsedTime`. Default is `ETA`.

  ```python
  # let us take an example of simple addition
  dependencies = [
    """a, b, c = 10, 20, 15"""
  ]
  # dependencies will have all the values needed for operations
  # follow python programming rules and indentation

  pycodes = [
    """a += b
  b = a + c
  d = a + b""",

    """e = a + b"""
  ]

  # pycodes will have all the operation codes
  # follow python programming rules and indentation

  # now the loading bar
  wrapControl.pyShellWrapper(
    pythoncodes=pycodes,
    dependencies=dependencies,
    label='Processing',
  )

  # to get the results,
  results: Dict[str, Any] = wrapControl.pyShellWrapperResults
  # will contain values of 'a', 'b', 'c', 'd', 'e' after carrying out both the operations provided in the list
  ```

  This will again result in a progress bar as shown in above cases.

<span> {% include icon.liquid id='exclamation-triangle' %} <b>Warning</b></span><br> Do not use keywords like return, yield, print or functions that use print, yield or return keywords, else they will mess up the loading bar.
{:.ui.warning.message}

- **Create a progress bar for downloading a file.** `>=v0.1.5`

  Use _downloadWrapper_ method. The _downloadWrapper_ method has the following parameters --

  - `link`: (str) type parameter. Set the link of the download.
  If you have the direct download link, put it there. It wont work with any other kind of link.

    _If you are downloading from a github release, put the repository link here._

  - `download_to`: (str) type parameter. Set the destination directory, it should exist.

  - `download_filename`: (str) type parameter. It is optional to provide. If the link given is a direct download link, `download_filename` could be left empty, in which case, the program will try to resolve it from the link. However, if the name is not provided and it could not be resolved from the link, an Exception will be raised.

    _If downloading from a github release, provide the name_

  - `type`: (Literal) type parameter. It takes only two values, `'direct'` and `'github_release'`. Set the type of link.

    _If you want to download from a github release, use the repo link in the `link` parameter_.

  - `github_release`: (str) type parameter. If you are downloading from a github release, set the version of the release here. If unsure, use `'latest'`. Defaults to `'latest'`. If direct link, ignore this param.

  - `private_repo`: (bool) type parameter. If the repository is private, set it to `True`.

  - `github_api_token`: (str) type parameter. This is optional and only needs to be set in case of private repository.
  
    _Note that if you are setting `private_repo` param as `True` and at the same time, no `github_api_token` was provided, an Exception will be raised._

  - `label`: (str) type parameter. Set the Label to be shown at the left of the loading bar.

  - `width`: (float) type parameter. Set the width of the loading bar. Default is `50`.

  - `chunk_size`: (int or None) type parameter. The chunk size to use for reading and writing data. If it is set to `None`, the data will be read in any size it is being downloaded.

  ```python
  # for downloading a file with a direct download link, these are the only parameters needed.
  wrapControl.downloadWrapper(
    label = 'Downloading:',
    link = "https://...",
    download_to = "<download-dir>",
    download_filename = 'file.zip',
    type = 'direct'
    width = 70,
  )

  # for github release.

  ## PUBLIC RELEASE (PUBLIC REPOSITORY)
  wrapControl.downloadWrapper(
    label = 'Downloading:',
    link = "https://github.com/d33pster/Friday", # public repo
    download_to = "./friday", # this should exist
    download_filename = 'bot.zip', # download bot.zip from some release of the repo
    type = 'github_release',
    github_release = 'latest', # download from the latest release
    # or set it to v1.0 or v2.34.4, and so on.
  )

  ## PRIVATE RELEASE (PRIVATE REPOSITORY)
  wrapControl.downloadWrapper(
    label = 'Downloading:',
    link = "https://github.com/d33p0st/some-private-repo", # private repo
    download_to = "./some-dir", # should exist
    download_filename = 'somefile.txt', # file to download
    type = 'github_release',
    github_release = 'latest',
    private_repo = True,
    github_api_token = '...', # your token
    width = 100,
  )
  ```

## Yanked Versions

- `v0.1.2`

## Issues

Submit any issues [here](https://github.com/d33p0st/wrapper-bar/issues).

Submit your pull requests [here](https://github.com/d33p0st/wrapper-bar/pulls).

---

[Go back](https://d33p0st.in/documentation) -[HomePage](https://d33p0st.in)