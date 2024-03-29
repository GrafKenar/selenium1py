from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD_FIRST = (By.ID, 'id_registration-password1')
    PASSWORD_SECOND = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages>.alert:nth-child(1)>.alertinner>strong')
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, '.product_main>h1')
    PRICE_ON_PAGE = (By.CSS_SELECTOR, '.product_main>.price_color')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages>.alert:nth-child(3)>.alertinner>p:nth-child(1)')
    BASCET_SUCCESS = (By.CLASS_NAME, 'alertinner')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini >.btn-group>.btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BascetPageLocators:
    BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
