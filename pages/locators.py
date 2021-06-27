from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    INPUT_EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_MESSAGE_PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_BUTTON_REGISTRATION = (By.CSS_SELECTOR, '[name="registration_submit"]')
    RESULT_MESSAGE_REGISTRATION = (By.CSS_SELECTOR, '.alertinner')
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')
    RESULT_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
