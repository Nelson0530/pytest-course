import pytest

@pytest.fixture
def fixture_1():
    print("\n執行fixture_1")         # 執行順序 1
    yield 1
    print("\n執行fixture_1的teardown程式碼")        # 執行順序 6


@pytest.fixture
def fixture_2(fixture_1):
    print("\n執行fixture_2")               # 執行順序 2
    yield 2
    print("\n執行fixture_2的teardown程式碼")           # 執行順序 6


@pytest.fixture
def fixture_add(fixture_1, fixture_2):
    print("\n執行fixture_add")              # 執行順序 3
    result = fixture_1 + fixture_2
    yield result
    print("\n執行fixture_add的teardown程式碼")          # 執行順序 5


def test_demo(fixture_add):
    print("\n執行測試函式test_demo")            # 執行順序 4
    assert fixture_add == 3


if __name__ == '__main__':
    pytest.main(["-s"])