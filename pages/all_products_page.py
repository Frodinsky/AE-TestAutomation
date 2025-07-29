from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AllProducts(BasePage):

    #
    ALL_PRODUCTS_TXT = (By.CSS_SELECTOR, ".title.text-center")
    FEATURE_ITEMS_TXT = (By.XPATH, "//h2[normalize-space()='Features Items']")
    FIRST_ITEM_BTN = (By.CSS_SELECTOR, "a[href='/product_details/1']")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_all_products_text(self):
        return self._get_text(self.ALL_PRODUCTS_TXT)

    def verify_feature_items_text(self):
        return self._get_text(self.FEATURE_ITEMS_TXT)

    def click_firts_product_button(self):
        self._scroll_into_view(self.FIRST_ITEM_BTN)
        self._click(self.FIRST_ITEM_BTN)
