from page_object.pages import main_page
from page_object.pages import phone_catalogs
from page_object.pages import product_cart
from page_object.pages import admin_page
from page_object.pages import user_registration
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(driver, base_url):
    driver.get(base_url)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(main_page.currency_bar))
    assert driver.title == "Your Store"
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(main_page.currency_bar))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(main_page.links))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(main_page.basket))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(main_page.desctop))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(main_page.product_card_btn))


def test_phone_catalog(driver, base_url):
    driver.get(f"{base_url}/smartphone")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(phone_catalogs.content))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(phone_catalogs.btn_list_view))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(phone_catalogs.product_cart))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(phone_catalogs.advertising))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(phone_catalogs.sort_by))


def test_poduct_cart(driver, base_url):
    driver.get(f"{base_url}/smartphone/htc-touch-hd")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(product_cart.image))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(product_cart.description))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(product_cart.write_bar))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(product_cart.btn_add_to_cart))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(product_cart.btn_wich_list_and_compare))


def test_admin_page(driver, base_url):
    driver.get(f"{base_url}/admin")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(admin_page.password))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(admin_page.username))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(admin_page.btn_login))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(admin_page.forgoten_password))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(admin_page.logo))


def test_user_registration_page(driver, base_url):
    driver.get(f"{base_url}index.php?route=account/register")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(user_registration.placeholder_first_name))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(user_registration.placeholder_last_name))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(user_registration.placeholder_email))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(user_registration.placeholder_telephone))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(user_registration.btn_continue))
