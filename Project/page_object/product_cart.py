from selenium.webdriver.common.by import By
from .BasePage import BasePage


class ProductCart(BasePage):
    image = (By.CSS_SELECTOR, ".thumbnails")
    description = (By.CSS_SELECTOR, ".tab-content")
    write_bar = (By.CSS_SELECTOR, ".btn-group")
    btn_add_to_cart = (By.CSS_SELECTOR, "#button-cart")
    btn_wich_list_and_compare = (By.XPATH, '//*[@class="col-sm-4"]/div[@class="btn-group"]')

    def verify_page(self):
        self._verify_element_presence(self.image)
        self._verify_element_presence(self.description)
        self._verify_element_presence(self.write_bar)
        self._verify_element_presence(self.btn_wich_list_and_compare)
        self._verify_element_presence(self.btn_add_to_cart)
