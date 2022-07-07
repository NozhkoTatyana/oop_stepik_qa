from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


@pytest.mark.skip
@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_should_see_login_link(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, url)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    '''Плюсы:

    * меньше связность кода;
    * меньше импортов, нет перекрестных импортов;
    * больше гибкость;
    * в тесте понятнее что происходит, т.к. явно инициализируем страницу.

    Минусы:

    * появляется лишний шаг в тест-кейсе;
    * каждый раз при написании теста нужно думать про корректные переходы;
    * дублируется код.'''


'''Плюсы такого подхода: 

* тест выглядит аккуратнее — не нужно инициализировать страницу в теле теста;
* явно возвращаем страницу — тип страницы ассоциирован с методом;
* не нужно каждый раз думать в разных тестах про инициализацию страницы — уменьшаем дублирование кода;

Минусы: 

* если у нас копится большое количество страниц и переходов — образуется много перекрестных импортов;
* большая связность кода — при изменении логики придется менять возвращаемое значение;
* сложнее понимать код, так как страница инициализируется неявно;
* образуются циклические зависимости, что часто приводит к ошибкам.

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page() '''


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.expect_are_no_items_in_the_cart()
    page.expect_is_a_text_that_the_cart_is_empty()


