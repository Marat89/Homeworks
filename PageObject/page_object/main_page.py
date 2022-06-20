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
    choice_currency = (By.CSS_SELECTOR, '[class="fa fa-caret-down"]')
    eur = (By.NAME, "EUR")
    check_eur = (By.XPATH, '//strong[text()="€"]')
    gbp = (By.NAME, "GBP")
    check_gbp = (By.XPATH, '//strong[text()="£"]')
    usd = (By.NAME, "USD")
    check_usd = (By.XPATH, '//strong[text()="$"]')

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

    def swich_currency(self):
        self._verify_element_presence(self.choice_currency).click()
        self._verify_element_presence(self.eur).click()
        self._verify_element_presence(self.check_eur)
        self._verify_element_presence(self.choice_currency).click()
        self._verify_element_presence(self.gbp).click()
        self._verify_element_presence(self.check_gbp)
        self._verify_element_presence(self.choice_currency).click()
        self._verify_element_presence(self.usd).click()
        self._verify_element_presence(self.check_usd)
