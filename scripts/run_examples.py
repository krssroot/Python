#!/usr/bin/env python3
"""
scripts/run_examples.py

Lightweight utility to find example python files under given directories and
verify they compile (using py_compile) without executing them. Safe for CI.
"""

import argparse
import os
import sys
import py_compile


def find_first_py(directory):
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith('.py') and not f.startswith('_'):
                return os.path.join(root, f)
    return None


def main():
    parser = argparse.ArgumentParser(description='Find and compile example python files')
    parser.add_argument('--dirs', nargs='+', default=['data_structures', 'sorts', 'graphs'],
                        help='List of directories to search (relative to repo root)')
    args = parser.parse_args()

    found = 0
    for d in args.dirs:
        if not os.path.isdir(d):
            print(f'SKIP: directory not found: {d}', file=sys.stderr)
            continue
        path = find_first_py(d)
        if not path:
            print(f'NO PY FILE: {d}')
            continue
        try:
            py_compile.compile(path, doraise=True)
            print(f'OK: compiled {path}')
            found += 1
        except py_compile.PyCompileError as e:
            print(f'FAIL: compile error in {path}: {e}', file=sys.stderr)

    if found == 0:
        print('No example files compiled successfully.', file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    main()
