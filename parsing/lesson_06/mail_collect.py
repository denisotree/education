import os
from dotenv import load_dotenv
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

load_dotenv()

AUTH_EMAIL = os.environ['AUTH_EMAIL']
AUTH_PASS = os.environ['AUTH_PASS']


def get_mail_list():
    driver = webdriver.Safari()
    driver.get('https://passport.yandex.ru/auth/add')
    assert "Авторизация" in driver.title
    login_field = driver.find_element_by_id('passp-field-login')
    login_field.send_keys(AUTH_EMAIL)
    login_field.send_keys(Keys.RETURN)
    mail_list_clean_data = []
    while True:
        try:
            password_field = WebDriverWait(driver, 5).until(
                ec.presence_of_element_located((By.ID, 'passp-field-passwd'))
            )
            password_field.send_keys(AUTH_PASS)
            password_field.send_keys(Keys.RETURN)
        except:
            break
    driver.get('https://mail.yandex.ru/')
    while True:
        try:
            mail_list = WebDriverWait(driver, 7).until(
                ec.presence_of_all_elements_located((By.CLASS_NAME, 'mail-MessageSnippet-Content'))
            )
            assert "Входящие — Яндекс.Почта" in driver.title
        except:
            break
    for mail in mail_list:
        mail_sender_name = mail.find_element_by_class_name('mail-MessageSnippet-FromText').text
        mail_sender_email = mail.find_element_by_class_name('mail-MessageSnippet-FromText').get_attribute('title')
        mail_title = mail.find_element_by_class_name('mail-MessageSnippet-Item_subject')\
            .find_element_by_tag_name('span').text
        mail_first_line = mail.find_element_by_class_name('mail-MessageSnippet-Item_firstline')\
            .find_element_by_tag_name('span').text
        mail_list_clean_data.append(
            {
                'sender_name': mail_sender_name,
                'sender_email': mail_sender_email,
                'sender_title': mail_title,
                'sender_text': mail_first_line,
            }
        )

    return mail_list_clean_data


if __name__ == '__main__':

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['mail_list']
    mail_list_collection = db['mail_list_collection']

    mail_list_collection.insert_many(get_mail_list())
