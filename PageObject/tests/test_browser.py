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
    browser.get(f"{base_url}/smartphone")
    PhoneCatalogs(browser).verify_page()


def test_poduct_cart(browser, base_url):
    browser.get(f"{base_url}/smartphone/htc-touch-hd")
    ProductCart(browser).verify_page()


def test_autorization_admin_page(browser, base_url):
    browser.get(f"{base_url}/admin")
    AutorizationAdminPage(browser).verify_page()


def test_user_registration_page(browser, base_url):
    browser.get(f"{base_url}index.php?route=account/register")
    UserRegistration(browser).verify_page()


def test_add_product(browser, base_url):
    browser.get(f"{base_url}/admin")
    browser.maximize_window()
    AutorizationAdminPage(browser).admin_autorization()
    AdminPage(browser).create_product()
    AdminPage(browser).fill_in_the_field()
    AdminPage(browser).checking_the_creation()
    AdminPage(browser).delete_product()
    time.sleep(1)  #если не подождать, не проходит удаление


def test_delete_product(browser, base_url):
    browser.get(f"{base_url}/admin")
    browser.maximize_window()
    AutorizationAdminPage(browser).admin_autorization()
    AdminPage(browser).create_product()
    AdminPage(browser).fill_in_the_field()
    AdminPage(browser).checking_the_creation()
    AdminPage(browser).delete_product()
    AdminPage(browser).checking_product_is_delete()


def test_register_new_user(browser, base_url):
    browser.get(base_url)
    browser.maximize_window()
    MainPage(browser).swith_to_register_user()
    UserRegistration(browser).fill_in_the_field()
    UserRegistration(browser).checking_registration()


def test_swith_currency(browser, base_url):
    browser.get(base_url)
    browser.maximize_window()
    MainPage(browser).swich_currency()
