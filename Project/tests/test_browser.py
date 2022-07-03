import time

from page_object.phone_catalog import PhoneCatalogs
from page_object.product_cart import ProductCart
from page_object.authorization_admin import AutorizationAdminPage
from page_object.user_registration import UserRegistration
from page_object.main_page import MainPage
from page_object.admin_page import AdminPage


def test_main_page(browser, base_url):
    browser.get(base_url)
    MainPage(browser).verify_page()


def test_phone_catalog(browser, base_url):
    """Тест проверки элементов страницы каталога телефонов
    1. Наличие основного контента
    2. Кнопка преключения отображения контента
    3. Карточка продукта
    4. Предложение под навигационной панелью
    5. Кнопка сортировки"""

    browser.get(f"{base_url}/smartphone")
    PhoneCatalogs(browser).verify_page()


def test_poduct_cart(browser, base_url):
    """Тест проверки элементов страницы продукта
    1. Изображение продукта
    2. Описание продукта
    3. Выбор валюты
    4. Добавить в карзину
    5. Набор кнопок"""
    browser.get(f"{base_url}/smartphone/htc-touch-hd")
    ProductCart(browser).verify_page()


def test_autorization_admin_page(browser, base_url):
    """Тест проверки элементов страницы авторизации администратора
       1. Поле ввода логина
       2. Поле ввода пароля
       3. Ссылка на восстановление пароля
       4. Кнопка входа в админку
       5. Логотип"""
    browser.get(f"{base_url}/admin")
    AutorizationAdminPage(browser).verify_page()


def test_user_registration_page(browser, base_url):
    """Тест проверки элементов страницы регистрации нового пользователя
           1. Поле ввода имени
           2. Поле ввода фамилии
           3. Поле ввода почты
           4. Поле ввода телефона
           5. Кнопка регистрации"""
    browser.get(f"{base_url}index.php?route=account/register")
    UserRegistration(browser).verify_page()


def test_add_product(browser, base_url):
    """Тест добавления нового продукта
            Шаги:
               1. Авторизация под админом
               2. Переход на страницу добавления продукта
               3. Заполнение обязательных полей
               4. Проверка создания продукта
               5. Удаление продукта"""
    browser.get(f"{base_url}/admin")
    AutorizationAdminPage(browser).admin_autorization()
    AdminPage(browser).create_product()
    AdminPage(browser).fill_in_the_field()
    AdminPage(browser).checking_the_creation()
    AdminPage(browser).delete_product()
    time.sleep(1)  # если не подождать, не проходит удаление


def test_delete_product(browser, base_url):
    """Тест удаления продукта
               Шаги:
                  1. Авторизация под админом
                  2. Переход на страницу добавления продукта
                  3. Заполнение обязательных полей
                  4. Проверка создания продукта
                  5. Удаление продукта
                  6. Проверка удаления продукта"""

    browser.get(f"{base_url}/admin")
    AutorizationAdminPage(browser).admin_autorization()
    AdminPage(browser).create_product()
    AdminPage(browser).fill_in_the_field()
    AdminPage(browser).checking_the_creation()
    AdminPage(browser).delete_product()
    AdminPage(browser).checking_product_is_delete()


def test_register_new_user(browser, base_url):
    """Тест регистрации нового пользователя
               Шаги:
                  1. Переход на старницу регистрации нового пользователя
                  2. Заполнение обязательных полей
                  3. Проверка регистрации пользователя"""
    browser.get(base_url)
    MainPage(browser).swith_to_register_user()
    UserRegistration(browser).fill_in_the_field()
    UserRegistration(browser).checking_registration()


def test_swith_currency(browser, base_url):
    """Тест переключения валюты
               Шаги:
                  1. Переключение валюты на евро
                  2. Переключение валюты на фунты
                  3. Переключение валюты на доллар
                  """
    browser.get(base_url)
    MainPage(browser).swich_currency()
