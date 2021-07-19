from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn:nth-child(1)")
    BASKET_PRODUCTS = (By.CSS_SELECTOR, ".basket-items")
    TEXT_FROM_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")

class LoginPageLocators():
    EMAIL_ADRESS = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LINK_TEXT = 'login'
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_FOR_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_TO_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div > .alert-success:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_TO_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div > .alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div > .alert-success")
