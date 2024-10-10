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

- Create a fake progress bar for aesthetics.

  Use the `decoy` method. The `decoy` method has these parameters -- 

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

- Create a progress bar and run shell commands behind it.

  Use the `shellWrapper` method. The `shellWrapper` method has the following parameters --

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