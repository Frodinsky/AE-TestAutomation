from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HeaderComponent(BasePage):

    HOME_BUTTON = (By.XPATH, "//a[normalize-space()='Home']")
    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")
    CART_BUTTON = (By.XPATH, "//a[normalize-space()='Cart']")
    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//a[normalize-space()='Signup / Login']")
    TEST_CASES_BUTTON = (By.XPATH, "//a[normalize-space()='Test Cases']")
    API_TESTING_BUTTON = (By.XPATH, "//a[normalize-space()='API Testing']")
    VIDEO_TUTORIALS_BUTTON = (By.XPATH, "//a[normalize-space()='Video Tutorials']")
    CONTACT_US_BUTTON = (By.XPATH, "//a[normalize-space()='Contact us']")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//a[normalize-space()='Delete Account']")

    def click_home_button(self):
        self._click(self.HOME_BUTTON)

    def click_products_button(self):
        self._click(self.PRODUCTS_BUTTON)

    def click_cart_button(self):
        self._click(self.CART_BUTTON)

    def click_signup_login_button(self):
        self._click(self.SIGNUP_LOGIN_BUTTON)

    def click_test_cases_button(self):
        self._click(self.TEST_CASES_BUTTON)

    def click_api_testing_button(self):
        self._click(self.API_TESTING_BUTTON)

    def click_video_tutorials_button(self):
        self._click(self.VIDEO_TUTORIALS_BUTTON)

    def click_contact_us_button(self):
        self._click(self.CONTACT_US_BUTTON)

    def click_logout_button(self):
        self._click(self.LOGOUT_BUTTON)

    def click_delete_account_button(self):
        self._click(self.DELETE_ACCOUNT_BUTTON)


