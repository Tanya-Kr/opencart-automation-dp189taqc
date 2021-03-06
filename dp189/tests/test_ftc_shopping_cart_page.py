import pytest
from dp189.pages.product_page import ProductPage
from dp189.pages.shopping_cart_page import ShoppingCartPage
from dp189.tests.conftest import get_test_data
from dp189.tests.base_test import BaseTest
from dp189.routes import *
from dp189.constants import ShoppingCartPageConstants


class TestShoppingCart(BaseTest):
    def setup(self):
        self.driver.maximize_window()

        self.driver.get(get_product_url('40'))
        product = ProductPage(self.driver)
        product.available_options.click_add_to_cart_button()
        product.catch_info_message.get_info_message()

        self.driver.get(CART_PAGE_URL)
        self.cart = ShoppingCartPage(self.driver)
        self.cart.generate_products_list()

    def test_shopping_cart_change_quantity_positive(self):
        """Positive test to check correct changing quantity of product.
        :param expected: str
        """
        self.cart.change_product_quantity(ShoppingCartPageConstants.TEST_ITEM1, '5')

        assert ShoppingCartPageConstants.RESULT in self.cart.catch_info_message.get_info_message()

    @pytest.mark.parametrize('test_input,expected',
                             get_test_data('shopping_cart/test_data_shopping_cart_quantity.csv'))
    def test_shopping_cart_change_quantity_negative(self, test_input: str, expected: str):
        """Negative test for checking changes in the cart when invalid data is entered.
        :param test_input: str
        :param expected: str
        """
        self.cart.change_product_quantity(ShoppingCartPageConstants.TEST_ITEM1, test_input)

        assert self.cart.get_text_empty_cart() == expected

    def test_use_coupon_code(self):
        """Positive test for checking success message display after apply coupon code."""
        self.cart.coupon_panel.open_coupon_panel()
        self.cart.coupon_panel.coupon_field.clear_and_fill_input_field('2222')
        self.cart.coupon_panel.click_apply_coupon_button()

        assert ShoppingCartPageConstants.RESULT4 in self.cart.catch_info_message.get_info_message()

    def test_shopping_cart_click_remove_button(self):
        """Positive test to check correct changing after remove product from shopping cart."""
        self.cart.click_remove_product_button(ShoppingCartPageConstants.TEST_ITEM1)

        assert ShoppingCartPageConstants.RESULT3 == self.cart.get_text_empty_cart()

    def test_shopping_cart_estimate_shipping_and_taxes(self):
        """Positive test for checking success message display after fill Estimate Shipping & Taxes field."""
        self.cart.estimate_shipping_panel.open_estimate_shipping_panel()
        self.cart.estimate_shipping_panel.country_selector.choose_dropdown_option('Ukraine')
        self.cart.estimate_shipping_panel.region_selector.choose_dropdown_option('Kyiv')
        self.cart.estimate_shipping_panel.click_get_quotes_button()

        self.cart.estimate_shipping_panel.modal_shipping_radio_button.choose_radio_button_option(
            ShoppingCartPageConstants.TEST_ITEM2)
        self.cart.estimate_shipping_panel.click_modal_apply_shipping_button()

        assert ShoppingCartPageConstants.RESULT5 in self.cart.catch_info_message.get_info_message()

    def test_checkout_button(self):
        """Positive test for checking button 'Checkout'"""
        self.cart.click_checkout_button()
        assert self.cart.get_title.get_title_page(ShoppingCartPageConstants.CHECKOUT_TITLE) == 'Checkout'

    def test_catch_info_message_update_quantity(self):
        """Positive test for catching info message about update quantity of products in shopping cart"""
        self.cart = self.cart.change_product_quantity(ShoppingCartPageConstants.TEST_ITEM1, "2")
        assert ShoppingCartPageConstants.RESULT in self.cart.catch_info_message.get_info_message()

    def test_total_price_of_product(self):
        """Positive test for checking total price of product after update quantity"""
        self.cart = self.cart.change_product_quantity(ShoppingCartPageConstants.TEST_ITEM1, "2")
        self.cart.generate_products_list()
        total_price = self.cart.get_product_total_price(ShoppingCartPageConstants.TEST_ITEM1)
        assert ShoppingCartPageConstants.RESULT2 == total_price

    def test_continue_button(self):
        """Positive test for checking work 'Continue' button"""
        self.cart.click_continue_shipping_button()
        assert self.cart.get_title.get_title_page(ShoppingCartPageConstants.HOME_TITLE) == 'Your Store'
