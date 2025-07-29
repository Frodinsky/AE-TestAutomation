from helpers.products_flows import Products
import time

def test_products(driver):

    products = Products(driver)
    products.see_product()