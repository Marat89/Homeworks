from selenium.webdriver.common.by import By
from .BasePage import BasePage


class PhoneCatalogs(BasePage):
    content = (By.CSS_SELECTOR, "#content")
    btn_list_view = (By.CSS_SELECTOR, "#list-view")
    product_cart = (By.CSS_SELECTOR, ".product-layout")
    advertising = (By.CSS_SELECTOR, ".swiper-viewport")
    sort_by = (By.XPATH, './/*[@class="col-md-4 col-xs-6"]//select')

    def verify_page(self):
        self._verify_element_presence(self.content)
        self._verify_element_presence(self.btn_list_view)
        self._verify_element_presence(self.product_cart)
        self._verify_element_presence(self.advertising)
        self._verify_element_presence(self.sort_by)
