import ast
import os


def collect_first_py_in(dirpath):
    for root, dirs, files in os.walk(dirpath):
        for f in files:
            if f.endswith('.py') and not f.startswith('_'):
                return os.path.join(root, f)
    return None


def test_directories_exist_and_parse():
    dirs = [
        'data_structures',
        'sorts',
        'graphs',
        'dynamic_programming',
    ]

    parsed = 0
    for d in dirs:
        assert os.path.isdir(d), f"Directory missing: {d}"
        p = collect_first_py_in(d)
        assert p is not None, f"No python files found in {d}"
        with open(p, 'r', encoding='utf-8') as fh:
            src = fh.read()
        # ensure file parses (syntax check) but do NOT execute
        ast.parse(src)
        parsed += 1

    assert parsed >= 1
