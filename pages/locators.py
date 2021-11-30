from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL_FIELD = (By.NAME, "login-username")
    LOGIN_PASSWORD_FIELD = (By.NAME, "login-password")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "[href^='/ru/password-reset']")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTER_EMAIL_FIELD = (By.NAME, "registration-email")
    REGISTER_PASSWORD1_FIELD = (By.NAME, "registration-password1")
    REGISTER_PASSWORD2_FIELD = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
