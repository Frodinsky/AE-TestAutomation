from helpers.user_flows import User
def test_register_new_user(driver):

    user = User(driver)
    user.create()
    user.delete()