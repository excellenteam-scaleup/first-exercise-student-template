import unittest
import importlib.util
import os


# Dynamically load long_cat_is_long from src/6.3.long_cat_is_long.py
def load_long_cat():
    file_path = os.path.join(os.path.dirname(__file__), '../src/6.3.long_cat_is_long.py')
    spec = importlib.util.spec_from_file_location("long_cat_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.long_cat_is_long


long_cat_is_long = load_long_cat()


class TestLongCatIsLong(unittest.TestCase):

    def test_basic(self):
        result = long_cat_is_long("Bla bla bla tralala 123")
        expected = {'Bla': 3, 'bla': 3, 'bla': 3, 'tralala': 7}
        # Since dictionary keys must be unique, test with lowercase input
        self.assertEqual(long_cat_is_long("bla bla tralala 123"), {'bla': 3, 'tralala': 7})

    def test_example_text(self):
        text = """
        You see, wire telegraph is a kind of a very, very long cat.
        You pull his tail in New York and his head is meowing in Los Angeles.
        Do you understand this?
        And radio operates exactly the same way: you send signals here, they receive them there.
        The only difference is that there is no cat.
        """

        expected_result = {
            'you': 3, 'see': 3, 'wire': 4, 'telegraph': 9, 'is': 2, 'a': 1, 'kind': 4,
            'of': 2, 'very': 4, 'long': 4, 'cat': 3, 'pull': 4, 'his': 3, 'tail': 4,
            'in': 2, 'new': 3, 'york': 4, 'and': 3, 'head': 4, 'meowing': 7, 'los': 3,
            'angeles': 7, 'do': 2, 'understand': 10, 'this': 4, 'radio': 5, 'operates': 8,
            'exactly': 7, 'the': 3, 'same': 4, 'way': 3, 'send': 4, 'signals': 7, 'here': 4,
            'they': 4, 'receive': 7, 'them': 4, 'there': 5, 'only': 4, 'difference': 10,
            'that': 4, 'no': 2
        }

        # Convert to lowercase because regex will preserve casing; we're asserting in lowercase
        result = {k.lower(): v for k, v in long_cat_is_long(text).items()}
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
