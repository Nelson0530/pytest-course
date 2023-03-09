# 在單元測試之前先建立好物件或變數，可重複使用
import pytest

@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    '''return value for fixture.'''
    assert some_data == 42

def test_inc_data(some_data):
    '''Use fixture return value for a test.'''
    inc_data = some_data + 1
    assert inc_data == 43