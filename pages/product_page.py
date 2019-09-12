from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_size_if_available(self):
        if len(self.driver.find_elements_by_css_selector('[name="options[Size]"]')) != 0:
            Select(self.driver.find_element_by_css_selector('[name="options[Size]"]')).select_by_value('Large')

    def add_item(self):
        quantity = self.driver.find_element_by_css_selector('span.quantity')
        new_quantity = int(quantity.text) + 1
        self.driver.find_element_by_css_selector('button[name="add_cart_product"]').click()
        self.wait.until(ec.text_to_be_present_in_element((By.CLASS_NAME, "quantity"), str(new_quantity)))
