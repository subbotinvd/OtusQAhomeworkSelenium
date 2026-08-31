from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    FORM = (By.ID, "form-register")
    FIRSTNAME = (By.ID, "input-firstname")
    LASTNAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    SUBMIT = (By.CSS_SELECTOR, "#form-register button[type='submit']")
    SUCCESS = (By.ID, "common-success")

    def open(self, base_url):
        super().open(f"{base_url}/index.php?route=account/register")

    def check_elements(self):
        self.is_visible(*self.FORM)
        self.is_visible(*self.FIRSTNAME)
        self.is_visible(*self.LASTNAME)
        self.is_visible(*self.EMAIL)
        self.is_visible(*self.PASSWORD)
        self.is_visible(*self.SUBMIT)

    def register(self, firstname, lastname, email, password):
        self.input_text(*self.FIRSTNAME, firstname)
        self.input_text(*self.LASTNAME, lastname)
        self.input_text(*self.EMAIL, email)
        self.input_text(*self.PASSWORD, password)
        self.click(*self.SUBMIT)

    def is_success(self):
        return self.is_visible(*self.SUCCESS)