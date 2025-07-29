from helpers.user_flows import User

def test_login_user_false(driver):
    user = User(driver)
    user.login_with_invalid_credentials()
