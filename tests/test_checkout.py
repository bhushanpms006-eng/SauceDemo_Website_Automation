import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from utils.read_config import get_base_url, config
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.usefixtures("setup")
class TestCheckout:
    def test_complete_checkout_flow(self, driver):
        logger.info("Starting test: test_complete_checkout_flow")

        driver.get(get_base_url())

        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.login_to_application(
            config.get("DEFAULT", "username"),
            config.get("DEFAULT", "password")
        )
        logger.info("User logged in successfully.")

        # Step 2: Add product
        products_page = ProductsPage(driver)
        product_id = "sauce-labs-bike-light"
        products_page.add_product_to_cart(product_id)
        products_page.go_to_cart()
        logger.info(f"Product '{product_id}' added and navigating to cart page.")

        # Step 3: Verify product in cart
        cart_page = CartPage(driver)
        assert cart_page.verify_product_in_cart("Sauce Labs Bike Light")
        cart_page.proceed_to_checkout()
        logger.info("Product verified in cart and proceeded to checkout page.")

        # Step 4: Checkout details
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_information("John", "Doe", "12345")
        checkout_page.finish_checkout()
        logger.info("Checkout information submitted and finished checkout.")

        # Step 5: Confirmation
        confirmation_page = ConfirmationPage(driver)
        message = confirmation_page.get_confirmation_message()

        assert "Thank you for your order!" in message
        logger.info("Order confirmed successfully. Confirmation message validated.")
