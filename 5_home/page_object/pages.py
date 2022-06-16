from selenium.webdriver.common.by import By


class main_page:
    currency_bar = (By.CSS_SELECTOR, ".pull-left")
    links = (By.CSS_SELECTOR, "#top-links")
    basket = (By.CSS_SELECTOR, "#cart")
    desctop = (By.XPATH, './/ul[@class ="nav navbar-nav"]/li[1]')
    product_card_btn = (By.XPATH, './/*[@class="product-thumb transition"]/div[@class="button-group"]')


class phone_catalogs:
    content = (By.CSS_SELECTOR, "#content")
    btn_list_view = (By.CSS_SELECTOR, "#list-view")
    product_cart = (By.CSS_SELECTOR, ".product-layout")
    advertising = (By.CSS_SELECTOR, ".swiper-viewport")
    sort_by = (By.XPATH, './/*[@class="col-md-4 col-xs-6"]//select')


class product_cart:
    image = (By.CSS_SELECTOR, ".thumbnails")
    description = (By.CSS_SELECTOR, ".tab-content")
    write_bar = (By.CSS_SELECTOR, ".btn-group")
    btn_add_to_cart = (By.CSS_SELECTOR, "#button-cart")
    btn_wich_list_and_compare = (By.XPATH, '//*[@class="col-sm-4"]/div[@class="btn-group"]')


class admin_page:
    username = (By.XPATH, '//*[@name="username"]')
    password = (By.XPATH, '//*[@name="password"]')
    forgoten_password = (By.CSS_SELECTOR, '.help-block')
    btn_login = (By.CSS_SELECTOR, '.btn-primary')
    logo = (By.CSS_SELECTOR, '.navbar-brand')


class user_registration:
    placeholder_first_name = (By.CSS_SELECTOR, '#input-firstname')
    placeholder_last_name = (By.CSS_SELECTOR, '#input-lastname')
    placeholder_email = (By.CSS_SELECTOR, '#input-email')
    placeholder_telephone = (By.CSS_SELECTOR, '#input-telephone')
    btn_continue = (By.CSS_SELECTOR, '.btn-primary')
