---
layout: page
title: Upgraded Built-ins
description: The index page for modstore's upgraded built ins
---

#### modstore
{:.no_toc}

# {{ page.title }}
{:.no_toc}

<p align='center'>
    <a href='../algorithms/#libraries'>Algorithms</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../new/#libraries'>New</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../rust/#libraries'>Rust</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../#libraries'>Go back</a>
</p>

## Table of Contents
{:.no_toc}

- TOC
{::options toc_levels="2,3,4" /}
{:toc}

## List Docs

The `List` is an upgraded version of python's built-in `list`. `List` has a lot of extra features which will make a lot of complex operations easy.

### Features

- **Upgrades**: `List` has a lot of upgrades which makes it the better choice. It also has built-in support for [`Stack`](#stack-docs).

### Usage

Let's jump to usage.

#### Importing and Creating a `List`.

```python
# import from modstore package
from modstore.python import List

# create a List type variable
# NOTE: create-option 1
some_list = List() # will create an empty List.

# NOTE: create-option 2
normal_list = [1 ,2 ,3, 4]
some_list1 = List(normal_list) # create from built-in list type object/variable.

# NOTE: create-option 3
some_dictionary = {1: "abc", 2: "xyz"}
some_list2 = List(some_dictionary) # will create a List -> [1, 2]

some_list3 = List(some_dictionary.values()) # will create a List -> ["abc", "xyz"]

some_list4 = List(some_dictionary.items()) # will create a List -> [(1, "abc"), (2, "xyz")]

# NOTE: create-option 4
some_tuple = (1, 2, 3, 4) # this is immutable
some_list5 = List(some_tuple) # this is mutable.

# NOTE: create-option 5
some_list6 = List()
some_list6.append(1)
some_list6.append(2)
```

<span>{% include icon.liquid id='info-circle' %} <b>Important Note</b></span><br> `List` inherits `list` class and has all the precursor methods in it. In addition, it has more.
{:.ui.info.message}

#### `fillByInput` and `fillByString` methods

FillByInput:

```python
# NOTE: FillByInput
# initialize an empty List
>>> some_list = List()

# fill the list from user input.
>>> some_list.fillByInput (
...    splitby=' ', # split using white spaces
...    typecast=int, # typecast the values if found, into int.
...    prompt='Enter some values here:', # prompt to be shown to the user.
... )
...
Enter some values here: 1 2 3  4    5    6
>>> some_list
[1, 2, 3, 4, 5, 6]
# NOTE: The number of white spaces does not matter, it wont be added to the list unless there is a value.

# NOTE: Additionally, It will raise TypeCastError if the typecast fails.
```

FillByString

```python
# NOTE: fillByString
# initialize an empty List
>>> some_list = List()

# fill the list from a string.
>>> some_list.fillByString (
...    string='12345', # string to be used.
...    splitby='', # split by each character,
...    typecast=int, # typecast each value to int
... )
...

>>> some_list
[1, 2, 3, 4, 5]
# NOTE: This will raise TypeCastError if the typecast fails.
```

#### Get Length of the `List`

```python
# lets make an example list
some_list = [1, 2, 3, 4]
length = some_list.length
```

#### Convert To `Stack`

You can either convert the `List` to stack with infinite capacity or a definite capacity (If the capacity is definite and less than the length of the `List`, it will raise `ValueError`)

```python
# NOTE: infinite capacity
some_list = List([1, 2, 3, 4, 5])
some_stack = some_list.convertToStack
```

```python
# NOTE: definite capacity
some_list = List([1, 2, 3, 4])
some_stack_with_capacity_10 = some_list.convertToStackWithCapacity(10)
```

#### Rotate the list

Rotate the `List`, `t` times with respect to `k` (number of elements to rotate) and from either `Back` or `Front`.

```python
# take some list
>>> some_list = List([1, 2, 3, 4, 5])

# rotate
>>> rotated_list = some_list.rotate (k=2, times=2, from_='Front')

>>> rotated_list
[5, 1, 2, 3, 4]

# This was the result of,
# first iteration: [3, 4, 5, 1, 2]
# second iteration: [5, 1, 2, 3, 4]
# NOTE: the elements were taken from the `Front` and put into the back. as `from_` parameter was set to `Front`.
```

#### Chunk the `List`

```python
>>> some_list = List([1, 2, 3, 4, 5, 6])
>>> chunkedList = some_list.chunk(2)
>>> chunkedList
[[1, 2], [3, 4], [5, 6]]
```

#### Flatten the `List`

```python
>>> some_list = List([[1, 2], [3, 4], [5, 6], 7, 8, 9, [10, 11]])
>>> flat = some_list.flatten
>>> flat
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

#### Get Unique Elements only

```python
>>> some_list = List([1, 1, 1, 1, 1, 1, 2, 3, 3, 4])
>>> unique = some_list.unique
>>> unique
[1, 2, 3, 4]
```

#### Filter Elements by type

```python
>>> some_list = List([1, 2, "a", 5, 6, "b"])

>>> strings = some_list.filter(str)
>>> strings
["a", "b"]

>>> integers = some_list.filter(int)
>>> integers
[1, 2, 5, 6]
```

#### Interleave more `Lists` into the current `List`

```python
# NOTE: This wont modify the current list. will return a new list
>>> some_list = List([1, 2, 3])
>>> new = some_list.interleave([10, 20, 30], [100, 200, 300, 320])
>>> new
[1, 10, 100, 2, 20, 200, 3, 30, 300, 320]
```

#### Apply some function to all the elements of the `List`

```python
# NOTE: Option 1
>>> some_list = List([1, 2, 3, 4])

# define some function to be applied to each element of the List and get a new List.
>>> def some_function(val: int) -> int: # a function that takes one int value and returns one int value
...     return 2 * val
...

# to get the new List, use the `work` method.
>>> new_list = some_list.work(some_function)
>>> new_list
[2, 4, 6, 8]
```

```python
# NOTE: Option 2
>>> some_list = List([1, 2, 3, 4])

# If your function returns bool and you want to store only the values that return true.

>>> def even(val: int) -> bool: # a function that takes each element and returns a bool type value.
...     return val % 2 == 0
...

# Now to store only the elements which returns True for the above function.

>>> new_list = some_list.work(even, store_elements=True)
>>> new_list
[2, 4]
```

#### Count the Occurrence of each Element.

```python
>>> some_list = List([1, 1, 1, 2, 2, 3, 4, 4, 5])
>>> data = some_list.counter
>>> data
{1: 3, 2: 2, 3: 1, 4: 2, 5: 1}
```

#### Remove Duplicates in place

```python
>>> some_list = List([1, 1, 1, 1, 2, 2, 2, 4, 5])
>>> some_list.remove_duplicates
>>> some_list
[1, 2, 4, 5]
```

#### Swap Two indexes in place

```python
>>> some_list = List([1, 2, 3, 4, 5])
>>> some_list.swap(0, some_list.length - 1) # swap index 0 with last element
>>> some_list
[5, 2, 3, 4, 1]

# NOTE: This will throw IndexError if the index does not exist
```

#### Partition the `List` based on boolean condition

```python
# NOTE: Works a bit like `work` method but returns two `Lists`

>>> some_list = List([1, 2, 3, 4, 5])

# define a function that takes one int as parameter (as the List elements are of type int) and returns bool.
>>> def some_function(val: int) -> bool:
...     return val % 2 == 0
...

# the values that return True are returned in the First List and the False ones in the Second List.
>>> even, odd = some_list.partition(some_function)

>>> even
[2, 4]

>>> odd
[1, 3, 5]
```

#### Combinations of the `List`

```python
# this works like `itertools.combinations`
>>> some_list = List([1, 2, 3, 4, 5])
>>> new_list = some_list.combinations(2)
>>> new_list
[(1, 1), (1, 2), (1, 3), ... (2, 2), (2, 3), ... (5, 5)]
```

#### Reverse in place

```python
>>> some_list = List([1, 2, 3, 4, 5])
>>> some_list.reverse
>>> some_list
[5, 4, 3, 2, 1]
```

#### Check if the `List` is a palindrome

```python
>>> some_list = List([1, 2, 1])
>>> some_list.isPalindrome
True

>>> some_list2 = List([1, 2, 3])
>>> some_list2.isPalindrome
False
```

#### Find and group the word anagrams

`Anagram` of word is another word with the same number of letters and same letters.

`Example`: ate and eat are anagrams.

```python
>>> words = List(['ate', 'tea', 'eat', 'abc', 'bca', 'a'])
>>> words.group_anagrams
[['ate', 'tea', 'eat'], ['abc', 'bca'], ['a']]
```

#### Merge Sorted `Lists`

```python
>>> some_list = List([1, 2, 5, 6])
>>> some_list.merge_sorted([2, 4, 6])
[1, 2, 2, 4, 5, 6, 6]
```

<p align='center'>
    <a href='../algorithms/#libraries'>Algorithms</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../rust/#libraries'>Rust</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../new/#libraries'>New</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../#libraries'>Go back</a>
</p>