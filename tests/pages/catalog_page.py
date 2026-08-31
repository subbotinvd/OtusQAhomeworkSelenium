import allure
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

    @allure.step("Open catalog page")
    def open(self, base_url):
        self.logger.info("Opening catalog page")
        super().open(f"{base_url}/index.php?route=product/category&path=20")

    @allure.step("Check catalog page elements")
    def check_elements(self):
        self.logger.info("Checking catalog page elements")
        self.is_visible(*self.PRODUCT_CATEGORY)
        self.is_visible(*self.COLUMN_LEFT)
        self.is_visible(*self.HEADING)
        self.is_visible(*self.PRODUCT_THUMB)
        self.is_visible(*self.PAGINATION)
        self.is_visible(*self.CONTENT)

    @allure.step("Get first product price")
    def get_first_product_price(self):
        self.logger.info("Getting first product price from catalog")
        return self.is_visible(*self.PRICE).text

    @allure.step("Switch currency to index {index}")
    def switch_currency(self, index=1):
        self.logger.info("Switching currency to index %s", index)
        self.click(*self.CURRENCY_TOGGLE)
        items = self.find_all(*self.CURRENCY_ITEMS)
        if len(items) > index:
            items[index].click()

    @allure.step("Get currency items count")
    def get_currency_items_count(self):
        self.logger.info("Getting currency items count")
        self.click(*self.CURRENCY_TOGGLE)
        return len(self.find_all(*self.CURRENCY_ITEMS))