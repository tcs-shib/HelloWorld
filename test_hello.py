from hello import say_hello

def test_say_hello():
    assert say_hello() == "Hello, World!"

def test_say_hello_not_empty():
    result = say_hello()
    assert result != "", "say_hello() should not return an empty string"

