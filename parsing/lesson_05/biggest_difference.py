from datetime import datetime, timedelta, date
from pymongo import MongoClient
from pprint import pprint
import math


def date_str_to_iso(date_str):
    y, m, d = date_str.split('-')
    return datetime(int(y), int(m), int(d))


currency_dict = {
    'AUD': 'Австралийский доллар',
    'AZN': 'Азербайджанский манат',
    'AMD': 'Армянских драмов',
    'BYN': 'Белорусский рубль',
    'BGN': 'Болгарский лев',
    'BRL': 'Бразильский реал',
    'HUF': 'Венгерских форинтов',
    'KRW': 'Вон Республики Корея',
    'HKD': 'Гонконгских долларов',
    'DKK': 'Датских крон',
    'USD': 'Доллар США',
    'EUR': 'Евро',
    'INR': 'Индийских рупий',
    'KZT': 'Казахстанских тенге',
    'CAD': 'Канадский доллар',
    'KGS': 'Киргизских сомов',
    'CNY': 'Китайских юаней',
    'MDL': 'Молдавских леев',
    'TMT': 'Новый туркменский манат',
    'NOK': 'Норвежских крон',
    'PLN': 'Польский злотый',
    'RON': 'Румынский лей',
    'XDR': 'СДР (специальные права заимствования)',
    'SGD': 'Сингапурский доллар',
    'TJS': 'Таджикских сомони',
    'TRY': 'Турецкая лира',
    'UZS': 'Узбекских сумов',
    'UAH': 'Украинских гривен',
    'GBP': 'Фунт стерлингов Соединенного королевства',
    'CZK': 'Чешских крон',
    'SEK': 'Шведских крон',
    'CHF': 'Швейцарский франк',
    'ZAR': 'Южноафриканских рэндов',
    'JPY': 'Японских иен'
}

if __name__ == '__main__':

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['courses']
    try:
        start_date = date_str_to_iso(input('Введите дату начала поиска в формате yyyy-mm-dd: '))
        end_date = date_str_to_iso(input('Введите дату окончания поиска в формате yyyy-mm-dd: '))

        for collection in db.list_collection_names():
            collection_values = db[collection].find({
                'date': {
                    '$gte': start_date,
                    '$lt': end_date
                }
            })
            max_val = math.inf
            max_val_date = 0
            min_val = 0
            min_val_date = 0
            for val in collection_values:
                if val['value'] > max_val:
                    max_val = val['value']
                    max_val_date = val['date']
                if val['value'] < min_val:
                    min_val = val['value']
                    min_val_date = val['date']

            diff = max_val - min_val

            print(f'Валюту {currency_dict.get(collection)} выгодно было купить {min_val_date},'
                  f' а продать {max_val_date}. Прибыль: {diff}')

    except ValueError:
        print('Вы ввели неверную дату')
