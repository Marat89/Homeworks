from selenium.common import TimeoutException

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait





class BasePage:
    def __init__(self, browser):

        self.browser = browser
       # self.driver = driver


    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 1).until(EC.visibility_of_element_located(locator))

        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _verify_button(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 3).until(EC.element_to_be_clickable(locator))

        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _all_elements(self, locator: tuple):
        try:
            return self.browser.find_elements(*locator)

        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _select_elements_by_index(self, locator: tuple, index: int = 0):
        try:
            return self.browser.find_elements(*locator)[index]

        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _accept_allert(self):
        alert = self.browser.switch_to.alert
        print(alert.text)
        alert.accept()
