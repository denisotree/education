from .cbr_parser import get_daily_courses
from datetime import datetime, timedelta
from pymongo import MongoClient

if __name__ == '__main__':

    start_date = input('Start date: ')
    end_date = input('End date: ')

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['courses']
    courses_collection = db['courses_collection']
    date_index_collection = db['date_index_collection']

    start = datetime.strptime(start_date, '%d-%m-%Y')
    end = datetime.strptime(end_date, '%d-%m-%Y')
    step = timedelta(days=1)

    final_json = []

    print('Запрашиваю данные')

    while start <= end:
        date = datetime.strftime(start, "%Y-%m-%d")

        start += step
        if date_index_collection.count_documents({"date": date}) == 0:
            final_json.append(get_daily_courses(date))
        else:
            continue

    if len(final_json) > 0:

        print('Записываю данные в базу')

        success = 0

        for day in final_json:
            courses_collection.insert_one(day)
            success += 1

        print(f'Готово! Я успешно добавил в базу {success} значений')

    else:
        print('Запрошенные даты уже в базе')
