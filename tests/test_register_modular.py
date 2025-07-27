from helpers.user_flows import User
import time

def test_register_new_user(driver):

    user = User(driver)
    user.create()
    #user.delete()

    time.sleep(5)