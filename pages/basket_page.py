from .locators import BasePageLocators
from .locators import BasketPageLocators
from .base_page import BasePage
import time


class BasketPage(BasePage):

    def expect_are_no_items_in_the_cart(self):
        assert self.is_element_present(*BasePageLocators.MESS_BASKET_IS_EMPTY), \
            "Success message is presented"

    def expect_is_a_text_that_the_cart_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BOOK_IN_BASKET), "Success message is not disappeared"