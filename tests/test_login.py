import pytest
from pages.login_page import LoginPage
from utils.read_config import get_base_url, config
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self, driver):
        logger.info("Starting test: test_valid_login")

        driver.get(get_base_url())
        login_page = LoginPage(driver)

        username = config.get("DEFAULT", "username")
        password = config.get("DEFAULT", "password")

        logger.info(f"Navigating to {get_base_url()} and logging in.")
        login_page.login_to_application(username, password)

        assert "inventory" in driver.current_url, "Login failed — inventory page not loaded."
        logger.info("Login successful. User is on inventory page.")
