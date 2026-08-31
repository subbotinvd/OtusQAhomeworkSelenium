import logging
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(self.__class__.__name__)

    @allure.step("Open URL {url}")
    def open(self, url):
        self.logger.info("Opening URL: %s", url)
        self.driver.get(url)

    @allure.step("Find element {by}={value}")
    def find(self, by, value):
        self.logger.info("Finding element: %s=%s", by, value)
        return self.driver.find_element(by, value)

    @allure.step("Find all elements {by}={value}")
    def find_all(self, by, value):
        self.logger.info("Finding all elements: %s=%s", by, value)
        return self.driver.find_elements(by, value)

    @allure.step("Click element {by}={value}")
    def click(self, by, value):
        self.logger.info("Clicking element: %s=%s", by, value)
        self.wait.until(EC.element_to_be_clickable((by, value))).click()

    @allure.step("Input text into {by}={value}")
    def input_text(self, by, value, text):
        self.logger.info("Inputting text into %s=%s", by, value)
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        element.clear()
        element.send_keys(text)

    @allure.step("Check visibility of {by}={value}")
    def is_visible(self, by, value):
        self.logger.info("Checking visibility: %s=%s", by, value)
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    @allure.step("Check presence of {by}={value}")
    def is_present(self, by, value):
        self.logger.info("Checking presence: %s=%s", by, value)
        return self.wait.until(EC.presence_of_element_located((by, value)))