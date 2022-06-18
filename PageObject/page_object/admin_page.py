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
    first_element_in_search = (By.CSS_SELECTOR, '[type="checkbox"]')
    btn_delete = (By.CSS_SELECTOR, '.btn-danger')

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
            raise AssertionError("Object not created")
        if len(self._all_elements(self.search_body)) > 2:
            raise AssertionError("Too many objects")

    def delete_product(self):
        self._verify_element_presence(self.searh_name).send_keys("test_product1")
        self._verify_button(self.btn_filter).click()
        self._select_elements_by_index(self.first_element_in_search, 1).click()
        self._verify_button(self.btn_delete).click()
        self._accept_allert(self)
        # (self.driver.switch_to.alert).accept
