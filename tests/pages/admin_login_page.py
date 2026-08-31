import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminLoginPage(BasePage):
    FORM = (By.ID, "form-login")
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    SUBMIT = (By.CSS_SELECTOR, "#form-login button[type='submit']")
    CARD_HEADER = (By.CLASS_NAME, "card-header")
    NAV_BRAND = (By.CLASS_NAME, "navbar-brand")

    @allure.step("Open admin login page")
    def open(self, base_url):
        self.logger.info("Opening admin login page")
        super().open(f"{base_url}/admin/")

    @allure.step("Check admin login page elements")
    def check_elements(self):
        self.logger.info("Checking admin login page elements")
        self.is_visible(*self.FORM)
        self.is_visible(*self.USERNAME)
        self.is_visible(*self.PASSWORD)
        self.is_visible(*self.SUBMIT)
        self.is_visible(*self.CARD_HEADER)
        self.is_visible(*self.NAV_BRAND)

    @allure.step("Login as {username}")
    def login(self, username="admin", password="admin123"):
        self.logger.info("Logging in as %s", username)
        self.input_text(*self.USERNAME, username)
        self.input_text(*self.PASSWORD, password)
        self.click(*self.SUBMIT)