from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.admin_login_page import AdminLoginPage
from pages.registration_page import RegistrationPage


def test_main_page_elements(driver, base_url):
    page = MainPage(driver)
    page.open(base_url)
    page.check_elements()


def test_catalog_page_elements(driver, base_url):
    page = CatalogPage(driver)
    page.open(base_url)
    page.check_elements()


def test_product_page_elements(driver, base_url):
    page = ProductPage(driver)
    page.open(f"{base_url}/index.php?route=product/product&product_id=43")
    page.check_elements()


def test_admin_login_page_elements(driver, base_url):
    page = AdminLoginPage(driver)
    page.open(base_url)
    page.check_elements()


def test_registration_page_elements(driver, base_url):
    page = RegistrationPage(driver)
    page.open(base_url)
    page.check_elements()