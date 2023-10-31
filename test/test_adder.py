import sys
sys.path.insert(0, "../src/")
from src.adder import add_numbers

def test_adder():
    res = add_numbers(5 + 5)
    # test will pass only if function returns 10
    assert res == 10, f"Should be 10, got: {res}"