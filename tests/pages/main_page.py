from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    LOGO = (By.ID, "logo")
    SEARCH = (By.CSS_SELECTOR, "input[name='search']")
    MENU = (By.ID, "menu")
    CART = (By.ID, "cart")
    PRODUCT_THUMB = (By.CLASS_NAME, "product-thumb")
    COMMON_HOME = (By.ID, "common-home")
    PRODUCT_LINK = (By.CSS_SELECTOR, ".product-thumb:first-child .image a")
    PRICE = (By.CSS_SELECTOR, ".product-thumb [class*='price']")
    CURRENCY_TOGGLE = (By.CSS_SELECTOR, "#form-currency .dropdown-toggle")
    CURRENCY_ITEMS = (By.CSS_SELECTOR, "#form-currency .dropdown-menu li a")

    def open(self, base_url):
        super().open(base_url)

    def check_elements(self):
        self.is_visible(*self.LOGO)
        self.is_visible(*self.SEARCH)
        self.is_visible(*self.MENU)
        self.is_visible(*self.CART)
        self.is_visible(*self.PRODUCT_THUMB)
        self.is_visible(*self.COMMON_HOME)

    def get_first_product_price(self):
        return self.is_visible(*self.PRICE).text

    def click_first_product(self):
        self.click(*self.PRODUCT_LINK)

    def switch_currency(self, index=1):
        self.click(*self.CURRENCY_TOGGLE)
        items = self.find_all(*self.CURRENCY_ITEMS)
        if len(items) > index:
            items[index].click()

    def get_currency_items_count(self):
        self.click(*self.CURRENCY_TOGGLE)
        return len(self.find_all(*self.CURRENCY_ITEMS))