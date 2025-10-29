import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.read_config import get_username, get_password, get_base_url
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.usefixtures("setup")
class TestCart:

    def test_verify_product_in_cart(self, driver):
        """Verify that a product added from the product page appears in the cart."""
        logger.info("===== Starting test: test_verify_product_in_cart =====")

        driver.get(get_base_url())
        login_page = LoginPage(driver)
        login_page.login_to_application(get_username(), get_password())
        logger.info("Login successful.")

        products_page = ProductsPage(driver)
        product_id = "sauce-labs-backpack"
        product_name = "Sauce Labs Backpack"

        products_page.add_product_to_cart(product_id)
        logger.info(f"Product added to cart: {product_name}")
        products_page.go_to_cart()
        logger.info("Navigated to cart page.")

        cart_page = CartPage(driver)
        assert cart_page.verify_product_in_cart(product_name), f"Product '{product_name}' not found in cart."
        logger.info(f"Verified product '{product_name}' is present in the cart.")

        logger.info("===== Test completed: test_verify_product_in_cart =====")

    def test_proceed_to_checkout(self, driver):
        """Verify user can navigate to checkout page."""
        logger.info("===== Starting test: test_proceed_to_checkout =====")

        driver.get(get_base_url())
        login_page = LoginPage(driver)
        login_page.login_to_application(get_username(), get_password())
        logger.info("Login successful.")

        products_page = ProductsPage(driver)
        product_id = "sauce-labs-backpack"

        products_page.add_product_to_cart(product_id)
        logger.info(f"Product '{product_id}' added to cart.")
        products_page.go_to_cart()
        logger.info("Navigated to cart page.")

        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()
        logger.info("Clicked on checkout button, waiting for navigation.")

        assert "checkout-step-one" in driver.current_url, \
            f"Failed to navigate to checkout page. Current URL: {driver.current_url}"
        logger.info("User successfully navigated to checkout page.")

        logger.info("===== Test completed: test_proceed_to_checkout =====")
