import pytest
from selenium import webdriver
import os
import logging

from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

DRIVERS = os.path.expanduser("~/Documents/Developer/drivers")

logger = logging.getLogger(__name__)

f = logging.FileHandler("Project/logs/test.log")
logger.addHandler(f)
logger.setLevel(logging.DEBUG)


class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        logger.info(f"I'm navigating to {url} and {driver.title}")

    def after_navigate_to(self, url, driver):
        logger.info(f"I'm on {url}")

    def before_find(self, by, value, driver):
        logger.info(f"I'm looking for '{value}' with '{by}'")

    def after_find(self, by, value, driver):
        logger.info(f"I've found '{value}' with '{by}'")

    def before_click(self, element, driver):
        logger.info(f"I'm clicking {element}")

    def after_click(self, element, driver):
        logging.info(f"I've clicked {element}")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="http://192.168.72.130")
    parser.addoption("--log_level", action="store", default="DEBUG")


# parser.addoption("--run", action="store", default="local")


@pytest.fixture
def base_url(request):
    url = request.config.getoption("--url", default="http://192.168.72.130:8081/")
    return url


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    # run = request.config.getoption("--run")
    # if run == "local":
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")
    # if run == "remote":
    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities={"browserName": browser, "platformName": "LINUX"}
    )
    # else:
    #   raise ValueError("Wrong attribute")

    #driver = EventFiringWebDriver(driver, MyListener())
    #driver.test_name = request.node.name

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
