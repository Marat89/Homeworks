import time

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locator))

        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _verify_button(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))

        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _all_elements(self, locator: tuple):
        try:
            return self.driver.find_elements(*locator)

        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _select_elements_by_index(self, locator: tuple, index: int = 0):
        try:
            return self.driver.find_elements(*locator)[index]

        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _accept_allert(self):
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()
