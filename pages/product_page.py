from .locators import ProductPageLocators
from .base_page import BasePage
import time


class ProductPage(BasePage):

    def click_add_to_basket(self):
        btn_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        btn_basket.click()
        time.sleep(2)

    def message_item_added_to_cart(self):
        mess = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_CART)
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        print(name_book.text)
        print(mess.text)
        assert name_book.text == mess.text, "Book name does not match "

    def message_price_added_to_cart(self):
        price_in_cart = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_IN_CART)
        price_in_main_page = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        print(price_in_main_page.text)
        print(price_in_cart.text)
        assert price_in_cart.text == price_in_main_page.text, 'Book price does not match'

    def should_not_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_CART), \
            "Success message is presented"

    def show_that_the_message_does_not_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_CART), "Success message is not disappeared"