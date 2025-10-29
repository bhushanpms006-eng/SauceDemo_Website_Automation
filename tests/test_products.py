import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.read_config import get_base_url, config
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.usefixtures("setup")
class TestProducts:
    def test_add_product_to_cart(self, driver):
        logger.info("Starting test: test_add_product_to_cart")

        driver.get(get_base_url())

        login_page = LoginPage(driver)
        login_page.login_to_application(
            config.get("DEFAULT", "username"),
            config.get("DEFAULT", "password")
        )

        products_page = ProductsPage(driver)
        product_list = products_page.get_all_products()
        logger.info(f"Products available: {product_list}")

        if not product_list:
            pytest.skip("No products found to add in cart.")

        # Example product id (can be read from configs)
        product_id = "sauce-labs-backpack"
        products_page.add_product_to_cart(product_id)
        logger.info(f"Product '{product_id}' added to cart successfully.")

        products_page.go_to_cart()
        assert "cart" in driver.current_url, "Failed to navigate to cart page."
        logger.info("Navigated to cart page successfully.")
