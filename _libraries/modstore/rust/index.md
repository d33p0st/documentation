---
layout: page
title: Rust Powered Data Structures
description: The index page for modstore's rust powered data structure
---

<p align='center'>
    <a href='./algorithms/#libraries'>Algorithms</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='./builtins/#libraries'>Built-ins</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='./new/#libraries'>New</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../'>Go back</a>
</p>

###### modstore
{:.no_toc}

# {{ page.title }}
{:.no_toc}

## Table of Contents
{:.no_toc}

- TOC
{::options toc_levels="2,3" /}
{:toc}

## BlockChain Docs

Blockchain is a decentralized digital ledger that securely records transactions across multiple computers, ensuring data transparency, security and immutability. It's most well-known as the underlying technology behind cryptocurrencies like `Bitcoin`, but its use extends far beyond digital currencies to areas such as supply chain management, healthcare, security and much more.

### Features

- **Immutability**: Once data is added to the blockchain, it is nearly impossible to alter without the consensus of the majority of nodes in the network, providing tamper resistance.

- **Consensus Mechanisms**:  Blockchain operates using consensus algorithms like Proof of Work (PoW) or Proof of Stake (PoS), ensuring that all nodes agree on the validity of transactions.

- **Chain Validation**: Includes functionality to ensure the blockchain remains valid and unaltered by checking block hashes and links.

- **Hashing**:  Implement cryptographic hashing (e.g., `SHA-256`) for generating unique block hashes.

- **Searching**: Search through the blockchain for specific blocks.

### Usage

Let us now jump to usage.

###### Importing the `Blockchain` class

```python
from modstore.rust import BlockChain
```

###### Creating an initial `BlockChain`

To create a blockchain, 

```python
blockchain = BlockChain(
    difficulty=5,
    timezone='IST'
)
```

- `difficulty`: The difficulty specifies how many leading zeros are required for a block's hash to be considered valid. A higher difficulty makes it more computationally expensive to find a valid hash, thereby regulating the time between block generations and maintaining the security of the blockchain. During the mining process (`mine` method (Internally)), the block repeatedly computes its hash until the first `difficulty` characters of the hash match the required pattern (i.e., a string of `0`s). This process involves trial and error, and the number of iterations needed depends on the difficulty level.

- `timezone`: This parameter sets the timezone of the timestamp to be used in each block. This parameter takes literals ['UTC', 'IST'] or `"HH:MM:SS"` to be added to UTC to get the desired timezone.


<span>{% include icon.liquid id='info-circle' %} <b>Note</b></span><br>  The above code will create one `Genesis` Block to initiate the blockchain. This is the first block in the blockchain.
{:.ui.info.message}

###### Adding Blocks in the `BlockChain`

To add a new block into the blockchain

```python
blockchain.addBlock(
    uniqueIdentifier='block1',
    data='Sample Data'
)
```

- `uniqueIdentifier`: Identifier for this block and its data.

- `data`: Data can be either bytes or str or any object. Except str, and excluding bytes any object will be converted to bytes.

###### Getting the length of the `BlockChain`

To get the length of the BlockChain,

```python
length_of_bc = blockchain.length
```

###### Checking validity and proof of work of the blockchain (in terms of difficulty)

As discussed [earlier](#creating-an-initial-blockchain), the blockchain will be created with a difficulty factor,

```python
validity: bool = blockchain.valid
```

This means whether the blockchain is consistent throughout or it has been tampered with.

**NOTE**: To tamper the blockchain the amount to computational power needed will be determined by the difficulty. To actually tamper even a simple blockchain, it would take a lot of computational power.

###### Searching the `BlockChain` for blocks.

```python
try:
    expected_block = blockchain.search(identifier='block1')
except Exception as e:
    print('Failed to find block - block1')
```

The `expected_block` will be of the type `Block` and will have a few methods and properties of it's own.

- index (property)
- timestamp (property)
- identifier (property)
- previous_hash (property)
- hash (property)
- data (method)
  - return_original (param) (bool)
    
    If `return_original` parameter of `data` method of `Block` class is set to `False`, data will be returned in either `str` or `bytes`. Now it wont be a problem if the data was originally `str` or `bytes`. But if the data was originally an `object`, it will be returned as `bytes`. To simply avoid any confusion, just set it to `True`.

##### Printing the BlockChain

```python
print(blockchain)
```

## DAG Docs



<p align='center'>
    <a href='./algorithms/#libraries'>Algorithms</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='./builtins/#libraries'>Built-ins</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='./new/#libraries'>New</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../'>Go back</a>
</p>