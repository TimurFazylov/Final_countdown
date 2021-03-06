from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_EMAIL_FIELD = (By.NAME, "login-username")
    LOGIN_PASSWORD_FIELD = (By.NAME, "login-password")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "[href^='/ru/password-reset']")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTER_EMAIL_FIELD = (By.NAME, "registration-email")
    REGISTER_PASSWORD1_FIELD = (By.NAME, "registration-password1")
    REGISTER_PASSWORD2_FIELD = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    MESSAGE_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) strong")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, ".basket_summary")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p > a")
