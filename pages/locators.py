from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.ID, 'id_registration-email')
    PASSWORD = (By.ID, 'id_registration-password1')
    CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    BTN_REGISTER = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET = (By.TAG_NAME, '.btn-add-to-basket')
    MESSAGE_ADD_TO_CART = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    MESSAGE_PRICE_IN_CART = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    NAME_BOOK = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRICE_BOOK = (By.TAG_NAME, 'p.price_color')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BTN_BASKET = (By.CSS_SELECTOR, '.btn-group')
    MESS_BASKET_IS_EMPTY = (By.XPATH, '//*[@id="content_inner"]/p')
    BOOK_ON_PAGE_CART = (By.CLASS_NAME, 'basket-items')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BOOK_IN_BASKET = (By.XPATH, "//*[@id='basket_formset']/div/div/div[1]/a/img")
