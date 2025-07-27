from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    #LOGIN
    EMAIL_LOGIN_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_LOGIN_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    #BUTTON
    LOGIN_BTN = (By.XPATH, "//button[normalize-space()='Login']")
    #TEST
    USER_VERIFY_TXT = (By.CSS_SELECTOR, "li:nth-child(10) a:nth-child(1)")
    USER_FALSE_DATA_TXT = (By.XPATH, "//p[normalize-space()='Your email or password is incorrect!']")


    def __init__(self, driver):
        super().__init__(driver)

    def enter_email_login_credentials(self, email, password):
        self._type(self.EMAIL_LOGIN_INPUT, email)
        self._type(self.PASSWORD_LOGIN_INPUT, password)

    def click_login_button(self):
        self._click(self.LOGIN_BTN)

    def verify_user_text(self):
        return self._get_text(self.USER_VERIFY_TXT)

    def verify_false_user_text(self):
        return self._get_text(self.USER_FALSE_DATA_TXT)
