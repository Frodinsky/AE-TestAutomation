from helpers.user_flows import User
import time

def test_login_user_false(driver):
    user = User(driver)
    user.login()

    time.sleep(2)