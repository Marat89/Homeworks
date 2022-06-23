from selenium.webdriver.common.by import By
from .BasePage import BasePage
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


class UserRegistration(BasePage):
    placeholder_first_name = (By.CSS_SELECTOR, '#input-firstname')
    placeholder_last_name = (By.CSS_SELECTOR, '#input-lastname')
    placeholder_email = (By.CSS_SELECTOR, '#input-email')
    placeholder_telephone = (By.CSS_SELECTOR, '#input-telephone')
    btn_continue = (By.CSS_SELECTOR, '.btn-primary')
    password = (By.CSS_SELECTOR, '[placeholder="Password"]')
    confirm_password = (By.CSS_SELECTOR, '[placeholder="Password Confirm"]')
    agree_privacy = (By.CSS_SELECTOR, '[name="agree"]')
    succes_registration = (By.LINK_TEXT, 'Your Account Has Been Created!')

    def verify_page(self):
        self._verify_element_presence(self.placeholder_first_name)
        self._verify_element_presence(self.placeholder_last_name)
        self._verify_element_presence(self.placeholder_email)
        self._verify_element_presence(self.placeholder_telephone)
        self._verify_element_presence(self.btn_continue)

    def fill_in_the_field(self):
        self._verify_element_presence(self.placeholder_first_name).send_keys('Ivan')
        self._verify_element_presence(self.placeholder_last_name).send_keys('Ivanov')
        self._verify_element_presence(self.placeholder_email).send_keys(f"{generate_random_string(5)}@mail.ru")
        self._verify_element_presence(self.placeholder_telephone).send_keys('=79876543212')
        self._verify_element_presence(self.password).send_keys('123456')
        self._verify_element_presence(self.confirm_password).send_keys('123456')
        self._verify_element_presence(self.agree_privacy).click()
        self._verify_element_presence(self.btn_continue).click()

    def checking_registration(self):
        assert self.browser.title == "Your Account Has Been Created!"
