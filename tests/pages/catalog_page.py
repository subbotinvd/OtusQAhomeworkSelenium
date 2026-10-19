from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CatalogPage(BasePage):
    PRODUCT_CATEGORY = (By.ID, "product-category")
    COLUMN_LEFT = (By.ID, "column-left")
    HEADING = (By.TAG_NAME, "h1")
    PRODUCT_THUMB = (By.CLASS_NAME, "product-thumb")
    PAGINATION = (By.CLASS_NAME, "pagination")
    CONTENT = (By.ID, "content")
    PRICE = (By.CSS_SELECTOR, ".product-thumb [class*='price']")
    CURRENCY_TOGGLE = (By.CSS_SELECTOR, "#form-currency .dropdown-toggle")
    CURRENCY_ITEMS = (By.CSS_SELECTOR, "#form-currency .dropdown-menu li a")

    def open(self, base_url):
        super().open(f"{base_url}/index.php?route=product/category&path=20")

    def check_elements(self):
        self.is_visible(*self.PRODUCT_CATEGORY)
        self.is_visible(*self.COLUMN_LEFT)
        self.is_visible(*self.HEADING)
        self.is_visible(*self.PRODUCT_THUMB)
        self.is_visible(*self.PAGINATION)
        self.is_visible(*self.CONTENT)

    def get_first_product_price(self):
        return self.is_visible(*self.PRICE).text

    def switch_currency(self, index=1):
        self.click(*self.CURRENCY_TOGGLE)
        items = self.find_all(*self.CURRENCY_ITEMS)
        if len(items) > index:
            items[index].click()

    def get_currency_items_count(self):
        self.click(*self.CURRENCY_TOGGLE)
        return len(self.find_all(*self.CURRENCY_ITEMS))