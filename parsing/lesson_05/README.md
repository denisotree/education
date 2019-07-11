# Сервис сравнения курсов валют

cbr_parser.py — тут лежит функция, собирающая данные из XML Сбербанка. Принимает строковую дату следующего формата — 'd-m-Y'. Возвращает словарь с курсами валют по запрошенной дате.

master_of_pain.py — функция, вызывающая страдания. Она ответит, когда нужно было покупать и продавать какую валюту, чтобы быть сейчас невероятно богатым. Принимает начальную и конечную дату в виде d-m-Y.

### Установка и запуск MongoDB

#### 1. Установка и запуск Docker
Если у вас уже установлен Docker, перейдите к следующему шагу

##### Ubuntu

Введите в терминал последовательно следующие команды:

`sudo apt-get update`

`sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D`

`sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'`

`sudo apt-get update`

`sudo apt-get install -y docker-engine`

Мы установили Docker, проверим, что процесс запущен

`sudo systemctl status docker`

##### MacOS

Загрузите [десктопное приложение Docker](https://download.docker.com/mac/stable/Docker.dmg) из официального репозитория

Установите, следуя указаниям системы

##### Windows

Загрузите [десктопное приложение Docker](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe) из официального репозитория

Установите, следуя указаниям системы

#### 2. Установка docker-compose
Если у вас уже установлен docker-compose, перейдите к следующему шагу

##### Ubuntu

Введите в терминал последовательно следующие команды:

`curl -L https://github.com/docker/compose/releases/download/1.8.0/run.sh > /usr/local/bin/docker-compose`

`chmod +x /usr/local/bin/docker-compose`

Проверяем установку

`docker-compose --version`

##### MacOS

Docker compose уже включен в приложение docker

##### Windows

Docker compose уже включен в приложение docker

#### 3. Запуск MongoDB

Теперь нужно создать файл окружения:

`nano .env`

И вставить туда переменные с логином и паролем от базы данных (логин и пароль установите свои):

`USER=dbuser`

`PASSWORD=dbpassword`

Осталась ерунда — нужно запустить контейнер следующей командой:

`docker-compose up --build -d`



