# Ternary Balance System
> Given an integer N, find a way to balance the integer with weights from the set {1, 3, 9, 27, ...}, i.e. the powers of 3.
  
  * [Features](#features)
  * [Getting started](#getting-started)
  * [Usage](#usage)
  * [Run tests](#run-tests)
  * [Build the documentation](#build-the-documentation)
  * [License](#license)


## Features
* Solve the ternary balance problem
* Provide numeric utilities for exploration and testing

## Getting started
Make sure your Python is up-to-date:
```
$ python --version
Python 3.8.2
```
Set up a python environment:
```
python -m venv ternary
```
Install the requirement:
```
pip install -r requirements.txt
```

## Usage
One query:
```python
from ternary_balance.solver import ternary_balance

solver = ternary_balance()
solver.solve()
```
Many queries:
```python
from ternary_balance.solver import ternary_balance

solver = ternary_balance()
for _ in range(10):
    solver.solve()
```

## Run tests
To run the doctests,
```
$ cd ternary_balance/utils
$ python numerics.py -v
```

## Build the documentation
To use Sphinx with Napoleon,
```
$ cd docs
$ sphinx-apidoc --version
sphinx-apidoc 3.0.3
$ sphinx-apidoc -o . ..
$ make html
```
The documentation is available in `docs/_build`.

## License
MIT


