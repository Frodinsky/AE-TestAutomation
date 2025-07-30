from components.header_component import HeaderComponent
from pages.all_products_page import AllProducts
from components.product_information_component import ProductInformation


class Products:

    def __init__(self, driver, search_product="Blue Top"):
        self.driver = driver
        self.search_product = search_product
        self.header = HeaderComponent(driver)
        self.all_products = AllProducts(driver)


    def see_product(self):

        assert "FEATURES ITEMS" in self.all_products.verify_feature_items_text()
        self.header.click_products_button()
        assert "ALL PRODUCTS" in self.all_products.verify_all_products_text()
        self.all_products.click_firts_product_button()

        #Product 1
        product_information = ProductInformation(self.driver)
        details = product_information.get_all_details()

        expected = {
            "name": "Blue Top",
            "category": "Women > Tops",
            "price": "500",
            "availability": "In Stock",
            "condition": "New",
            "brand": "Polo"
        }

        for key, expected_value in expected.items():
            assert details[key] == expected_value, f"Expected {key} to be '{expected_value}' but got '{details[key]}'"

    def search_product_bar(self):
        assert "FEATURES ITEMS" in self.all_products.verify_feature_items_text()
        self.header.click_products_button()
        self.all_products.fill_serch_product_bar(self.search_product)
        self.all_products.click_search_product_button()
        assert "Blue Top" in self.all_products.get_product_search_text()


