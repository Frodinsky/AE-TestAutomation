import random
import string
from pages.register_page import RegisterPage
from components.header_component import HeaderComponent
from pages.login_page import LoginPage


class User:

    def __init__(self, driver, name="Juan Tester", password="test1234"):
        self.driver = driver
        self.name = name
        self.password = password
        self.email = self._generate_random_email()
        self.register_page = RegisterPage(driver)
        self.header = HeaderComponent(driver)
        self.login_page = LoginPage(driver)

    @staticmethod
    def _generate_random_email():
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"tester_{random_string}@example.com"

    def create(self):
        self.header.click_signup_login_button()
        print(f"Correo random generado: {self.email}")

        self.register_page.enter_signup_credentials(self.name, self.email)
        self.register_page.click_signup_button()
        assert "ENTER ACCOUNT INFORMATION" in self.register_page.get_account_info_title()

        self.register_page.fill_account_information(
            title=True,
            password=self.password,
            day="10",
            month="June",
            year="1990",
            newsletter=True,
            special_offer=True
        )

        self.register_page.fill_address_information(
            first_name="Juan",
            last_name="Pérez",
            company="Empresa S.A.",
            address1="Calle Falsa 123",
            address2="Depto 4",
            country="Canada",
            state="Ontario",
            city="Toronto",
            zipcode="A1A1A1",
            mobile="+1234567890"
        )

        self.register_page.click_create_account_button()
        assert "ACCOUNT CREATED!" in self.register_page.get_account_created_message()
        self.register_page.click_continue_button()
        assert self.name in self.register_page.get_logged_user_text()

    def delete(self):
        self.header.click_delete_account_button()
        assert "ACCOUNT DELETED!" in self.register_page.get_account_deleted_text()
        self.register_page.click_continue_button()

    def get_credentials(self):

        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

    def login_with_valid_credentials(self):
        self.header.click_signup_login_button()
        assert self.driver.current_url == "https://automationexercise.com/login"
        self.login_page.enter_email_login_credentials(self.email, self.password)
        self.login_page.click_login_button()
        assert self.name in self.login_page.verify_user_text()

    def login_with_invalid_credentials(self):
        self.header.click_signup_login_button()
        assert self.driver.current_url == "https://automationexercise.com/login"
        self.login_page.enter_email_login_credentials("fake_email@example.com", "wrongpassword")
        self.login_page.click_login_button()
        assert "Your email or password is incorrect!" in self.login_page.verify_false_user_text()

    def logout(self):
        self.header.click_logout_button()
        assert self.driver.current_url == "https://automationexercise.com/login"



