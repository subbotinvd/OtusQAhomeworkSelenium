import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, "#checkout-cart .table tbody tr")

    @allure.step("Open cart page")
    def open(self, base_url):
        self.logger.info("Opening cart page")
        super().open(f"{base_url}/index.php?route=checkout/cart")

    @allure.step("Get cart items count")
    def get_items_count(self):
        self.logger.info("Getting cart items count")
        return len(self.find_all(*self.CART_ITEMS))