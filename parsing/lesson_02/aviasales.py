import requests
import json


def get_prices(city_dep, city_dest):

    req_params = requests.get(f'https://www.travelpayouts.com/widgets_suggest_params?q={city_dep}%20{city_dest}')
    req_params = json.loads(req_params.text)

    if req_params == {}:
        return 1

    dep_iata = req_params['origin']['iata']
    dest_iata = req_params['destination']['iata']

    req = requests.get(f"http://min-prices.aviasales.ru/calendar_preload?origin={dep_iata}&destination={dest_iata}&one_way=true")

    return json.loads(req.text)


dep = 'Санкт-Петербург'
dest = 'Москва'

flights = get_prices(dep, dest)

if flights != 1:
    print(f'Билеты из города {dep} в город {dest}')
    for fly in flights['best_prices']:
        if fly['actual']:
            print(f'Дата вылета: {fly["depart_date"]}')
            print(f'Стоимость: {fly["value"]}₽')
            print(f'Магазин: {fly["gate"]}')
            print('\n')
else:
    print('Вы ввели название города неверно')















