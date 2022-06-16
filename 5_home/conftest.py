import pytest
from selenium import webdriver
import os


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://192.168.72.130:8081/")
    parser.addoption("--drivers", default=os.path.expanduser("~/Documents/Developer/drivers"))


@pytest.fixture
def base_url(request):
    url = request.config.getoption("--url")
    return url


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    if browser_name == "chrome":
        browser = webdriver.Chrome(executable_path=f"{drivers}/chromedriver")
    elif browser_name == "firefox":
        browser = webdriver.Firefox(executable_path=f"{drivers}/geckodriver")
    elif browser_name == "opera":
        browser = webdriver.Opera(executable_path=f"{drivers}/operadriver")
    else:
        print("Wrong browser")
    yield browser
    browser.close()
