import unittest
import importlib.util
import os


def load_communicating_vessels():
    file_path = os.path.join(os.path.dirname(__file__), '../src/5.4.communicating_vessels.py')  # Adjust if needed
    spec = importlib.util.spec_from_file_location("communicating_vessels", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


interleave = load_communicating_vessels().interleave
generator_interleave = load_communicating_vessels().generator_interleave


class MyTestCase(unittest.TestCase):

    def test_basic_merge(self):
        result = list(interleave('ab', [1, 2, 3], ('@', '%')))
        generator_result = list(generator_interleave('ab', [1, 2, 3], ('@', '%')))
        self.assertEqual(result, ['a', 1, '@', 'b', 2, '%', 3])

    def test_single_iterable(self):
        result = list(interleave([10, 20, 30]))
        generator_result = list(generator_interleave([10, 20, 30]))
        self.assertEqual(result, [10, 20, 30])
        self.assertEqual(generator_result, [10, 20, 30])

    def test_empty(self):
        result = list(interleave())
        self.assertEqual(result, [])

        generator_result = list(generator_interleave())
        self.assertEqual(generator_result, [])


if __name__ == '__main__':
    unittest.main()
