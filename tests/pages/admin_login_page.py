from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminLoginPage(BasePage):
    FORM = (By.ID, "form-login")
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    SUBMIT = (By.CSS_SELECTOR, "#form-login button[type='submit']")
    CARD_HEADER = (By.CLASS_NAME, "card-header")
    NAV_BRAND = (By.CLASS_NAME, "navbar-brand")

    def open(self, base_url):
        super().open(f"{base_url}/admin/")

    def check_elements(self):
        self.is_visible(*self.FORM)
        self.is_visible(*self.USERNAME)
        self.is_visible(*self.PASSWORD)
        self.is_visible(*self.SUBMIT)
        self.is_visible(*self.CARD_HEADER)
        self.is_visible(*self.NAV_BRAND)

    def login(self, username="admin", password="admin123"):
        self.input_text(*self.USERNAME, username)
        self.input_text(*self.PASSWORD, password)
        self.click(*self.SUBMIT)