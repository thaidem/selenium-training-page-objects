from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_cart(self):
        self.driver.find_element_by_css_selector('#cart .link').click()
        self.driver.find_element_by_css_selector('.act').click()

    def del_items(self):
        while len(self.driver.find_elements_by_css_selector('[value="Remove"]')) != 0:
            self.driver.find_element_by_css_selector('[value="Remove"]').click()
            item = self.driver.find_element_by_css_selector('.dataTable td.item')
            self.wait.until(ec.staleness_of(item))
