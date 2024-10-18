---
layout: page
title: Newly added Data Structures
description: The index page for modstore's newly added data structures
---

#### modstore
{:.no_toc}

# {{ page.title }}
{:.no_toc}

<p align='center'>
    <a href='../algorithms/#libraries'>Algorithms</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../builtins/#libraries'>Built-ins</a>
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

## Stack Docs

A `stack` is a linear data structure that follows the Last In First Out (LIFO) principle, where the most recently added element is the first to be removed. Operations typically include:

- Push
- Pop
- Peek
- isEmpty

### Features

- **Disabled `[]`**: The usage of `[]` for setting, getting or deleting an element is disabled and will generate `StackError`.

- **Vast Range of Utilities**: Several utilities are available directly inbuilt inside the class that can be used for either testing purpose or projects or the unavoidable cheating in exams (not made for this purpose.).

- **Can be Generated from [List][list] Class**: The [List][list] class available under `modstore.python` can convert itself to `Stack` or can be explicitly passed to `Stack`'s `__init__` method (meaning, if you have a [List][list] type variable you can create a stack by `Stack(variable)`). We will look into it Later.

- **All `Stack` behavior**: The `stack` class is made into a proper implementation of stack and replicates complete stack behavior `(LIFO)`.

### Usage

Let us jump to usage.

#### Importing and creating `Stack`

```python
# import the Stack class
>>> from modstore.python import Stack

# Stack Creation
# NOTE: method 1 - Empty Stack
>>> empty_stack = Stack(capacity=10) 
# capacity of the stack is 10.
# for infinite capacity, set the capacity to None.

# NOTE: method 2 - From any iterable sequence
>>> stack = Stack([1, 2, 3, 4])
# stack that has 4 elements pushed into it with 4 at the top and capacity infinity

>>> stack2 = Stack((1, 2, 3, 4, 5), 10)
# stack with 5 elements with 5 at top and capacity 10.

# NOTE: method 3 - From `modstore's List`
>>> from modstore.python import List

# create some list for this example
>>> some_list = List([1, 2, 3, 4])

# convert to stack
# with infinite capacity
>>> stack_inf_cap = some_list.convertToStack

# with limited capacity
>>> stack_lim = some_list.convertToStackWithCapacity(10)
# this will raise a ValueError if the limit is less than the number of elements in the List.

# NOTE: Apart from the `convertToStack` and `convertToStackWithCapacity` the `modstore.python.List` type variables can be directly passed to the Stack().

>>> some_stack = Stack(some_list)
# This is what I was talking about in the Features Section
```

#### Push into the stack

```python
stack.push(1)
stack.push("abc")
```

#### Pop from the stack

```python
top_value = stack.pop
```

#### Peek

`Peek` means getting the value at the top of the stack without popping it.

```python
value_at_top = stack.peek
```

#### Getting the top index

```python
top = stack.top
```

#### Checking if stack is Empty or not

```python
if stack.isEmpty:
    print("Stack is empty")
else:
    print("Stack is not empty")
```

#### get the size of the stack (filled)

```python
length = stack.size
```

#### Get capacity of the stack

```python
print(stack.capacity) # will print `inf` if infinity else some `int`
```

#### Get the sum of all elements in the stack (only if the elements are `int` and `float`)

```python
stack = Stack()
stack.push(19)
stack.push(20)

print(stack.sum) # will print 39
```

#### The `''.join()` functionality.

```python
print(stack.joinWith('')) # will work the same as ''.join(Some Iterable)
# BONUS: if the elements are not str, it will be forcefully
# typecasted to str.
```

#### STATIC METHODS

These methods don't need to an instance of `Stack` class.

```python
# suppose you want to call some static method named poopoo
# in the stack class.

from modstore.python import Stack

Stack.poopoo(*args, **kwargs) # and it will run

# *args and **kwargs means parameters
```

- Infix, Postfix, Prefix conversion

  ```python
  Stack.infixToPostfix("A+B*(C-D)")
  # will output -> "ABCD-*+"

  Stack.infixToPrefix("A+B*(C-D)")
  # will output -> "+A*B-CD"

  Stack.postfixToInfix("ABCD-*+") # "(A+(B*(C-D)))"

  Stack.postfixToPrefix("ABCD-*+") # "+A*B-CD"

  Stack.prefixToInfix("+A*B-CD") # "(A+(B*(C-D)))"

  Stack.prefixToPostfix("+A*B-CD") # "ABCD-*+"
  ```

  > And Yes, they support white spaces. -_-

- Roman Number and Number Conversion

  ```python
  Stack.resolveRomanNumber("MXCVII") # 1097

  Stack.generateRomanNumber(1097) # MXCVII
  ```

<p align='center'>
    <a href='../algorithms/#libraries'>Algorithms</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../builtins/#libraries'>Built-ins</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../rust/#libraries'>Rust</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../#libraries'>Go back</a>
</p>

[list]: https://d33p0st.in/documentation/libraries/modstore/builtins/#list-docs "modstore.python.list.List"