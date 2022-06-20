from selenium.webdriver.common.by import By
from .BasePage import BasePage


class AutorizationAdminPage(BasePage):
    username = (By.XPATH, '//*[@name="username"]')
    password = (By.XPATH, '//*[@name="password"]')
    forgoten_password = (By.CSS_SELECTOR, '.help-block')
    btn_login = (By.CSS_SELECTOR, '.fa-key')
    logo = (By.CSS_SELECTOR, '.navbar-brand')

    def verify_page(self):
        self._verify_element_presence(self.username)
        self._verify_element_presence(self.password)
        self._verify_element_presence(self.forgoten_password)
        self._verify_element_presence(self.btn_login)
        self._verify_element_presence(self.logo)

    def admin_autorization(self):
        self._verify_element_presence(self.username).send_keys("user")
        self._verify_element_presence(self.password).send_keys("bitnami")
        self._verify_button(self.btn_login).click()
