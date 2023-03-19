from .pages.product_page import *
from .pages.basket_page import *
from .pages.login_page import *
import pytest
import time

email = str(time.time()) + "@fakemail.org"
password = '1234'

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_can_add_product_to_basket(browser, link):
    browser.implicitly_wait(5)
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    #    page.solve_the_puzzle()
    page.check_name_in_message()
    page.check_price_in_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
#    page.solve_the_puzzle()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
#    page.solve_the_puzzle()
    page.success_message_should_disappear()

@pytest.mark.smoke
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.smoke
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()



def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_bascet()
    page = BascetPage(browser, link)
    page.basket_should_be_empty()


class TestUserAddToBasketFromProductPage(LoginPage):

    @pytest.fixture(scope='class')
    def setup(self):
        self.go_to_login_page()
        self.register_new_user(email, password)
        self.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser, link):
        browser.implicitly_wait(5)
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        #    page.solve_the_puzzle()
        page.check_name_in_message()
        page.check_price_in_message()