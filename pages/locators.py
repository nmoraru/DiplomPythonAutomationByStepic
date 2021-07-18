from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LINK_TEXT = 'login'

class ProductPageLocators():
    BUTTON_FOR_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_TO_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div > .alert-success:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_TO_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div > .alert-info strong")