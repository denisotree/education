import requests
from bs4 import BeautifulSoup as bs
import sys
import os

'''

@:arg position — list of str

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
    pagination_container = html.findAll("span", {"class": "bloko-button-group"})
    pagination_count = pagination_container[0].findAll('', {"data-qa": "pager-page"})
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
        compensation = position_html.find('div', {"data-qa": "vacancy-serp__vacancy-compensation"}).text
    except AttributeError:
        compensation = ''

    output = {
        'title': title,
        'link': link,
        'employer_title': emp_title,
        'employer_link': f'https://spb.hh.ru{emp_url}',
        'compensation': compensation
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
                else:
                    filename = filename + "_" + arg

        output_positions_list = get_positions_list(request)

        if len(output_positions_list) > 0:

            if not os.path.exists('output'):
                os.makedirs('output')

            f = open(f'./output/{filename}_output_file.html', 'w')
            html_header = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>{request} positions</title>
            </head>
            <body>
            <div class="position__body">
                <table>
                    <thead>
                        <tr>
                            <th>Наименование вакансии</th>
                            <th>Работодатель</th>
                            <th>Зарплата</th>
                        </tr>
                    </thead>
                    <tbody>
            """
            html_footer = f"""
                 </tbody>
                    </table>
                </div>    
            </body>
            </html>
            """
            print('Выгружаю данные в файл')
            f.write(html_header)
            for position in output_positions_list:
                position_html = f"""
                <tr>
                    <td class="position__title"><a href="{position['link']}">{position['title']}</a></td>
                    <td class="position__employer">
                        <a href="{position['employer_link']}">{position['employer_title']}</a>
                    </td>
                    <td class="position__compensation">{position['compensation']}</td>
                </tr>
                """
                f.write(position_html)
            f.write(html_footer)
            f.close()
            print(f'Все готово! Результаты поиска доступны в файле output/{filename}_output_file.html')
        else:
            print('Я не нашел вакансий по вашему запросу')
