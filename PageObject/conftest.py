import pytest
from selenium import webdriver
import os
import logging

from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

DRIVERS = os.path.expanduser("~/Documents/Developer/drivers")

logger = logging.getLogger(__name__)


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
    parser.addoption("--executor", action="store", default="http://192.168.72.130:8081/")
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture
def base_url(request):
    url = request.config.getoption("--url", default="http://192.168.72.130:8081/")
    return url


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    log_level = request.config.getoption("--log_level")

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")
    else:
        driver = webdriver.Remote(
            command_executor="http://{}:4444/wd/hub".format(executor),
            desired_capabilities={"browserName": browser}
        )

    driver = EventFiringWebDriver(driver, MyListener())
    driver.test_name = request.node.name
    driver.log_level = log_level

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
