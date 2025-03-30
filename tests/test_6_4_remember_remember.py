import unittest
import importlib.util
import os


def load_remember_remember():
    file_path = os.path.join(os.path.dirname(__file__), '../src/6.4.remember_remember.py')
    spec = importlib.util.spec_from_file_location("remember_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.remember_remember


remember_remember = load_remember_remember()


class TestRememberRemember(unittest.TestCase):

    def test_hidden_message(self):
        img_path = os.path.join(os.path.dirname(__file__), '../src/code.png')
        message = remember_remember(img_path)

        expected_message = "Place gunpowder beneath the House of Lords. 11/05/1605"
        self.assertEqual(message, expected_message)


if __name__ == '__main__':
    unittest.main()
