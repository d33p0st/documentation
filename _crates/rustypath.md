---
layout: page
title: Rustypath
description: A straightforward no bullshit crate for managing paths in rust.
order: 1
---

![Crates.io Total Downloads](https://img.shields.io/crates/d/rustypath?style=flat&logoSize=auto&label=crates.io%20downloads)

# {{ page.title }}
{:.no_toc}

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

<span> {% include icon.liquid id='info-circle' %} <b>Info</b></span><br> `creation`, `management`, `conversion` and `boolean` are enabled by default. `pyo3-bindings` is disabled by default. To enable this, run this in terminal/CMD: `cargo add rustypath --features pyo3-bindings`.
{:.ui.info.message}

## Usage

- Importing

  ```rust
  use rustypath::RPath; // for all basic functionalities.
  ```
  `Note:` Implementation includes -> [`Clone`, `Debug`, `PartialEq`, `Eq`, `PartialOrd`, `Ord`, `Hash`] and a custom trait for printing `RPath`.
  ```rust
  // for printing the path as it is, `Display` trait can be imported.
  use rustypath::Display;
  ```

- Creating `RPath`

  - From `&str`, `Path` and `PathBuf`
    ```rust
    // to create a RPath
    let rpath_str = RPath::from(value);

    // NOTE: value can be of type &str, Path (std::path::Path) or PathBuf (std::path::PathBuf)

    // Examples:
    let rpath = RPath::from("/temp");
    let rpath_ = RPath::from(std::path::Path::new("/temp"));
    let rpath__ = RPath::from(std::path::PathBuf::from("/temp"));
    ```

  - Allocate an empty `RPath`
    ```rust
    let rpath_empty_or_new = RPath::new();
    // this will allocate an empty RPath
    ```

- Path Manipulation

  - Join
    ```rust
    // make a RPath
    let rpath = RPath::from("/temp");

    // add childs to it,
    let new = rpath.join("abc.txt");
    new.print();
    // this will print "/temp/abc.txt"
    ```

  - Join Multiple
    ```rust
    // make a RPath
    let mut rpath = RPath::from("/temp");

    // suppose you want to add multiple components to the path
    rpath.join_multiple(vec![value1, value2, ...]);
    // here value1, value2 can be any of these types => [&str, Path, or PathBuf]
    rpath.print();
    // this will print -> "/temp/value1/value2/..."
    ```
  
  - Basename/Filename
    ```rust
    // to get the basename or filename of the path:
    let rpath: Rpath = RPath::from("/temp/abc.txt");
    let basename: &str = rpath.basename();
    ```

  - Replace Basename
    ```rust
    // suppose there's a RPath -> "/temp/abc.txt" and
    // you want to just replace "abc.txt" with "xyz.txt" without
    // typing whole new full paths or rel paths, and just update using
    // the existing one.

    let rpath = RPath::from("/temp/abc.txt");
    let rpath_ = rpath.with_basename("xyz.txt"); // this will be "/temp/xyz.txt" 
    ```

  - Dirname/Parent
    ```rust
    let rpath: RPath = RPath::from("/temp/abc.txt");

    // to get the parent
    let parent: RPath = rpath.dirname(); // this will be "/temp"
    ```

  - Replace Dirname/Parent
    ```rust
    // suppose there's a RPath -> "/temp/abc.txt" and
    // you want to replace "/temp" with something else

    let rpath: RPath = RPath::from("/temp/abc.txt");
    let new = rpath.with_dirname("/temp/temp2"); // this will make it -> "/temp/temp2/abc.txt"
    ```

  - Extention
    ```rust
    // to get the extension of a file from the RPath
    let rpath = RPath::from("/temp/abc.txt");

    let extension: &str = rpath.extension();
    // NOTE: this will return either extension (if present) or the basename.
    // if path is invalid it will print error and exit.
    ```

  - Expand
    ```rust
    let rpath = RPath::from("./temp");
    let expanded = rpath.expand(); // this will expand if not full path, else it wont throw error.
    // remeber that it will only expand the path if the path exits
    // if "./temp" directory doesnt exist it will return "./temp"
    ```

  - Read_Dir (return an iterator with DirEntry)
    ```rust
    let rpath = RPath::from("/temp");

    for entry in rpath.read_dir().expect("Failed to call read_dir") {
        if let Ok(entry) = entry {
            println!("{:?}", entry.path());
        }
    }
    ```

  - Get Current Working Directory
    ```rust
    let current_dr: RPath = RPath::pwd();
    ```

  - Get Home dir of your OS
    ```rust
    let home: RPath = RPath::gethomedir();
    ```

  - Clear the current RPath buffer
    ```rust
    let rpath = RPath::from("/temp");
    rpath.clear(); // this will be equivalent to RPath::new();
    ```

- Conversion

  - Convert to string
    ```rust
    let rpath = RPath::from("/abc");
    let rpath_string = rpath.convert_to_string();
    ```

  - Convert to PathBuf
    ```rust
    let rpath = RPath::from("/abc");
    let rpath_in_pathbuf = rpath.convert_to_pathbuf();
    ```

- Boolean

  - exists
    ```rust
    let rpath = RPath::from("/abc");
    if rpath.exists() {
        // do something
    }
    ```

  - is_dir/is_file
    ```rust
    let rpath = RPath::from("/abc");

    if rpath.is_dir() {
        // do something
    } else if rpath.is_file() {
        // do something
    }
    ```
  Similarly, the following will work:

  - is_absolute

  - is_symlink

  - is_relative

  Extras:

  - if_extension

    ```rust
    let rpath = RPath::from("/abc.txt");
    
    if rpath.if_extension("txt") {
      println!("The file is a text file!");
    }
    ```

- Printing

  `RPath` supports printing as a single string.

  To use the `.print()` function, import `Display` trait
  ```rust
  use rustypath::Display;
  ```

  Printing using `.print()` method.
  ```rust
  let rpath = RPath::gethomedir();
  rpath.print();
  // this will print `homedir` path in a single line.
  ```

  To print with other strings:
  ```rust
  let rpath = RPath::gethomedir();

  println!("Homedir: {}", rpath.convert_to_string());
  println!("{:?}", rpath);
  ```

- Operators

  - Supports `==` and `!=` operators
    ```rust
    let rpath = RPath::pwd();
    let rpath_ = RPath::gethomedir();

    if rpath == rpath_ {
        // do something
    } else {
        // do something else
    }
    ```

- Supports Hash

## pyo3-bindings

Lets understand by an example.

You are using `rustypath::RPath` to manage all your paths but when creating Python/Rust Mix projects, you also want it to be easier to return `RPath` to python? right?. Say No more!

```rust
use pyo3::prelude::*;
use rustypath::RPath;

#[pyfunction]
fn demo(dir: &str) -> PyResult<RPath> { // see that I am returning RPath, which is not supported by python.
  let new = RPath::from(dir);

  Ok(new) // this will work fine and will return a string.
}

// similarly while returning Vec<RPath>, it will return a list of strings.
```


## Issues

If any issues were found kindly add 'em [here](https://github.com/d33pster/rustypath/issues) along with any feature requests.

## Pull Requests

Pull requests are encouraged and can be added [here](https://github.com/d33pster/rustypath).