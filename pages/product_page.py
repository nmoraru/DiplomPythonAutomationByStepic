from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_correct_success_message(self):
        self.should_be_correct_product_name_to_success_message()
        self.shoul_be_correct_product_price_to_success_message()
        
    def add_product_to_basket(self):
        button_for_add_product_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_FOR_ADD_PRODUCT_TO_BASKET)
        button_for_add_product_to_basket.click()

    def should_be_correct_product_name_to_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_to_success_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TO_SUCCESS_MESSAGE).text
        assert product_name == product_name_to_success_message, "Incorrect product name to success message"

    def shoul_be_correct_product_price_to_success_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_to_success_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_TO_SUCCESS_MESSAGE).text
        assert product_price == product_price_to_success_message, "Incorrect product price to success message"
        