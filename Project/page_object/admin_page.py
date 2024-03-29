import time

import allure
from selenium.webdriver.common.by import By
from .BasePage import BasePage


class AdminPage(BasePage):
    catalog = (By.LINK_TEXT, 'Catalog')
    list_products = (By.LINK_TEXT, "Products")
    btn_add_new = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    product_name = (By.CSS_SELECTOR, '[placeholder = "Product Name"]')
    meta_tags_title = (By.CSS_SELECTOR, '[placeholder = "Meta Tag Title"]')
    tab_data = (By.LINK_TEXT, 'Data')
    model = (By.CSS_SELECTOR, '[placeholder = "Model"]')
    price = (By.CSS_SELECTOR, '[placeholder = "Price"]')
    quantity = (By.CSS_SELECTOR, '[placeholder = "Quantity"]')
    btn_save = (By.CSS_SELECTOR, '[data-original-title="Save"]')
    searh_name = (By.CSS_SELECTOR, '[placeholder = "Product Name"]')
    btn_filter = (By.CSS_SELECTOR, '#button-filter')
    search_body = (By.XPATH, '//tr')
    first_element_in_search = (By.XPATH, '//tbody//input')
    btn_delete = (By.CSS_SELECTOR, '.btn-danger')
    no_result_search = (By.XPATH, '//td[text()="No results!"]')

    def create_product(self):
        self._verify_element_presence(self.catalog).click()
        self._verify_element_presence(self.list_products).click()
        self._verify_button(self.btn_add_new).click()

    def fill_in_the_field(self):
        self._verify_element_presence(self.product_name).send_keys("test_product1")
        self._verify_element_presence(self.meta_tags_title).send_keys("tag_test_product1")
        self._verify_element_presence(self.tab_data).click()
        self._verify_element_presence(self.model).send_keys("test_model1")
        self._verify_element_presence(self.price).send_keys("100")
        self._verify_element_presence(self.quantity).send_keys("99")
        self._verify_element_presence(self.btn_save).click()

    def checking_the_creation(self):
        self._verify_element_presence(self.searh_name).send_keys("test_product1")
        self._verify_button(self.btn_filter).click()
        if len(self._all_elements(self.search_body)) < 2:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Object not created")
        if len(self._all_elements(self.search_body)) > 2:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Too many objects in search list")

    def delete_product(self):
        self._verify_element_presence(self.first_element_in_search).click()
        self._verify_button(self.btn_delete).click()
        self._accept_allert()

    def checking_product_is_delete(self):
        self._verify_element_presence(self.no_result_search)


