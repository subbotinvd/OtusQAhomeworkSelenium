import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    TITLE = (By.TAG_NAME, "h1")
    PRICE = (By.CSS_SELECTOR, "[class*='price']")
    QUANTITY = (By.ID, "input-quantity")
    ADD_TO_CART = (By.ID, "button-cart")
    IMAGE = (By.CLASS_NAME, "image")
    DESCRIPTION = (By.ID, "tab-description")

    @allure.step("Check product page elements")
    def check_elements(self):
        self.logger.info("Checking product page elements")
        self.is_visible(*self.TITLE)
        self.is_visible(*self.PRICE)
        self.is_visible(*self.QUANTITY)
        self.is_visible(*self.ADD_TO_CART)
        self.is_visible(*self.IMAGE)
        self.is_visible(*self.DESCRIPTION)

    @allure.step("Add product to cart")
    def add_to_cart(self):
        self.logger.info("Adding product to cart")
        self.click(*self.ADD_TO_CART)