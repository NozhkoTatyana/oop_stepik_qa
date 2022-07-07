from .pages.login_page import LoginPage
import pytest


@pytest.mark.skip
def test_guest_should_see_login_page_url(browser):
    url = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_url()


@pytest.mark.skip
def test_guest_should_see_login_page_form(browser):
    url = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_form()


@pytest.mark.skip
def test_guest_should_see_register_page_form(browser):
    url = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
    page = LoginPage(browser, url)
    page.open()
    page.should_be_register_form()


def test_user_register_should_see(browser):
    url = "http://selenium1py.pythonanywhere.com/uk/accounts/login/"
    page = LoginPage(browser, url)
    page.open()
    page.register_new_user('dvfdvfb@gmail.com', 'dvddvd')
