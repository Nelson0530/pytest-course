import pytest

@pytest.fixture()
def set_up_and_post_condition():
    print("pre condition")
    yield
    print("post condition")

def test(set_up_and_post_condition):
    print("Body of test!")
