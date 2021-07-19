from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .base_page import BasePage
import time
import re


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_adress_field = self.browser.find_element(*LoginPageLocators.EMAIL_ADRESS)
        email_adress_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_password_field.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_url(self):
        assert re.search(LoginPageLocators.LINK_TEXT, self.browser.current_url), "Incorrect link"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
        