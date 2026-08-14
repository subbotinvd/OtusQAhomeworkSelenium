from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_login_page_elements(driver, base_url):
    driver.get(f"{base_url}/admin/")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "form-login")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-username")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#form-login button[type='submit']")
    ))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "card-header")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "navbar-brand")))