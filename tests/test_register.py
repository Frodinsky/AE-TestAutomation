from pages.register_page import RegisterPage

def test_register_new_user(driver):
    driver.get("https://automationexercise.com/")
    page = RegisterPage(driver)

    page.click_signup_login_button()
    assert "New User Signup!" in page.get_new_user_title()

    page.enter_signup_credentials("Juan Tester", "juan1@example.com")
    page.click_signup_button()
    assert "ENTER ACCOUNT INFORMATION" in page.get_account_info_title()

    page.fill_account_information(
        title=True,
        password="test1234",
        day="10",
        month="June",
        year="1990",
        newsletter=True,
        special_offer=True
    )

    page.fill_address_information(
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

    page.click_create_account_button()
    assert "ACCOUNT CREATED!" in page.get_account_created_message()

    page.click_continue_button()
    assert "Juan Tester" in page.get_logged_user_text()

    page.click_delete_account_button()
    assert "ACCOUNT DELETED!" in page.get_account_deleted_text()

    page.click_continue_button()

