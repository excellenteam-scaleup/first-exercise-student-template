import unittest
import importlib.util
import os


def load_parsle_tongue():
    file_path = os.path.join(os.path.dirname(__file__), '../src/5.3.parsle_tongue.py')  # Adjust path if needed
    spec = importlib.util.spec_from_file_location("parsle_tongue", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.parsle_tongue


parsle_tongue = load_parsle_tongue()


class MyTestCase(unittest.TestCase):

    def test_hidden_words_found(self):
        import os

        original_dir = os.getcwd()  # Save current directory
        print("Starting in:", os.getcwd())
        try:
            os.chdir("src")  # Change to new directory
            print("Now in:", os.getcwd())  # Perform actions in new directory

            result = parsle_tongue()

            expected_words = ['python', 'isawesome', 'welldone', 'goodjob']

            for word in expected_words:
                self.assertIn(word, result)
        finally:
            os.chdir(original_dir)  # Revert back
            print("Back to:", os.getcwd())


if __name__ == '__main__':
    unittest.main()
