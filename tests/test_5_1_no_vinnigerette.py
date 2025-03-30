import unittest
import importlib.util
import os
from unittest.mock import patch


def load_no_vinnigrette():
    file_path = os.path.join(os.path.dirname(__file__), '../src/5.1.no_vinnigrette.py')
    spec = importlib.util.spec_from_file_location("no_vinnigrete", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.no_vinnigrete


no_vinnigrette = load_no_vinnigrette()


class MyTestCase(unittest.TestCase):

    @patch("builtins.print")
    @patch("random.randint", return_value=0)  # Always choose the first day
    def test_print(self, mock_rand, mock_print):
        no_vinnigrette("2023-07-10", "2023-07-10")  # Monday
        mock_print.assert_called_once_with("Ain't gettin' no vinaigrette today :(")


if __name__ == '__main__':
    unittest.main()
