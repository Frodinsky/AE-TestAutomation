from helpers.products_flows import Products

def test_products(driver):

    products = Products(driver)
    products.see_product()