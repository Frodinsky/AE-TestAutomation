from selenium import webdriver
import pytest

BASE_URL = "https://automationexercise.com/"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

    """
    Datos para trabajar
Address 1: 742 Evergreen Terrace

Address 2: Apt 12B

Ciudad: Springfield

Estado: IL (Illinois)

ZIP Code: 62704

Teléfono: (217) 555-0198
"""