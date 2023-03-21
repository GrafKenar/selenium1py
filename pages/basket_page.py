from .base_page import BasePage
from .locators import BascetPageLocators

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_element_present(*BascetPageLocators.BASKET_TEXT), 'there is no text about empty basket'


