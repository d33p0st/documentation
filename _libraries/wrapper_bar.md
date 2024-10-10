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
- TOC
{::options toc_levels="2,3" /}
{:toc}

## Installation

To install `wrapper-bar`, use pip.

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

