from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def find_all(self, by, value):
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        self.wait.until(EC.element_to_be_clickable((by, value))).click()

    def input_text(self, by, value, text):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        element.clear()
        element.send_keys(text)

    def is_visible(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def is_present(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))