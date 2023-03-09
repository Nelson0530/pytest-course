# 預約疫苗系統 unit test 如何擷取系統時間
import pytest

from mock_system_time.mock_system_time import book_vaccine

# 此範例會出現error!!
# ==============================================================================
# def test_book_b4_begin_time(mocker):
#     fake_time = datetime(2021, 6, 14, 7, 59)
#     mocker.patch('datetime.now', return_value=fake_time)
#     result = book_vaccine()
#     assert result == "2021-6-14 08:00 才能預約"
#
# def test_book_after_begin_time(mocker):
#     fake_time = datetime(2021, 6, 14, 8, 0)
#     mocker.patch('datetime.now', return_value=fake_time)
#     result = book_vaccine()
#     assert result == "開始預約"
# ===========================================================================

# 正確範例:使用 pytest-freezegun
@pytest.mark.freeze_time("2021-06-14 7:59")
def test_book_b4_begin_time(mocker):
    result = book_vaccine()
    assert result == "2021-6-14 08:00 才能預約"

@pytest.mark.freeze_time("2021-06-14 8:00")
def test_book_after_begin_time():
    result = book_vaccine()
    assert result == "開始預約"
