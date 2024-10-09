import pytest
from count import print_even_numbers

def test_print_even_numbers(capsys):
    # Call the function
    print_even_numbers()

    # Capture the output
    captured = capsys.readouterr()

    # Verify the output
    assert captured.out == "2\n4\n6\n8\n10\n"