"""Module for the testing 'Register' page."""

import pytest
from dp189.pages.register_page import RegisterPage
from dp189.pages.home_page import HomePage
from dp189.tests.base_test import BaseTest
from dp189.tests.conftest import get_test_data
from dp189.routes import *


class TestRegisterPage(BaseTest):
    """Class for the 'Register' page."""

    def setup(self) -> None:
        """Setup for the test.

        :return: None
        """

        self.driver.maximize_window()
        self.driver.get(HOME_PAGE_URL)
        self.home_page = HomePage(self.driver)
        self.home_page.click_account_and_go_to_register()

        self.register_page = RegisterPage(self.driver)

    @pytest.mark.parametrize('test_input', get_test_data('register_page/first_name_positive.csv'))
    def test_check_first_name_field_valid_data(self, test_input: str) -> None:
        """Check the 'First name' field with valid data on register page.

        :param test_input: test data for 'first name' field
        :return: None
        """

        self.register_page.your_personal_details_form.first_name_field.clear_and_fill_input_field(test_input)
        self.register_page.privacy_policy_checkbox.agree_with_privacy_policy()
        self.register_page.click_continue_button()

        assert not self.register_page.your_personal_details_form.first_name_field.error_message.get_error_message()

    def test_check_email_field_valid_data(self) -> None:
        """Check the 'Email' field with valid data on register page.

        :return: None
        """

        self.register_page.your_personal_details_form.email_field.clear_and_fill_input_field('test@gmail.com')
        self.register_page.click_continue_button()

        assert not self.register_page.your_personal_details_form.email_field.error_message.get_error_message()
