import time
from pages.registration_page import RegistrationPage


def test_register_new_user(driver, base_url):
    page = RegistrationPage(driver)
    page.open(base_url)
    page.register(
        firstname="Test",
        lastname="User",
        email=f"testuser{int(time.time())}@example.com",
        password="testpass123"
    )
    assert page.is_success()