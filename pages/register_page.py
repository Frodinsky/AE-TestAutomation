from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class RegisterPage(BasePage):

    #NAVEGATION BAR
    SIGNUP_LOGIN_BTN = (By.XPATH, "//a[normalize-space()='Signup / Login']")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BTN = (By.XPATH, "//button[normalize-space()='Signup']")
    #REGISTER
    PASSWORD_INPUT = (By.ID, "password")
    TITLE_INPUT = (By.ID, "id_gender1")
    #VALUE
    DAY_INPUT = (By.ID, "days")
    MONTH_INPUT = (By.ID, "months")
    YEAR_INPUT = (By.ID, "years")
    NEWSLETTER_INPUT = (By.ID, "newsletter")
    SPECIAL_OFERT = (By.ID, "optin")

    #PERSONAL DATA
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    COMPANY_INPUT = (By.ID, "company")
    ADDRESS_INPUT = (By.ID, "address1")
    ADDRESS_INPUT_2 = (By.ID, "address2")
    COUNTRY_INPUT = (By.ID, "country")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_NUMBER_INPUT = (By.ID, "mobile_number")

    #created and delete
    CREATE_ACOUNT_BTN = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    CONTINUE_BTN = (By.XPATH, "//a[@class='btn btn-primary']")
    DELETE_ACCOUNT_BTN = (By.XPATH, "//a[normalize-space()='Delete Account']")


    #testing
    NEW_USER_VERIFY = (By.XPATH, "//h2[normalize-space()='New User Signup!']")
    SINGUP_VERIFY = (By.XPATH, "//b[normalize-space()='Enter Account Information']")
    ACOUNT_CREATE_VERIFY = (By.XPATH, "//b[normalize-space()='Account Created!']")
    USER_VERIFY = (By.XPATH, "//*[contains(text(),'Logged in as')]")
    DELETE_ACCOUNT_TXT = (By.XPATH, "//b[normalize-space()='Account Deleted!']")


    def __init__(self, driver):
        super().__init__(driver)

    #buttons
    def click_signup_login(self):
        self._click(self.SIGNUP_LOGIN_BTN)

    def click_signup_button(self):
        self._click(self.SIGNUP_BTN)

    def click_create_acount(self):
        self._click(self.CREATE_ACOUNT_BTN)

    def continue_button(self):
        self._click(self.CONTINUE_BTN)

    def delete_acount_button(self):
        self._click(self.DELETE_ACCOUNT_BTN)

    #data
    def enter_signup_credentials(self, name, email):
        self._type(self.NAME_INPUT, name)
        self._type(self.EMAIL_INPUT, email)

    def fill_account_information(self, title=True, password="1234", day="1", month="1", year="2000",
                                 newsletter = True, special_ofert = True):
        if title:
            self._click(self.TITLE_INPUT)
        self._type(self.PASSWORD_INPUT, password)
        self._select_dropdown(self.DAY_INPUT, day)
        self._select_dropdown(self.MONTH_INPUT, month)
        self._select_dropdown(self.YEAR_INPUT, year)
        if newsletter:
            self._click(self.NEWSLETTER_INPUT)
        if special_ofert:
            self._click(self.SPECIAL_OFERT)


    def fill_address_information(self, first_name, last_name, company, address1, address2,
                                 country, state, city, zipcode, mobile):

        self._type(self.FIRST_NAME_INPUT, first_name)
        self._type(self.LAST_NAME_INPUT, last_name)
        self._type(self.COMPANY_INPUT, company)
        self._type(self.ADDRESS_INPUT, address1)
        self._type(self.ADDRESS_INPUT_2, address2)
        self._select_dropdown(self.COUNTRY_INPUT, country)
        self._type(self.STATE_INPUT, state)
        self._type(self.CITY_INPUT, city)
        self._type(self.ZIPCODE_INPUT, zipcode)
        self._type(self.MOBILE_NUMBER_INPUT, mobile)

    def _select_dropdown(self, by_locator, value):
        select = Select(self._find_element(by_locator))
        select.select_by_visible_text(value)

    #asserts
    def get_new_user_title(self):
        return self._get_text(self.NEW_USER_VERIFY)

    def get_account_info_title(self):
        return self._get_text(self.SINGUP_VERIFY)

    def get_create_count(self):
        return self._get_text(self.ACOUNT_CREATE_VERIFY)

    def user_login(self):
        return self._get_text(self.USER_VERIFY)

    def user_delete(self):
        return self._get_text(self.DELETE_ACCOUNT_TXT)





