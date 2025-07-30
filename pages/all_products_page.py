from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AllProducts(BasePage):

    #ALL PRODUCTS
    ALL_PRODUCTS_TXT = (By.CSS_SELECTOR, ".title.text-center")
    FEATURE_ITEMS_TXT = (By.XPATH, "//h2[normalize-space()='Features Items']")
    FIRST_ITEM_BTN = (By.CSS_SELECTOR, "a[href='/product_details/1']")

    #BAR
    SEARCH_PRODUCT_BAR = (By.ID, "search_product")
    SEARCH_PRODUCT_BTN = (By.ID, "submit_search")
    SEARCH_PRODUCT_VERIFY = (By.XPATH, "//div[contains(@class, 'product-image-wrapper')]//p[contains(text(), 'Blue Top')]")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_all_products_text(self):
        return self._get_text(self.ALL_PRODUCTS_TXT)

    def verify_feature_items_text(self):
        return self._get_text(self.FEATURE_ITEMS_TXT)

    def click_firts_product_button(self):
        self._scroll_into_view(self.FIRST_ITEM_BTN)
        self._click(self.FIRST_ITEM_BTN)

    def fill_serch_product_bar(self, product):
        self._type(self.SEARCH_PRODUCT_BAR, product)

    def click_search_product_button(self):
        self._scroll_into_view(self.FIRST_ITEM_BTN)
        return self._click(self.SEARCH_PRODUCT_BTN)

    def get_product_search_text(self):
        self._find_element(self.FIRST_ITEM_BTN)
        self._scroll_into_view(self.FIRST_ITEM_BTN)
        return self._get_text(self.SEARCH_PRODUCT_VERIFY)