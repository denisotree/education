# coding utf-8

from pymongo import MongoClient
from slugify import slugify

client = MongoClient('mongodb://127.0.0.1:27017')
db = client['hh_positions']


def positions_compensation_filter(request, compensation):

    try:
        compensation = int(compensation)
    except ValueError:
        print('Вы ввели неверное значение зарплаты')

    request = slugify(request, to_lower=True, separator='_')

    positions_collection = db[request]

    positions = positions_collection.find({'compensation_start': {"$gt": compensation}}).sort('compensation_start')

    positions_len = positions_collection.count_documents({})

    if positions_len > 0:
        for position in positions:
            print(position)
    else:
        print('Я не нашел таких вакансий')


if __name__ == "__main__":

    collections = db.list_collection_names({})

    print('В базе данных следующие вакансии:')

    for collection in collections:
        print(collection)

    print('Название вакансии можно вводить на киррилице')

    r = input('\nВведите название вакансии: ')

    c = input('Введите минимальную зарплату: ')

    positions_compensation_filter(r, c)
