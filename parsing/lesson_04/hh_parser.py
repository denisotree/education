import requests
import re
from bs4 import BeautifulSoup as bs
import sys
from pymongo import MongoClient
from slugify import slugify

'''

:arg position — list of str

'''

# Функция получает на вход запрос str и номер текущей страницы int


def get_search_page(request, page):
    api_host = 'https://spb.hh.ru/search/vacancy'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko)' \
                 'Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    params = {
        "text": '"' + request + '"',
        "search_field": "name",
        "items_on_page": 100,
        "only_with_salary": "true",
        "page": page
    }

    print(f'Запрашиваю данные c {page + 1} страницы')

    html = requests.get(api_host, params=params, headers=headers).text
    parsed_html = bs(html, 'lxml')
    return parsed_html


# Функция выбирает из сырого HTML блок с результатами поиска


def get_raw_positions(html):
    positions_page_raw_list = html.findAll("div", {"data-qa": "vacancy-serp__vacancy"})
    return positions_page_raw_list


# Функция выбирает из сырого HTML блок с ссылками на страницы пагинации и возвращает их количество


def get_pages_count(html):
    try:
        pagination_container = html.findAll("span", {"class": "bloko-button-group"})
        pagination_count = pagination_container[0].findAll('', {"data-qa": "pager-page"})
        return len(pagination_count)
    except IndexError:
        pagination_count = []
        return len(pagination_count)


# Функция перебирает карточки вакансий, выдергивая из них нужные нам данные. Пакует все в json


def get_clean_position_data(position_html):
    position_data = position_html.find('a', {"data-qa": "vacancy-serp__vacancy-title"})
    title = position_data.text
    link = position_data['href']
    emp_data = position_html.find('a', {"data-qa": "vacancy-serp__vacancy-employer"})
    emp_title = emp_data.text
    emp_url = emp_data['href']
    try:
        compensation = position_html.find('div', {"data-qa": "vacancy-serp__vacancy-compensation"}).text.replace(u'\xa0', ' ')
        compensation_clean = re.sub(r"[^-\d]", "", compensation).split("-")
        if len(compensation_clean) > 1:
            compensation_start = int(compensation_clean[0])
            compensation_end = int(compensation_clean[1])
        else:
            compensation_start = int(compensation_clean[0])
            compensation_end = ''
    except AttributeError:
        compensation_start = ''
        compensation_end = ''

    output = {
        'title': title,
        'link': link,
        'employer_title': emp_title,
        'employer_link': f'https://spb.hh.ru{emp_url}',
        'compensation_start': compensation_start,
        'compensation_end': compensation_end,
    }

    return output


# Основная функция — вызывает все предыдущие и возвращает json со всеми вакансиями


def get_positions_list(request):
    clean_positions_list = []

    first_page_parsed_html = get_search_page(request, 0)

    positions = get_raw_positions(first_page_parsed_html)

    pages_count = get_pages_count(first_page_parsed_html)

    if pages_count > 1:
        for i in range(1, pages_count):
            html = get_search_page(request, i)
            new_positions = get_raw_positions(html)
            positions.extend(new_positions)

    for position in positions:
        clean_positions_list.append(get_clean_position_data(position))

    return clean_positions_list


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Передайте аргументом название вакансии в виде: "python hh_parser.py Python developer"')
    else:
        request = ''
        filename = ''
        for i, arg in enumerate(sys.argv):
            if i > 0:
                request = request + " " + arg
                if i == 1:
                    filename = arg
                    filename = slugify(filename, to_lower=True, separator='_')
                else:
                    filename = filename + "_" + arg
                    filename = slugify(filename, to_lower=True, separator='_')

        output_positions_list = get_positions_list(request)

        client = MongoClient('mongodb://127.0.0.1:27017')

        db = client['hh_positions']

        positions_collection = db[filename]

        if len(output_positions_list) > 0:

            print('Записываю данные в базу')
            for position in output_positions_list:

                if positions_collection.find({"title": position['title']}).count() == 0:
                    positions_collection.insert_one(position)
                else:
                    continue
            print('Готово!')

        else:
            print('Я не нашел вакансий по вашему запросу')
