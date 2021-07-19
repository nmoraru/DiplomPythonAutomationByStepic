from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
from .base_page import BasePage
import re


class BasketPage(BasePage):
    def should_be_correct_text_to_empty_basket(self):
        text_from_empty_basket = (self.browser.find_element(*BasketPageLocators.TEXT_FROM_EMPTY_BASKET)).text
        assert re.search("Your basket is empty.", text_from_empty_basket), "Incorrect text information message for empty basket"

    def should_not_be_products_to_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), \
        "Products is presented to basket, but should not be"
