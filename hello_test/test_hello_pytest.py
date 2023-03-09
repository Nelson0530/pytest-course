# pytest語法想較容易，不用再使用class
from hello import hello_name

def test_hello_pytest():
    assert hello_name("Nelson") == "Hello, Nelson"