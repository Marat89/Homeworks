import pytest
from selenium import webdriver

DRIVERS = "~/Documents/Developer/drivers"

def test_first():
    browser = webdriver.Chrome(executable_path="/home/mtest/Documents/Developer/drivers/chromedriver")
    browser.get("http://192.168.72.130:8081/")
    assert browser.title == "Your Store"