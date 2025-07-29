from helpers.user_flows import User

def test_login_user(driver):

    user = User(driver)
    user.create()
    user.logout()
    user.login_with_valid_credentials()
    user.delete()