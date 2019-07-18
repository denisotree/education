from zeep import Client, Settings
import re


def parse_daily_courses(date: str):
    url = 'https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?WSDL'
    settings = Settings(force_https=False)
    client = Client(url, settings=settings)
    course_object = client.service.GetCursOnDate(date)
    courses_raw = course_object._value_1._value_1
    courses = []
    for val in courses_raw:
        courses.append({
            'code': val['ValuteCursOnDate']['VchCode'],
            'name': ' '.join(val['ValuteCursOnDate']['Vname'].split()),
            'num': int(re.sub(r'[^.\d]', '', str(val['ValuteCursOnDate']['Vnom']))),
            'date': date,
            'value': float(re.sub(r'[^.\d]', '', str(val['ValuteCursOnDate']['Vcurs'])))
        })
    output = courses
    return output
