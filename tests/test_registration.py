import time
import allure
from pages.registration_page import RegistrationPage


@allure.feature("User Registration")
class TestRegistration:

    @allure.story("New User")
    @allure.title("Register new user")
    def test_register_new_user(self, driver, base_url):
        page = RegistrationPage(driver)
        page.open(base_url)
        page.register(
            firstname="Test",
            lastname="User",
            email=f"testuser{int(time.time())}@example.com",
            password="testpass123",
        )
        assert page.is_success()