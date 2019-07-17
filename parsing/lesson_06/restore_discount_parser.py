from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def get_goods_list():
    driver = webdriver.Safari()
    driver.get('https://www.re-store.ru/discount')
    assert "Распродажа витринных образцов" in driver.title
    choose_city_btn = driver.find_element_by_class_name('choose-another-city')
    choose_city_btn.click()
    city_btn_list = driver.find_elements_by_class_name('city')
    for city in city_btn_list:
        if city.get_attribute('data-name') == "Санкт-Петербург":
            city.click()
            break

    # btns_more = driver.find_elements_by_class_name('r-discount-section__btn-more')
    # for btn in btns_more:
    #     btn.click()


if __name__ == '__main__':
    get_goods_list()
