from src.hello import hello

def test_hello():
    res = hello()
    assert res == "Hello World!", f"Should be Hello World!, got: {res}"