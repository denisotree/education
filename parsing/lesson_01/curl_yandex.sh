#!/usr/bin/env bash

# Запрос забирает rss фид с новостного сайта

curl -v https://pravda-nn.ru/feed/turbo/?paged=3

# Этот запрос запрашивает у Яндекса адрес, на который отправлять фид

curl -X GET \
  'https://api.webmaster.yandex.net/v4/user/1130000013702896/hosts/https:pravda-nn.ru:443/turbo/uploadAddress?mode=DEBUG' \
  -H 'Authorization: OAuth key'