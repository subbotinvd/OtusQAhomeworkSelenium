import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminDashboardPage(BasePage):
    HEADING = (By.CSS_SELECTOR, "#content h1")
    LOGOUT = (By.CSS_SELECTOR, "#nav-logout a")
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog a")
    PRODUCTS_LINK = (By.CSS_SELECTOR, "#menu-catalog ul li a[href*='product']")

    def check_logged_in(self):
        self.is_visible(*self.HEADING)
        assert "Dashboard" in self.driver.title

    def logout(self):
        try:
            close = self.driver.find_element(By.CSS_SELECTOR, ".modal.show .btn-close")
            close.click()
            time.sleep(0.5)
        except:
            pass
        self.click(*self.LOGOUT)

    def go_to_products(self):
        self.click(*self.CATALOG_MENU)
        self.click(*self.PRODUCTS_LINK)