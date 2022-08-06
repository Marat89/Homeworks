import pytest
from selenium import webdriver
import os
import logging

from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

DRIVERS = os.path.expanduser("~/Downloads")

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
    parser.addoption("--executor", action="store", default="172.17.0.1")
    parser.addoption("--run", action="store", default="remote")
    parser.addoption("--url", action="store", default="http://192.168.72.131:8081/")


@pytest.fixture
def base_url(request):
    url = request.config.getoption("--url", default="http://192.168.72.131:8081/")
    return url


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")

    executor_url = f"http://{executor}:4444/wd/hub"
    run = request.config.getoption("--run")
    if run == "local":
        if browser == "chrome":
            driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
        elif browser == "firefox":
            driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")
        driver.maximize_window()
    if run == "remote":
        caps = {
            "browserName": browser,
            "screenResolution": "1920x1080"

        }
        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

    driver = EventFiringWebDriver(driver, MyListener())
    driver.test_name = request.node.name

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
