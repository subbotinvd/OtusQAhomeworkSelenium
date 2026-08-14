from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog_page_elements(driver, base_url):
    driver.get(f"{base_url}/index.php?route=product/category&path=20")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "product-category")))
    wait.until(EC.visibility_of_element_located((By.ID, "column-left")))
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-thumb")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pagination")))
    wait.until(EC.visibility_of_element_located((By.ID, "content")))