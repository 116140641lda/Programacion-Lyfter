import unittest
from Logic_main import FinancialManager
from validation import text_validation, amount_validation


class FinancialTest(unittest.TestCase):

    def setUp(self):
        self.manage = FinancialManager()

    def test_add_category(self):
        self.manager.add_category("Food")
        self.assertEqual(len(self.manager.categories), 1)

    def test_save_categorie_check_save(self):
        self.manage.add_category("Food")
        self.assertEqual(len(self.manage.categories), 1)

    def test_add_category_not_duplicate(self):
        self.manage.add_category("Food")
        with self.assertRaises(ValueError):
            self.manage.add_category("Food")

    def test_add_movement_with_category(self):
        with self.assertRaises(ValueError):
            self.manage.add_movements("Dinner", 20, "Food", "Expense")

    def test_add_movement_check(self):
        self.manage.add_category("Food")
        self.manage.add_movements("Dinner", 20, "Food", "Expense")
        self.assertEqual(len(self.manage.movements), 1)

    def test_text_validation_correct(self):
        self.assertTrue(text_validation("Hi"))

    def test_text_validation_incorrect(self):
        self.assertFalse(text_validation(""))

    def test_amount_validation_correct(self):
        self.assertTrue(amount_validation("10"))

    def test_amount_validation_incorrect(self):
        self.assertFalse(amount_validation("-5"))


if __name__ == "__main__":
    unittest.main()