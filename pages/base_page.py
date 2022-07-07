from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium.webdriver.common.by import By
from .locators import BasePageLocators
import time
import pytest


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # проверить, что какой-то элемент исчезает
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    '''Первый способ перехода между страницами: возвращать нужный Page Object.
            def go_to_login_page(self):
                link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
                link.click()
                return LoginPage(browser=self.browser, url=self.browser.current_url) '''
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    '''Второй подход: переход происходит неявно, страницу инициализируем в теле теста'''
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        time.sleep(5)

    def go_to_basket(self):
        btn_basket_link = self.browser.find_element(*BasePageLocators.BTN_BASKET)
        btn_basket_link.click()
        assert self.is_element_present(*BasePageLocators.MESS_BASKET_IS_EMPTY), "Message not present on page"

    def expect_there_are_no_items_in_the_cart(self):
        assert self.is_not_element_present(*BasePageLocators.BOOK_ON_PAGE_CART), "The book is in the cart"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented,"\
                                                                     "probably unauthorised user"
