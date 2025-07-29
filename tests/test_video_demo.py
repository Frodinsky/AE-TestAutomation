from helpers.user_flows import User
from helpers.products_flows import Products

def test_demo_video(driver):

    video_user = User(driver)
    video_user.create()
    video_user.logout()
    video_user.login_with_valid_credentials()
    video_products = Products(driver)
    video_products.see_product()
    video_user.delete()