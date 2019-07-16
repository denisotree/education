from requests import get, post
from json import loads

key = 'AgAEA7qhabbwAAUEeqV5uB-pg05wruD-eCD-YoI'


def get_task_status(userid, apikey, host, taskid):
    url = get(
        url=f'https://api.webmaster.yandex.net/v4/user/{userid}/hosts/{host}/turbo/tasks/{taskid}',
        headers={'Authorization': f'OAuth {apikey}'}
    )
    return loads(url.text)


with open('tasks.txt', 'r') as f:

    tasks_list = loads(f.read())

    for task in tasks_list:
        taskid = task['task_id']
        current_status = get_task_status('1130000013702896', key, 'https:pravda-nn.ru:443', taskid)

        print(current_status['load_status'])
        print(current_status['errors'])


