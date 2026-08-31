import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )
    parser.addoption(
        "--url",
        default="http://localhost/opencart",
        help="Base URL of the shop"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="function")
def driver(browser, request):
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        drv = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        drv = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    drv.implicitly_wait(5)
    yield drv
    drv.quit()