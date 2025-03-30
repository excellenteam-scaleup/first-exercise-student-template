import unittest
import importlib.util
import os


def load_piece_of_cake():
    file_path = os.path.join(os.path.dirname(__file__), '../src/5.2.piece_of_cake.py')  # Adjust path as needed
    spec = importlib.util.spec_from_file_location("piece_of_cake", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.piece_of_cake


piece_of_cake = load_piece_of_cake()


class MyTestCase(unittest.TestCase):

    def test_skip_optional_item(self):
        result = piece_of_cake(
            prices={'milk': 20, 'chocolate': 18},
            optionals=['milk'],
            milk=200,
            chocolate=100
        )
        # milk is skipped, chocolate is 18/100 * 100 = 18
        self.assertEqual(result, 18.0)

    def test_no_optionals_all_included(self):
        result = piece_of_cake(
            prices={'bread': 25, 'jam': 10},
            optionals=[],
            bread=100,
            jam=50
        )
        # bread: 25/100 * 100 = 25
        # jam: 10/100 * 50 = 5
        self.assertEqual(result, 30.0)

    def test_empty_optionals_missing_key(self):
        result = piece_of_cake(
            prices={'bread': 25, 'jam': 10},
            optionals=['butter'],  # butter isn't in kwargs, so has no effect
            bread=100
        )
        # only bread is included: 25/100 * 100 = 25
        self.assertEqual(result, 25.0)

    def test_empty_everything(self):
        result = piece_of_cake(prices={}, optionals=[])
        self.assertEqual(result, 0.0)

    def test_zero_quantity(self):
        result = piece_of_cake(
            prices={'milk': 20},
            optionals=[],
            milk=0
        )
        self.assertEqual(result, 0.0)


if __name__ == '__main__':
    unittest.main()
