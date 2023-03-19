from .base_page import BasePage
from .locators import LoginPageLocators
import time



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is not in the url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "there is no login form on the page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "there is no register form on the page"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIRST).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_SECOND).send_keys(password)