from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_elements(driver, base_url):
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='search']")))
    wait.until(EC.visibility_of_element_located((By.ID, "menu")))
    wait.until(EC.visibility_of_element_located((By.ID, "cart")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-thumb")))
    wait.until(EC.visibility_of_element_located((By.ID, "common-home")))