from selenium.webdriver.common.by import By

from .BasePage import BasePage


class MainPage(BasePage):
    currency_bar = (By.CSS_SELECTOR, ".pull-left")
    links = (By.CSS_SELECTOR, "#top-links")
    basket = (By.CSS_SELECTOR, "#cart")
    desctop = (By.XPATH, './/ul[@class ="nav navbar-nav"]/li[1]')
    product_card_btn = (By.XPATH, './/*[@class="product-thumb transition"]/div[@class="button-group"]')
    my_account = (By.CSS_SELECTOR, '[class="fa fa-user"]')
    register_new_user = (By.LINK_TEXT, 'Register')

    def verify_page(self):
        self._verify_element_presence(self.currency_bar)
        self._verify_element_presence(self.links)
        self._verify_element_presence(self.basket)
        self._verify_element_presence(self.desctop)
        self._verify_element_presence(self.product_card_btn)
        return self

    def swith_to_register_user(self):
        self._verify_element_presence(self.my_account).click()
        self._verify_element_presence(self.register_new_user).click()
