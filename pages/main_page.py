from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://litecart.stqa.ru/en/")
        return self

    @property
    def product_item(self):
        return self.driver.find_element_by_css_selector(".product")
