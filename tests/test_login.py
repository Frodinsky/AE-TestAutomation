from helpers.user_flows import User
import time

def test_login_user(driver):

    user = User(driver)
    user.create()
    user.logout()
    user.login()
    user.delete()
    time.sleep(1)