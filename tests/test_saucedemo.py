import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage

@pytest.mark.usefixtures("setup")
class TestSauceDemo:

    def test_complete_flow(self):
        login = LoginPage(self.driver)
        products = ProductsPage(self.driver)
        cart = CartPage(self.driver)
        checkout = CheckoutPage(self.driver)
        confirmation = ConfirmationPage(self.driver)

        # Login
        login.login("standard_user", "secret_sauce")
        assert login.verify_login_success(), "User login failed!"
        print("User logged in successfully!!!")

        # Verify products visible
        assert products.get_all_products(), "No products found on Products page!"

        # Add to cart
        product_id = "sauce-labs-backpack"
        assert products.add_product_to_cart(product_id), "Product not added to cart!"
        products.go_to_cart()

        # # Verify in cart
        # assert cart.verify_product_in_cart("Sauce Labs Backpack"), "Product missing in cart!"
        # print(" Product successfully added to cart and visible in cart page.")

        # # Checkout
        # cart.proceed_to_checkout()
        # checkout.fill_information("John", "Doe", "431608")
        # checkout.finish_checkout()
        #
        # # Confirmation
        # msg = confirmation.get_confirmation_message()
        # print(msg)
        # assert "Thank you for your order!" in msg
