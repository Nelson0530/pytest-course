# 預約疫苗系統
from datetime import datetime

begin = datetime(2021, 6, 14, 8, 0)

def book_vaccine():
    now = datetime.now()
    if now >= begin:
        return "開始預約"
    else:
        return "2021-6-14 08:00 才能預約"

if __name__ == '__main__':
    print(book_vaccine())
