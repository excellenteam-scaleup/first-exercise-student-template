import unittest
import importlib.util
import os
import tempfile
from pathlib import Path


def load_thats_the_way():
    file_path = os.path.join(os.path.dirname(__file__), '../src/5.1.thats_the_way.py')
    spec = importlib.util.spec_from_file_location("thats_the_way", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.thats_the_way


thats_the_way = load_thats_the_way()


class MyTestCase(unittest.TestCase):

    def test_deep_file_filtering(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Create some test files
            filenames = [
                "deep_one.txt", "deep2.jpg", "not_deep.txt", "deep.png", "another.txt"
            ]
            expected = ["deep_one.txt", "deep2.jpg", "deep.png"]

            for fname in filenames:
                Path(tmp_dir, fname).touch()

            result = thats_the_way(tmp_dir)
            self.assertCountEqual(result, expected)  # Order doesn't matter


if __name__ == '__main__':
    unittest.main()
