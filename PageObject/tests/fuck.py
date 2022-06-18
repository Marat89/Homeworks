import time
from page_object.phone_catalog import PhoneCatalogs
from page_object.product_cart import ProductCart
from page_object.authorization_admin import AutorizationAdminPage
from page_object.user_registration import UserRegistration
from page_object.main_page import MainPage
from page_object.admin_page import AdminPage


def c_delete_product(driver, base_url):
    driver.get(f"{base_url}/admin")
    driver.maximize_window()
    AutorizationAdminPage(driver).admin_autorization()
    AdminPage(driver).create_product()
    AdminPage(driver).fill_in_the_field()
    AdminPage(driver).delete_product()
    time.sleep(7)



