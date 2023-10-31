import sys
sys.path.insert(0, "../src/")
from src.hello import hello

def test_hello():
    res = hello()
    # test will pass only if function returns "Hello World!"
    assert res == "Hello World!", f"Should be Hello World!, got: {res}"