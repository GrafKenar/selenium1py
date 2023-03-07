from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()

    def solve_the_puzzle(self):
        BasePage.solve_quiz_and_get_code(self)

    def check_name_in_message(self):
        expected_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE).text
        actual_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert expected_name == actual_name, "names are different on page and in the message"

    def check_price_in_message(self):
        expected_price = self.browser.find_element(*ProductPageLocators.PRICE_ON_PAGE).text
        actual_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        assert expected_price in actual_price, "names are different on page and in the message"
