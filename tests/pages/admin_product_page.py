import time
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminProductPage(BasePage):
    ADD_NEW = (By.CSS_SELECTOR, "a[href*='product/form']")
    PRODUCT_NAME = (By.ID, "input-name-1")
    META_TAG = (By.ID, "input-meta-title-1")
    DATA_TAB = (By.CSS_SELECTOR, "#form-product a[href='#tab-data']")
    MODEL = (By.ID, "input-model")
    PRICE = (By.ID, "input-price")
    QUANTITY = (By.ID, "input-quantity")
    SAVE = (By.CSS_SELECTOR, "button[form='form-product']")
    SUCCESS_ALERT = (By.CLASS_NAME, "alert-success")
    CHECKBOXES = (By.CSS_SELECTOR, "table tbody input[type='checkbox']")
    DELETE_BTN = (By.CSS_SELECTOR, "button[title='Delete']")
    CONFIRM_OK = (By.CSS_SELECTOR, ".modal-dialog .btn-danger")

    @allure.step("Click add new product")
    def click_add_new(self):
        self.logger.info("Clicking add new product")
        self.click(*self.ADD_NEW)

    @allure.step("Fill product form: {name}, {meta}, {model}, {price}, {qty}")
    def fill_product_form(self, name, meta, model, price, qty):
        self.logger.info("Filling product form: %s", name)
        self.input_text(*self.PRODUCT_NAME, name)
        self.input_text(*self.META_TAG, meta)
        self.click(*self.DATA_TAB)
        time.sleep(0.5)
        self.input_text(*self.MODEL, model)
        self.input_text(*self.PRICE, price)
        self.input_text(*self.QUANTITY, qty)

    @allure.step("Save product")
    def save(self):
        self.logger.info("Saving product")
        self.click(*self.SAVE)

    @allure.step("Check success alert")
    def is_success(self):
        self.logger.info("Checking success alert")
        return self.is_visible(*self.SUCCESS_ALERT)

    @allure.step("Delete first product")
    def delete_first_product(self):
        self.logger.info("Deleting first product")
        checkboxes = self.find_all(*self.CHECKBOXES)
        if checkboxes:
            checkboxes[0].click()
            self.click(*self.DELETE_BTN)
            time.sleep(1)
            self.click(*self.CONFIRM_OK)
            time.sleep(1)

    @allure.step("Get products count")
    def get_products_count(self):
        self.logger.info("Getting products count")
        return len(self.find_all(*self.CHECKBOXES))