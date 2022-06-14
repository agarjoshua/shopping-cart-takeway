# import unittest
from unittest import TestCase
import unittest
from unittest.mock import Mock, patch
# from main import main_menu,order,view_cart,cancel_order,view_order

from unittest.mock import Mock, patch

def valid_letter():
    '''
    Prompts the user for a column between 'a' and 'g'.
    Continuously asks for a valid letter if invalid data is provided.
    '''
    while True:
        column = input("What column do you wish to select from a to g? ")
        if ord(column) in range(ord('a'), ord('g') + 1):
            return column
        print("Your input is invalid")


def test_valid_letter():
    with patch('builtins.input', new=Mock(return_value='1')):
        assert valid_letter == '3'
    with patch('builtins.input', new=Mock(side_effect=['z', 'q', 'g', 'c'])):
        assert valid_letter == 'g'


test_valid_letter()


if __name__ == '__main__':
    test_valid_letter()