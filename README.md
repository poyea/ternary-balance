# Ternary Balance System
> Given an integer N, find a way to balance the integer with weights from the set {1, 3, 9, 27, ...}, i.e. the powers of 3.

![Ternary Balance](https://github.com/poyea/ternary-balance/workflows/Ternary%20Balance/badge.svg)

  * [Features](#features)
  * [Getting started](#getting-started)
  * [Usage](#usage)
  * [Run tests](#run-tests)
  * [Build the documentation](#build-the-documentation)
  * [Style](#style)
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
$ python -m venv ternary
```
Install the requirement:
```
(ternary) $ pip install -r requirements.txt
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
(ternary) $ cd ternary_balance/utils
(ternary) $ python numerics.py -v
```

## Build the documentation
To use Sphinx with Napoleon,
```
(ternary) $ cd docs
(ternary) $ sphinx-apidoc --version
sphinx-apidoc 3.0.3
(ternary) $ sphinx-apidoc -o . ..
(ternary) $ make html
```
The documentation is available in `docs/_build`.

## Style
To format the code, run
```
(ternary) $ black .
```

## License
MIT


