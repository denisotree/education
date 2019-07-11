from zeep import Client, Settings
import re


def get_daily_courses(date: str):
    url = 'https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?WSDL'
    settings = Settings(force_https=False)
    client = Client(url, settings=settings)
    course_object = client.service.GetCursOnDate(date)
    courses_raw = course_object._value_1._value_1
    courses = []
    for val in courses_raw:
        courses.append({
            'code': val['ValuteCursOnDate']['VchCode'],
            'value': float(re.sub(r'[^.\d]', '', str(val['ValuteCursOnDate']['Vcurs'])))
        })
    output = {
        'date': date,
        'courses': courses
    }
    return output


print(get_daily_courses('2019-07-10'))
