import time
import allure
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.admin_login_page import AdminLoginPage
from pages.admin_dashboard_page import AdminDashboardPage


@allure.feature("End-to-end Scenarios")
class TestScenarios:

    @allure.story("Admin Auth")
    @allure.title("Admin login and logout")
    def test_admin_login_logout(self, driver, base_url):
        login_page = AdminLoginPage(driver)
        login_page.open(base_url)
        login_page.login("admin", "admin123")

        dashboard = AdminDashboardPage(driver)
        dashboard.check_logged_in()
        dashboard.logout()

        login_page.is_visible(*login_page.FORM)

    @allure.story("Cart")
    @allure.title("Add product to cart from main page")
    def test_add_to_cart_from_main(self, driver, base_url):
        main = MainPage(driver)
        main.open(base_url)
        main.click_first_product()

        product = ProductPage(driver)
        product.add_to_cart()
        time.sleep(2)

        cart = CartPage(driver)
        cart.open(base_url)
        assert cart.get_items_count() >= 1