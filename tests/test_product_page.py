from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_product_page_elements(driver, base_url):
    driver.get(f"{base_url}/index.php?route=product/product&product_id=43")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='price']")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-quantity")))
    wait.until(EC.visibility_of_element_located((By.ID, "button-cart")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "image")))
    wait.until(EC.visibility_of_element_located((By.ID, "tab-description")))