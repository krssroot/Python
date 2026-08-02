<div align="center">

# The Algorithms — Python (krssroot/Python)

[![Repository Size](https://img.shields.io/github/repo-size/krssroot/Python?style=flat-square)](https://github.com/krssroot/Python)
[![License](https://img.shields.io/github/license/krssroot/Python?style=flat-square)](https://github.com/krssroot/Python/blob/master/LICENSE.md)
[![Top Language](https://img.shields.io/github/languages/top/krssroot/Python?style=flat-square)](https://github.com/krssroot/Python)
[![Last Commit](https://img.shields.io/github/last-commit/krssroot/Python?style=flat-square)](https://github.com/krssroot/Python/commits)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=flat-square)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/static/v1?label=code%20style&message=ruff&color=black&style=flat-square)](https://github.com/charliermarsh/ruff)
[![CI](https://img.shields.io/github/actions/workflow/status/krssroot/Python/build.yml?branch=master&style=flat-square)](https://github.com/krssroot/Python/actions/workflows/build.yml)
[![Ruff CI](https://img.shields.io/github/actions/workflow/status/krssroot/Python/ruff.yml?branch=master&style=flat-square)](https://github.com/krssroot/Python/actions/workflows/ruff.yml)
[![Docs](https://img.shields.io/github/actions/workflow/status/krssroot/Python/sphinx.yml?branch=master&style=flat-square)](https://github.com/krssroot/Python/actions/workflows/sphinx.yml)

</div>

# All Algorithms implemented in Python

A curated collection of algorithm implementations in Python — organized by topic and intended for education, learning, and experimentation.

- Repository: krssroot/Python (forked from TheAlgorithms)
- Description: All Algorithms implemented in Python

## Table of contents

- [About](#about)
- [Badges & Status](#badges--status)
- [Quick links](#quick-links)
- [Repository structure](#repository-structure)
- [How to use](#how-to-use)
- [Examples runner](#examples-runner)
- [Development & Tests](#development--tests)
- [Contributing](#contributing)
- [License](#license)

## About

This repository collects implementations of common algorithms and data structures in Python. It's primarily aimed at learners who want readable, straightforward implementations to study algorithmic ideas. Implementations may prioritize clarity over micro-optimizations.

## Badges & Status

- Top-level badges show repository size, license, language, last commit.
- CI workflows are present (.github/workflows/*): build, ruff, sphinx documentation. Badges above link to their workflow pages.
- Linters and pre-commit hooks are configured (see .pre-commit-config.yaml and pyproject.toml).
- A development container is provided in .devcontainer for a reproducible contributor environment.

## Quick links

- Data structures: https://github.com/krssroot/Python/tree/master/data_structures
- Graph algorithms: https://github.com/krssroot/Python/tree/master/graphs
- Sorting algorithms: https://github.com/krssroot/Python/tree/master/sorts
- Dynamic programming: https://github.com/krssroot/Python/tree/master/dynamic_programming
- Machine learning: https://github.com/krssroot/Python/tree/master/machine_learning

Feel free to open DIRECTORY.md for a full, grouped listing.

## Repository structure

Top-level directories (annotated):

```text
.devcontainer/        Development container configuration and README
.github/              GitHub workflows and issue templates (CI and automation)
.vscode/              VSCode workspace settings
audio_filters/        Audio processing filter examples
backtracking/         Backtracking algorithm implementations
bit_manipulation/     Bit-level algorithms and helpers
blockchain/           Simple blockchain examples / educational
boolean_algebra/      Boolean algebra utilities and examples
cellular_automata/    Cellular automata (e.g., Game of Life)
ciphers/              Classic cipher implementations
computer_vision/      Basic computer vision algorithms and demos
conversions/          Unit and base conversions
data_compression/     Compression and decompression algorithms
data_structures/      Implementations of common data structures
digital_image_processing/ Image processing utilities
divide_and_conquer/   Algorithms using divide-and-conquer paradigms
docs/                 Documentation and guides
dynamic_programming/  Classic DP algorithm examples
electronics/          Educational electronics/math utilities
file_transfer/        File transfer examples and utilities
financial/            Financial algorithms and calculators
fractals/             Fractal generation examples
fuzzy_logic/          Fuzzy logic examples
genetic_algorithm/    Genetic algorithm examples
geodesy/              Geodesy and geospatial utilities
geometry/             Computational geometry algorithms
graphics/             Graphics demos and helpers
graphs/               Graph algorithms (BFS, DFS, Dijkstra, etc.)
greedy_methods/       Greedy algorithm implementations
hashes/               Hashing algorithms and examples
knapsack/             Knapsack problem solutions
linear_algebra/       Linear algebra routines
linear_programming/   Simple LP solvers and examples
machine_learning/     Educational ML algorithms (from-scratch)
maths/                Math utilities and helpers
matrix/               Matrix algorithms and helpers
networking_flow/      Network flow algorithms
neural_network/       From-scratch neural network examples
other/                Miscellaneous examples
physics/              Physics-related simulations/algorithms
project_euler/        Solutions / helpers for Project Euler problems
quantum/              Quantum algorithms and demos (educational)
scheduling/           Scheduling algorithms and examples
scripts/              Utility scripts used by the repository
searches/             Searching algorithms and examples
sorts/                Sorting algorithms
strings/              String algorithms and utilities
uv.lock               Dependency lock (UV project file)
pyproject.toml        Project metadata and tooling configuration
index.md              Simple index / landing page
```

> For a navigable list of algorithms see DIRECTORY.md which groups implementations by topic.

## How to use

Clone the repository:

```bash
git clone https://github.com/krssroot/Python.git
cd Python
```

Use the development container (recommended for contributors):

- Open this repository in VS Code and select "Reopen in Container" when prompted (requires Docker + Remote - Containers extension).

Run linters and formatting checks locally:

```bash
python -m pip install --user pre-commit
pre-commit install
pre-commit run --all-files
# or
ruff check .
```

Examples: check a single algorithm file compiles (safe smoke check):

```bash
python -m py_compile sorts/example_sort.py  # replace with an existing file
```

## Examples runner

A lightweight utility that finds the first Python example in a set of categories and verifies it compiles (safe, non-executing check):

```bash
python scripts/run_examples.py --dirs data_structures sorts graphs dynamic_programming
```

This will report which example files were found and verify they compile without executing their runtime code.

## Development & Tests

The repository uses pyproject.toml for tooling configuration and pre-commit hooks (see .pre-commit-config.yaml).

To run the smoke tests (provided below) locally:

```bash
python -m pip install -r requirements-dev.txt || true
python -m pip install pytest
pytest -q
```

The included tests are lightweight and perform syntax/parsing checks on representative files so they are fast and safe to run.

## Contributing

Thank you for considering contributing!

[![Contributions Welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square)](CONTRIBUTING.md)

1. Read CONTRIBUTING.md to learn the contribution process and coding standards.
2. Pick an issue labeled "good first issue" or open a new issue to propose changes.
3. Follow code style and run pre-commit hooks before submitting a PR.

Contributing checklist (short):
- Fork the repository
- Create a descriptive branch name
- Implement tests or example usage where applicable
- Keep implementations clear and educational

## License

This project follows the license in LICENSE.md. See the license file for details.

---

If you'd like, I can also open a dedicated PR that adds more example runner coverage, or expand the tests to actually import and run small, isolated functions with timeouts. Let me know which categories you want deeper test coverage for.