def valid_letter() -> str:
    '''
    Prompts the user for a column between 'a' and 'g'.
    Continuously asks for a valid letter if invalid data is provided.
    '''
    while True:
        column = input("What column do you wish to select from a to g? ")
        if ord(column) in range(ord('a'), ord('g') + 1):
            return column
        print("Your input is invalid")


from unittest.mock import Mock, patch

from ..main import main_menu

def test_valid_letter() -> None:
    with patch('builtins.input', new=Mock(return_value='a')):
        assert valid_letter() == 'a'
    with patch('builtins.input', new=Mock(side_effect=['z', 'q', 'g', 'c'])):
        assert main_menu() == {'key': 'value'}


test_valid_letter()