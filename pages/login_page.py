from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Word 'Login is not defined'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not visible"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not visible"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        btn_login_in = self.browser.find_element(*LoginPageLocators.BTN_REGISTER)
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_confirm_input.send_keys(password)
        time.sleep(5)
        btn_login_in.click()
        time.sleep(5)
