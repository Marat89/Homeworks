import allure
from selenium.common import TimeoutException

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):

        self.browser = browser

    @allure.step("Проверяю наличие элемента по локатору: {locator}")
    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 1).until(EC.visibility_of_element_located(locator))

        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Cant find element by locator: {}".format(locator))

    @allure.step("Проверяю наличие кнопки по локатору: {locator}")
    def _verify_button(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 3).until(EC.element_to_be_clickable(locator))

        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Cant find element by locator: {}".format(locator))

    @allure.step("Ищу несколько  элементов по локатору: {locator}")
    def _all_elements(self, locator: tuple):
        try:
            return self.browser.find_elements(*locator)

        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Cant find element by locator: {}".format(locator))

    @allure.step("Ищу элемент из множества по идексу {index} по локатору: {locator}")
    def _select_elements_by_index(self, locator: tuple, index: int = 0):
        try:
            return self.browser.find_elements(*locator)[index]

        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Cant find element by locator: {}".format(locator))

    @allure.step("Подтверждаю действие  а аллерте")
    def _accept_allert(self):
        alert = self.browser.switch_to.alert
        print(alert.text)
        alert.accept()
