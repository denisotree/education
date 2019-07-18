from datetime import datetime, timedelta, date
from pymongo import MongoClient
from pprint import pprint
from cbr_parser import parse_daily_courses

if __name__ == '__main__':

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['courses']
    courses_collection = db['courses_collection']

    step = timedelta(days=1)
    start = date.today() - step*2
    end = date.today()

    print('Запрашиваю данные')

    while start <= end:
        date = datetime.strftime(start, "%Y-%m-%d")
        daily_course = parse_daily_courses(date)
        for currency in daily_course:
            courses_collection[currency['code']]['values'].insert_one(
                {
                    'date': currency['date'],
                    'value': currency['value']
                }
            )
        start += step

    # if len(final_json) > 0:
    #
    #     print('Записываю данные в базу')
    #
    #     success = 0
    #
    #     for day in final_json:
    #         courses_collection.insert_one(day)
    #         success += 1
    #
    #     print(f'Готово! Я успешно добавил в базу {success} дней наблюдений')
    #
    # else:
    #     print('Для этих дат не найдено данных')
