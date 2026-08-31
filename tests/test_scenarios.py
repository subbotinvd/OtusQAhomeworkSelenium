import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_login_logout(driver, base_url):
    driver.get(f"{base_url}/admin/")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "input-username"))).send_keys("admin")
    driver.find_element(By.ID, "input-password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "#form-login button[type='submit']").click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content h1")))
    assert "Dashboard" in driver.title

    try:
        close_btn = driver.find_element(By.CSS_SELECTOR, ".modal.show .btn-close")
        close_btn.click()
        time.sleep(0.5)
    except:
        pass

    driver.find_element(By.CSS_SELECTOR, "#nav-logout a").click()
    wait.until(EC.visibility_of_element_located((By.ID, "form-login")))


def test_add_to_cart_from_main(driver, base_url):
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)

    product = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".product-thumb:first-child .image a")
    ))
    product.click()

    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    wait.until(EC.element_to_be_clickable((By.ID, "button-cart"))).click()
    time.sleep(2)

    driver.get(f"{base_url}/index.php?route=checkout/cart")
    wait.until(EC.visibility_of_element_located((By.ID, "checkout-cart")))
    items = driver.find_elements(By.CSS_SELECTOR, "#checkout-cart .table tbody tr")
    assert len(items) >= 1


def test_currency_switch_on_main(driver, base_url):
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)

    price_before = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".product-thumb [class*='price']")
    )).text

    currency_btns = driver.find_elements(By.CSS_SELECTOR, "#form-currency .dropdown-toggle")
    if not currency_btns:
        currency_btns = driver.find_elements(By.CSS_SELECTOR, "[data-bs-toggle='dropdown']")
    if not currency_btns:
        pytest.skip("Currency switcher not found")

    currency_btns[0].click()
    time.sleep(1)

    currencies = driver.find_elements(By.CSS_SELECTOR, "#form-currency .dropdown-menu li a")
    if not currencies:
        currencies = driver.find_elements(By.CSS_SELECTOR, ".dropdown-menu.show li a")
    if len(currencies) <= 1:
        pytest.skip("Only one currency available")

    currencies[1].click()
    time.sleep(2)

    price_after = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".product-thumb [class*='price']")
    )).text
    assert price_before != price_after


def test_currency_switch_in_catalog(driver, base_url):
    driver.get(f"{base_url}/index.php?route=product/category&path=20")
    wait = WebDriverWait(driver, 10)

    price_before = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".product-thumb [class*='price']")
    )).text

    currency_btns = driver.find_elements(By.CSS_SELECTOR, "#form-currency .dropdown-toggle")
    if not currency_btns:
        currency_btns = driver.find_elements(By.CSS_SELECTOR, "[data-bs-toggle='dropdown']")
    if not currency_btns:
        pytest.skip("Currency switcher not found")

    currency_btns[0].click()
    time.sleep(1)

    currencies = driver.find_elements(By.CSS_SELECTOR, "#form-currency .dropdown-menu li a")
    if not currencies:
        currencies = driver.find_elements(By.CSS_SELECTOR, ".dropdown-menu.show li a")
    if len(currencies) <= 1:
        pytest.skip("Only one currency available")

    currencies[1].click()
    time.sleep(2)

    price_after = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".product-thumb [class*='price']")
    )).text
    assert price_before != price_after