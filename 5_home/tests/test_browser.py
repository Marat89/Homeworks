

def test_driver_get(driver, base_url):
    driver.get(base_url)
    assert driver.title == "Your Store"


