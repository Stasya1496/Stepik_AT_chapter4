from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_ADD_TO_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages :nth-child(1) > .alertinner strong")
    MESSAGE_COST_OF_BASKET = (By.CSS_SELECTOR, '#messages :nth-child(3) > .alertinner p strong')


