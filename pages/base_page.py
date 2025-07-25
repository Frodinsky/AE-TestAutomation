from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def _find_element(self, by_locator: tuple[str, str]):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def _click(self, by_locator: tuple[str, str]):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def _type(self, by_locator: tuple[str, str], text: str):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def _get_text(self, by_locator: tuple[str, str]):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text

    def _is_element_displayed(self, by_locator: tuple[str, str]):
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False

    def _scroll_into_view(self, by_locator: tuple[str, str]):
        element = self._find_element(by_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)