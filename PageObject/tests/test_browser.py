import time

from page_object.phone_catalog import PhoneCatalogs
from page_object.product_cart import ProductCart
from page_object.authorization_admin import AutorizationAdminPage
from page_object.user_registration import UserRegistration
from page_object.main_page import MainPage
from page_object.admin_page import AdminPage


def test_main_page(driver, base_url):
    driver.get(base_url)
    MainPage(driver).verify_page()


def test_phone_catalog(driver, base_url):
    driver.get(f"{base_url}/smartphone")
    PhoneCatalogs(driver).verify_page()


def test_poduct_cart(driver, base_url):
    driver.get(f"{base_url}/smartphone/htc-touch-hd")
    ProductCart(driver).verify_page()


def test_autorization_admin_page(driver, base_url):
    driver.get(f"{base_url}/admin")
    AutorizationAdminPage(driver).verify_page()


def test_user_registration_page(driver, base_url):
    driver.get(f"{base_url}index.php?route=account/register")
    UserRegistration(driver).verify_page()

def test_add_product(driver, base_url):
    driver.get(f"{base_url}/admin")
    driver.maximize_window()
    AutorizationAdminPage(driver).admin_autorization()
    AdminPage(driver).create_product()
    AdminPage(driver).fill_in_the_field()
    AdminPage(driver).checking_the_creation()

def test_delete_product(driver, base_url):
    driver.get(f"{base_url}/admin")
    driver.maximize_window()
    AutorizationAdminPage(driver).admin_autorization()
    AdminPage(driver).create_product()
    AdminPage(driver).fill_in_the_field()
    AdminPage(driver).delete_product()
    time.sleep(7)

def test_register_new_user(driver, base_url):
    driver.get(base_url)
    driver.maximize_window()
    MainPage(driver).swith_to_register_user()
    UserRegistration(driver).fill_in_the_field()
    UserRegistration(driver).checking_registration()
    time.sleep(3)








