---
layout: page
title: Rustypath
description: A straightforward no bullshit crate for managing paths in rust.
order: 1
---

# {{ page.title }}
{:.no_toc}

<span> {% include icon.liquid id='info-circle' %} <b>Badges</b></span><br>
![Crates.io Total Downloads](https://img.shields.io/crates/d/rustypath?style=flat&logoSize=auto&label=crates.io%20downloads)
{:.ui.big.success.message}

`rustypath` is a no bullshit crate for managing paths in rust. Single methods for carrying out tasks or checking something path related.

## Table of Contents
{:.no_toc}

- TOC
{::options toc_levels="2,3" /}
{:toc}

## Installation

Run the following code in terminal/CMD.

Install for your project.

```bash
cargo add rustypath
```

Install globally

```bash
cargo install rustypath
```

## Crate Features

In `>=v1.0.0`, the code has been divided into features due to growing functionality --

- `creation`: This is responsible for creation of `RPath` from any of these -- `String`, `&str`, `Path` and `PathBuf`.

- `management`: This is responsible for management and manipulation of paths.

- `conversion`: This is responsible for conversion of `RPath` to other types.

- `Boolean`: This contains all the boolean return type functions (checks).

- `pyo3-bindings`: This contains bindings for `pyo3` crate. Enables `RPath` return type for functions defined under `pyo3`. When `RPath` is returned to python, it will be automatically converted to string.

<span> {% include icon.liquid id='info-circle' %} <b>Info</b></span><br> `creation`, `management`, `conversion` and `boolean` are enabled by default. `pyo3-bindings` are disabled by default. To enable this, run this in terminal/CMD: `cargo add rustypath --features pyo3-bindings`.
{:.ui.info.message}
