from requests import get, post
from json import loads

key = 'key'


def get_upload_url(userid, apikey, host):
    url = get(
        url=f'https://api.webmaster.yandex.net/v4/user/{userid}/hosts/https:{host}:443/turbo/uploadAddress?mode=DEBUG',
        headers={'Authorization': f'OAuth {apikey}'}
    )
    return loads(url.text)


def post_rss_to_yandex(upload_url, apikey, post_data):
    return post(
        url=upload_url,
        headers={
            'Authorization': f'OAuth {apikey}',
            'Content-Type': 'application/rss+xml',
        },
        data=post_data.encode('utf-8')
    )


for i in range(5, 70):
    data = get(f'https://pravda-nn.ru/feed/turbo/?paged={i}')

    url_data = get_upload_url('1130000013702896', key, 'pravda-nn.ru')

    url = url_data['upload_address']

    print(post_rss_to_yandex(url, key, data.text))
