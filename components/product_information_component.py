from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductInformation(BasePage):
    # Localizador base de la sección completa
    CONTAINER = (By.CLASS_NAME, "product-information")

    # Localizadores dentro del contenedor
    NAME = (By.XPATH, "//div[@class='product-information']/h2")
    CATEGORY = (By.XPATH, "//div[@class='product-information']/p[1]")
    PRICE = (By.XPATH, "//div[@class='product-information']/span/span")
    AVAILABILITY = (By.XPATH, "//div[@class='product-information']//p/b[normalize-space()='Availability:']/parent::p")
    CONDITION = (By.XPATH, "//div[@class='product-information']//p/b[normalize-space()='Condition:']/parent::p")
    BRAND = (By.XPATH, "//div[@class='product-information']//p/b[normalize-space()='Brand:']/parent::p")

    def __init__(self, driver):
        super().__init__(driver)
        self.container = self._find_element(self.CONTAINER)

    def get_name(self):
        return self._get_text(self.NAME)

    def get_category(self):
        # "Category: Women > Tops"
        raw_text = self._get_text(self.CATEGORY)
        return raw_text.replace("Category:", "").strip()

    def get_price(self):
        raw_text = self._get_text(self.PRICE)
        return raw_text.replace("Rs.", "").strip()

    def get_availability(self):
        # "Availability: In Stock"
        raw_text = self._get_text(self.AVAILABILITY)
        return raw_text.replace("Availability:", "").strip()

    def get_condition(self):
        raw_text = self._get_text(self.CONDITION)
        return raw_text.replace("Condition:", "").strip()

    def get_brand(self):
        raw_text = self._get_text(self.BRAND)
        return raw_text.replace("Brand:", "").strip()

    def get_all_details(self):
        return {
            "name": self.get_name(),
            "category": self.get_category(),
            "price": self.get_price(),
            "availability": self.get_availability(),
            "condition": self.get_condition(),
            "brand": self.get_brand(),
        }
