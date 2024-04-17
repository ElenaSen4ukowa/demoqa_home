import time
from pages.swag_labs import SwagLabs

def test_check_swag_labs_icon(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()                  # переход на страницу https://www.saucedemo.com/
    time.sleep(3)
    assert swag_labs_page.exist_icon()      # проверка наличия иконки swag_labs

def test_check_input_user_name(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()                  # переход на страницу https://www.saucedemo.com/
    time.sleep(3)
    assert swag_labs_page.exist_name()      # проверка наличия поля "Имя"

def test_check_input_password(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()                  # переход на страницу https://www.saucedemo.com/
    time.sleep(3)
    assert swag_labs_page.exist_password()  # проверка наличия поля "Пароль"

