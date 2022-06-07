import unittest
from main import main_menu,order,view_cart,cancel_order,view_order

class TestCart(unittest.TestCase):
    def test_menu(self):
        """
        Test whether the menu shows
        """
        self.assertTrue(main_menu())
    def test_order(self):
        """
        Test whether one can order
        """
        test_data = { "item": "towel", "quantity": 2 }
        self.assertTrue(order(test_data))
    def test_view_cart(self):
        """
        Test whether the cart can be viewed
        """
        self.assertTrue(view_cart())
    def test_order(self):
        """
        Test whether the order can be cancelled
        """
        self.assertTrue(cancel_order())
    def test_order(self):
        """
        Test whether the order can be viewed
        """
        self.assertTrue(view_order())

if __name__ == '__main__':
    unittest.main()