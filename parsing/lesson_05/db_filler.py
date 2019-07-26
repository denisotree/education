from datetime import datetime, timedelta, date
from pymongo import MongoClient
from cbr_parser import parse_daily_courses


def date_str_to_iso(date_str):
    y, m, d = date_str.split('-')
    return datetime(int(y), int(m), int(d))


if __name__ == '__main__':

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['courses']

    step = timedelta(days=1)
    start = date(2009, 1, 1)
    end = date.today()

    print('Запрашиваю данные')
    i = 0
    while start <= end:
        date = datetime.strftime(start, "%Y-%m-%d")
        daily_course = parse_daily_courses(date)
        for currency in daily_course:
            update_data ={
                    'date': date_str_to_iso(currency['date']),
                    'num': currency['num'],
                    'value': currency['value']
            }
            if db[currency['code']].count_documents({'date': currency['date']}) == 0:
                db[currency['code']].insert_one(update_data)
        start += step
        i += 1

    print(f'Добавлены курсы валют за {i} дней')
