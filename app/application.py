from selenium import webdriver
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_items_in_cart(self):
        self.main_page.open()
        self.main_page.product_item.click()
        self.product_page.select_size_if_available()
        self.product_page.add_item()

    def del_items_from_cart(self):
        self.cart_page.open_cart()
        self.cart_page.del_items()
