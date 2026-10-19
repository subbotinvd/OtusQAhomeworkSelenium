import allure
from pages.admin_login_page import AdminLoginPage
from pages.admin_dashboard_page import AdminDashboardPage
from pages.admin_product_page import AdminProductPage


@allure.feature("Admin Products")
class TestAdminProduct:

    @allure.story("CRUD")
    @allure.title("Add new product")
    def test_add_new_product(self, driver, base_url):
        login = AdminLoginPage(driver)
        login.open(base_url)
        login.login("admin", "admin123")

        dashboard = AdminDashboardPage(driver)
        dashboard.go_to_products()

        products = AdminProductPage(driver)
        products.click_add_new()
        products.fill_product_form(
            name="Test Product",
            meta="Test Meta",
            model="TEST-001",
            price="99.99",
            qty="10",
        )
        products.save()
        assert products.is_success()

    @allure.story("CRUD")
    @allure.title("Delete product")
    def test_delete_product(self, driver, base_url):
        login = AdminLoginPage(driver)
        login.open(base_url)
        login.login("admin", "admin123")

        dashboard = AdminDashboardPage(driver)
        dashboard.go_to_products()

        products = AdminProductPage(driver)
        before = products.get_products_count()
        products.delete_first_product()
        assert products.is_success()
        after = products.get_products_count()
        assert after < before