import unittest
import importlib.util
import os


def load_cup_of_join():
    file_path = os.path.join(os.path.dirname(__file__), '../src/5.2.cup_of_join.py')  # adjust path as needed
    spec = importlib.util.spec_from_file_location("cup_of_join_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.cup_of_join


cup_of_join = load_cup_of_join()


class MyTestCase(unittest.TestCase):

    def test_no_separator(self):
        result = cup_of_join([1, 2], ['a', 'b'], [True])
        self.assertEqual(result, [1, 2, 'a', 'b', True])

    def test_with_separator(self):
        result = cup_of_join([1, 2], ['a'], [True, False], sep='-')
        self.assertEqual(result, [1, 2, '-', 'a', '-', True, False, '-'])

    def test_empty_lists(self):
        result = cup_of_join([], [1], [], sep='x')
        self.assertEqual(result, ['x', 1, 'x', 'x'])

    def test_single_list(self):
        result = cup_of_join(['only'], sep='-')
        self.assertEqual(result, ['only', '-'])


if __name__ == '__main__':
    unittest.main()
