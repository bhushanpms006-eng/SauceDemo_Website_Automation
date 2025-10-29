import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from utils.read_config import get_username, get_password
from utils.test_data import get_checkout_data
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.usefixtures("setup")
class TestConfirmation:
    def test_order_confirmation_message(self):
        """Verify user can complete checkout and see confirmation message."""

        logger.info("=== Test Start: Order Confirmation ===")

        login_page = LoginPage(self.driver)
        logger.info("Logging in with valid credentials")
        login_page.login_to_application(get_username(), get_password())

        products_page = ProductsPage(self.driver)
        logger.info("Adding product to cart")
        products_page.add_product_to_cart("sauce-labs-backpack")
        products_page.go_to_cart()

        cart_page = CartPage(self.driver)
        logger.info("Verifying product in cart")
        assert cart_page.verify_product_in_cart("Sauce Labs Backpack")

        cart_page.proceed_to_checkout()
        checkout_page = CheckoutPage(self.driver)
        data = get_checkout_data()
        checkout_page.fill_information(data["first_name"], data["last_name"], data["postal_code"])
        checkout_page.finish_checkout()

        confirmation_page = ConfirmationPage(self.driver)
        message = confirmation_page.get_confirmation_message()
        logger.info(f"Confirmation message: {message}")

        assert "Thank you for your order!" in message
        logger.info(" Order confirmation message verified successfully")
        logger.info("=== Test End ===")
