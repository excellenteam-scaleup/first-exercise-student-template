import unittest
import importlib.util
import os


def load_running_2000():
    file_path = os.path.join(os.path.dirname(__file__), '../src/6.2.running_2000.py')
    spec = importlib.util.spec_from_file_location("running_2000_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.running_2000


running_2000 = load_running_2000()


class MyTestCase(unittest.TestCase):

    def test_print(self):
        duration = running_2000(print, "Hello")
        self.assertIsInstance(duration, float)
        self.assertGreaterEqual(duration, 0)

    def test_zip(self):
        duration = running_2000(zip, [1, 2, 3], [4, 5, 6])
        self.assertIsInstance(duration, float)
        self.assertGreaterEqual(duration, 0)

    def test_format(self):
        duration = running_2000("Hi {name}".format, name="Bug")
        self.assertIsInstance(duration, float)
        self.assertGreaterEqual(duration, 0)


if __name__ == '__main__':
    unittest.main()
