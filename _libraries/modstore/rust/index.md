---
layout: page
title: Rust Powered Data Structures
description: The index page for modstore's rust powered data structure
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
    <a href='../new/#libraries'>New</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../#libraries'>Go back</a>
</p>

## Table of Contents
{:.no_toc}

- TOC
{::options toc_levels="2,3,4" /}
{:toc}

## BlockChain Docs

Blockchain is a decentralized digital ledger that securely records transactions across multiple computers, ensuring data transparency, security and immutability. It's most well-known as the underlying technology behind cryptocurrencies like `Bitcoin`, but its use extends far beyond digital currencies to areas such as supply chain management, healthcare, security and much more.
{:.larger.text}

### Features

- **Immutability**: Once data is added to the blockchain, it is nearly impossible to alter without the consensus of the majority of nodes in the network, providing tamper resistance.

- **Consensus Mechanisms**:  Blockchain operates using consensus algorithms like Proof of Work (PoW) or Proof of Stake (PoS), ensuring that all nodes agree on the validity of transactions.

- **Chain Validation**: Includes functionality to ensure the blockchain remains valid and unaltered by checking block hashes and links.

- **Hashing**:  Implement cryptographic hashing (e.g., `SHA-256`) for generating unique block hashes.

- **Searching**: Search through the blockchain for specific blocks.

### Usage

Let us now jump to usage.

#### Importing the `Blockchain` class

```python
from modstore.rust import BlockChain
```

#### Creating an initial `BlockChain`

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

#### Adding Blocks in the `BlockChain`

To add a new block into the blockchain

```python
blockchain.addBlock(
    uniqueIdentifier='block1',
    data='Sample Data'
)
```

- `uniqueIdentifier`: Identifier for this block and its data.

- `data`: Data can be either bytes or str or any object. Except str, and excluding bytes any object will be converted to bytes.

#### Getting the length of the `BlockChain`

To get the length of the BlockChain,

```python
length_of_bc = blockchain.length
```

#### Checking validity and proof of work of the blockchain (in terms of difficulty)

As discussed [earlier](#creating-an-initial-blockchain), the blockchain will be created with a difficulty factor,

```python
validity: bool = blockchain.valid
```

This means whether the blockchain is consistent throughout or it has been tampered with.

**NOTE**: To tamper the blockchain the amount to computational power needed will be determined by the difficulty. To actually tamper even a simple blockchain, it would take a lot of computational power.

#### Searching the `BlockChain` for blocks.

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

#### Printing the BlockChain

```python
print(blockchain)
```

## DAG Docs

A Directed Acyclic Graph (DAG) is a data structure where nodes are connected by directed edges, and the graph has no cycles. This structure is often used in blockchain-like applications to overcome some of the limitations of traditional blockchains, such as scalability and transaction speed. DAGs enable asynchronous, non-linear processing of transactions, where multiple transactions can be confirmed simultaneously.
{:.larger.text}

### Features

- **No Mining**: In many DAG-based networks, there’s no need for miners, as transactions themselves play the role of confirming other transactions.

- **Scalability**: DAG-based systems can process multiple transactions simultaneously, leading to faster transaction times compared to traditional blockchains.

- **No Blocks**: Instead of grouping transactions into blocks, each transaction references one or more previous transactions, creating a web-like structure.

- **High Throughput**: Because of the parallel nature, DAG is highly suitable for applications requiring high throughput like IoT, micro-payments, or supply chain management.

### Usage

Now let us jump to usage.

- [import](#import-the-relevant-class)
- [Init](#init)
  - [Basic DAG](#basic-dag)
    - [Add Nodes](#add-nodes)
    - [Add Edges](#add-edges)
    - [List Edges and Nodes](#list-of-edges-and-nodes)
    - [Print/Get String Representation](#print-or-get-the-dag-in-string-form)
  - [Transaction Based DAG](#transaction-based-dag)
    - [Add Transaction](#add-transaction)
    - [Validity](#check-validity-of-the-dag-ledger)
    - [Get all Transactions](#get-all-transactions)
    - [Get a Transaction by Transaction ID](#get-a-transaction-by-id)
    - [Transaction Class](#transaction-class)

#### import the relevant class

```python
from modstore.rust import DAG
```

#### Init

Now there are two types of DAGs available under the DAG class.

> Basic DAG

##### Basic DAG

```python
dag: DAG.BasicDag = DAG(type='Basic')
# type parameter takes only two values.
# 'Basic' and `Transaction-Based`.
```

##### Add Nodes

```python
dag.addNode('A') # add node A
dag.addNode('B') # add node B
```

##### Add Edges

```python
# `addEdge` method returns True if Edge was added successfully else Returns False

if dag.addEdge('A', 'B'): # adds an edge between A and B
    print("Edge Added")

try:
    dag.addEdge('B', 'C') # will raise NotImplementedError
    # as 'C' was not added as a node.
except NotImplementedError:
    print("Edge was not added.")

if dag.addEdge('B', 'C', force=True): # this will add any 
    # node that is not added using `addNode` and then 
    # create an edge.
    print("Added Edge B->C")

# NOTE: Any Edge that you're trying to add, if that
# creates a cyclic Graph, it will return False.
if dag.addEdge('C', 'A'): # this creates a cycle
    # as A -> B, B -> C and we are trying to
    # C -> A. which is a cycle.
    print("Cycle Added") # code wont reach here.
else:
    # code will go here
    print("C -> A creates a Cycle and hence not allowed.")
```

##### List of Edges and Nodes

```python
all_edges = dag.edges # in the form [('A', 'B'), ('B', 'C')]
all_nodes = dag.nodes # in the form ['A', 'B', 'C']
```

##### Print or get the DAG in string form.

```python
# print
print(dag) # will print the dag.

# get in string form
string_representation = dag.toString
```

> Transaction Based DAG (Simulation of DAG used in [IOTA](https://www.iota.org)).

##### Transaction Based DAG

```python
dag: DAG.TransactionBased = DAG(type='Transaction-Based')
```

##### Add Transaction

```python
# NOTE: Transaction Data can be any of there:
# str, bytes, object (list, dict, class or any other object)

# INTERNAl WORKING: 
# If str | bytes are provided, it will be taken as it is.
# if object is provided, it will be converted to bytes
# using DAG.ObjectToBytes(obj) static method.
# similarly, when getting the transaction back from DAG,
# to get the original data back,
# it uses DAG.BytesToObject(bytes) to return the original
# object or str or bytes.

demo_transaction_id = dag.addTransaction(data = "This is a DEMO", parents = [])
```

##### Check Validity of the DAG Ledger.

```python
if dag.valid:
    print("Ledger is valid.")
else:
    print("Ledger is invalid.")
```

##### Get All Transactions

```python
all_transactions = dag.transactions # returns a list of all transaction ids
```

##### Get a Transaction by ID

```python
# NOTE: the `transaction` method returns a `Transaction` type
# value, which contains some inbuilt methods that can be callable to get info about the transaction.
```

```python
# Stubs for `transaction` method
    def transaction(self, id: str) -> Transaction:
        """`Returns a Transaction with id if exists else raises Value Error.`"""
        ...
```

```python
# get a transaction by ID
transaction = dag.transaction(id=demo_transaction_id) # returns a Transaction.
```

>> #### Transaction class

```python
# the Transaction type has three methods.

# method 1: id
id_of_transaction = transaction.id # str

# method 2: parents
parents_of_transaction = transaction.parents # list[str]

# method 3: data
# NOTE: The data as said earlier could be str | bytes | object.
transaction_data = transaction.data()

# NOTE: if str or bytes was passed, this method will return the same.
# IF Object was passed as a data it is better to use
# `return_original` parameter of the `transaction.data()` method.

transaction_data = transaction.data(return_original=True)
# this returns either str or bytes or object, whatever was
# used in original form.
```

<p align='center'>
    <a href='../algorithms/#libraries'>Algorithms</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../builtins/#libraries'>Built-ins</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../new/#libraries'>New</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='../#libraries'>Go back</a>
</p>