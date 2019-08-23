from .controllers import date_controller, get_human_date

actionmapping = [
    {'action': 'humandate', 'controller': get_human_date},
    {'action': 'date', 'controller': date_controller},
]
