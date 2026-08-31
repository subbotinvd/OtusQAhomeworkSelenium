import time
import pytest
import allure
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage


@allure.feature("Currency")
class TestCurrency:

    @allure.story("Main Page")
    @allure.title("Currency switch on main page")
    def test_currency_switch_on_main(self, driver, base_url):
        page = MainPage(driver)
        page.open(base_url)

        price_before = page.get_first_product_price()

        if page.get_currency_items_count() <= 1:
            pytest.skip("Only one currency available")

        page.switch_currency(index=1)
        time.sleep(2)

        price_after = page.get_first_product_price()
        assert price_before != price_after

    @allure.story("Catalog Page")
    @allure.title("Currency switch in catalog")
    def test_currency_switch_in_catalog(self, driver, base_url):
        page = CatalogPage(driver)
        page.open(base_url)

        price_before = page.get_first_product_price()

        if page.get_currency_items_count() <= 1:
            pytest.skip("Only one currency available")

        page.switch_currency(index=1)
        time.sleep(2)

        price_after = page.get_first_product_price()
        assert price_before != price_after