import pytest
from postcodeverifier import is_valid_postal_code

# Test cases

def test_valid_postal_code():
    # Test for valid postal codes
    assert is_valid_postal_code("121426") == True
    assert is_valid_postal_code("523563") == True
    assert is_valid_postal_code("987654") == True
    assert is_valid_postal_code("123456") == True

def test_invalid_postal_code_out_of_range():
    # Test for out-of-range postal codes
    assert is_valid_postal_code("99999") == False  # Less than 6 digits
    assert is_valid_postal_code("000001") == False # Starts with 0
    assert is_valid_postal_code("1000000") == False # More than 6 digits

def test_invalid_postal_code_alternating_repetitive_pairs():
    # Test for postal codes with more than one alternating repetitive digit pair
    assert is_valid_postal_code("552523") == False
    assert is_valid_postal_code("121212") == False

def test_edge_cases():
    # Test for edge cases
    assert is_valid_postal_code("100000") == True  # Exact lower bound
    assert is_valid_postal_code("999999") == True  # Exact upper bound
    assert is_valid_postal_code("101010") == True  # One alternating pair
    assert is_valid_postal_code("010101") == False # Starts with zero
