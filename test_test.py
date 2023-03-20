import pytest
from pages.product_page import ProductPage
from pages.basket_page import BascetPage
from pages.login_page import LoginPage
import time



class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = email
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email=email, password=password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        browser.implicitly_wait(5)
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.check_name_in_message()
        page.check_price_in_message()