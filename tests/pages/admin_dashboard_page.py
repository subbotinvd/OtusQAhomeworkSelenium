import time
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminDashboardPage(BasePage):
    HEADING = (By.CSS_SELECTOR, "#content h1")
    LOGOUT = (By.CSS_SELECTOR, "#nav-logout a")
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog a")
    PRODUCTS_LINK = (By.CSS_SELECTOR, "#menu-catalog ul li a[href*='product']")

    @allure.step("Check logged in state")
    def check_logged_in(self):
        self.logger.info("Checking logged in state")
        self.is_visible(*self.HEADING)
        assert "Dashboard" in self.driver.title

    @allure.step("Logout from admin panel")
    def logout(self):
        self.logger.info("Logging out")
        try:
            close = self.driver.find_element(By.CSS_SELECTOR, ".modal.show .btn-close")
            close.click()
            time.sleep(0.5)
        except Exception:
            pass
        self.click(*self.LOGOUT)

    @allure.step("Go to products page")
    def go_to_products(self):
        self.logger.info("Navigating to products page")
        self.click(*self.CATALOG_MENU)
        self.click(*self.PRODUCTS_LINK)