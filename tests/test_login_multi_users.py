import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import get_base_url, get_usernames, get_password
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.usefixtures("setup")
class TestLoginMultiUsers:

    @pytest.mark.parametrize("username", get_usernames())
    def test_login_multiple_users(self, username):
        """Data-driven test for multiple user logins, with dynamic data and logout."""
        self.driver.get(get_base_url())
        login_page = LoginPage(self.driver)

        password = get_password()
        logger.info(f" Starting test for user: {username}")

        login_page.login_to_application(username, password)

        if login_page.is_login_successful():
            logger.info(f" Login successful for user: {username}")

            # Logout to reset session for next iteration
            products_page = ProductsPage(self.driver)
            products_page.logout_from_application()
            logger.info(f" Logout successful for user: {username}")

        else:
            error_message = login_page.get_error_message()
            logger.warning(f" Login failed for {username} | Error: {error_message}")
