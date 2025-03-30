import unittest
import importlib.util
import os


# Dynamically load group_by from src/6.5.group_by.py
def load_group_by():
    file_path = os.path.join(os.path.dirname(__file__), '../src/6.5.group_by.py')
    spec = importlib.util.spec_from_file_location("group_by_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.group_by


group_by = load_group_by()


class TestGroupBy(unittest.TestCase):

    def test_group_by_len(self):
        result = group_by(len, ["hi", "bye", "yo", "try"])
        expected = {2: ["hi", "yo"], 3: ["bye", "try"]}
        self.assertEqual(result, expected)

    def test_group_by_mod2(self):
        result = group_by(lambda x: x % 2, [1, 2, 3, 4, 5, 6])
        expected = {
            1: [1, 3, 5],
            0: [2, 4, 6]
        }
        self.assertEqual(result, expected)

    def test_group_by_first_letter(self):
        result = group_by(lambda s: s[0], ["apple", "apricot", "banana", "blueberry", "cherry"])
        expected = {
            'a': ["apple", "apricot"],
            'b': ["banana", "blueberry"],
            'c': ["cherry"]
        }
        self.assertEqual(result, expected)

    def test_group_by_empty(self):
        result = group_by(len, [])
        expected = {}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
