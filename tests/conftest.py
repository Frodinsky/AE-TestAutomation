from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
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