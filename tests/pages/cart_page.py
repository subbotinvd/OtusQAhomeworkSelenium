from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, "#checkout-cart .table tbody tr")

    def open(self, base_url):
        super().open(f"{base_url}/index.php?route=checkout/cart")

    def get_items_count(self):
        return len(self.find_all(*self.CART_ITEMS))