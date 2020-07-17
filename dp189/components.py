from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Remote
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from dp189.locators import LocatorsSearch, LocatorsNavBar, RightMenuLocators, LocatorsShoppingCartButton, \
    LocatorsYourPersonalDetailsComponent, LocatorsYourPasswordComponent, LocatorsRegisterPage, \
    LocatorsNewsletterComponent


class SearchArea:
    """"This class describes the search area common in all pages. It consists or search field and search button"""

    def __init__(self, driver):
        self._driver = driver
        self._search_field = driver.find_element(*LocatorsSearch.SEARCH_FIELD)
        self._search_button = driver.find_element(*LocatorsSearch.SEARCH_BUTTON)

    def fill_search_field_and_hit_return(self, item: str):
        self._search_field.clear()
        self._search_field.send_keys(item).send_keys(Keys.RETURN)
        # return SearchPage(self._driver)

    def fill_search_field_and_click(self, item: str):
        self._search_field.clear()
        self._search_field.send_keys(item)
        self._search_button.click()
        # return SearchPage(self._driver)


class ShopCartButton:
    # TODO test functionality
    def __init__(self, driver):
        self._driver = driver
        self._shop_cart_button = driver.find_element(*LocatorsShoppingCartButton.SHOP_CART_BUTTON)

    def click_shop_cart_button(self):
        self._shop_cart_button.click()
        cart_items = self._driver.find_elements(*LocatorsShoppingCartButton.CART_ITEMS)
        if len(cart_items) == 0:
            return 'Your cart is empty!'
        else:
            return ShopCartDropdown(self._driver)


class ShopCartDropdown:
    def __init__(self, driver):
        pass


class BaseNavBar:
    """This class describes the top nav bar of the base page"""

    def __init__(self, driver):
        self._driver = driver
        self._currency = driver.find_element(*LocatorsNavBar.CURRENCY)
        self._nav_bar = driver.find_element(*LocatorsNavBar.NAVBAR)

    def click_currency_euro(self):
        self._currency.click()
        self._currency.find_element(*LocatorsNavBar.EUR).click()

    def click_currency_pound(self):
        self._currency.click()
        self._currency.find_element(*LocatorsNavBar.POUND).click()

    def click_currency_usd(self):
        self._currency.click()
        self._currency.find_element(*LocatorsNavBar.USD).click()

    def click_contact_us(self):
        self._nav_bar.find_element(*LocatorsNavBar.CONTACT_US).click()

    def click_wishlist(self):
        self._nav_bar.find_element(*LocatorsNavBar.WISH_LIST).click()

    def click_shopping_cart(self):
        self._nav_bar.find_element(*LocatorsNavBar.SHOPPING_CART).click()


class BaseRightMenu:
    def __init__(self, driver) -> None:
        self._driver = driver
        self._right_menu = driver.find_element_by_class_name('list-group')

    def click_my_account(self):
        self._right_menu.find_element(*RightMenuLocators.MY_ACCOUNT).click()

    def click_address_book(self):
        self._right_menu.find_element(*RightMenuLocators.ADDRESS_BOOK).click()

    def click_wish_list(self):
        self._right_menu.find_element(*RightMenuLocators.WISH_LIST).click()

    def click_order_history(self):
        self._right_menu.find_element(*RightMenuLocators.ORDER_HISTORY).click()

    def click_downloads(self):
        self._right_menu.find_element(*RightMenuLocators.DOWNLOADS).click()

    def click_recurring_payments(self):
        self._right_menu.find_element(*RightMenuLocators.RECURRING_PAYMENTS).click()

    def click_reward_points(self):
        self._right_menu.find_element(*RightMenuLocators.REWARD_POINTS).click()

    def click_returns(self):
        self._right_menu.find_element(*RightMenuLocators.RETURNS).click()

    def click_transactions(self):
        self._right_menu.find_element(*RightMenuLocators.TRANSACTIONS).click()

    def click_newsletter(self):
        self._right_menu.find_element(*RightMenuLocators.NEWSLETTER).click()


class YourPersonalDetailsComponent:
    """Your personal details form сonsists four fields to fill first name, last name, email, telephone."""

    def __init__(self, driver: Remote) -> None:
        """Initialize input fields first name, last name, email, telephone.

        :param driver: Remote.
        """
        self._driver = driver
        self.first_name_field = InputFieldComponent(self._driver, LocatorsYourPersonalDetailsComponent.FIRST_NAME_FIELD)
        self.last_name_field = InputFieldComponent(self._driver, LocatorsYourPersonalDetailsComponent.LAST_NAME_FIELD)
        self.email_field = InputFieldComponent(self._driver, LocatorsYourPersonalDetailsComponent.EMAIL_FIELD)
        self.telephone_field = InputFieldComponent(self._driver, LocatorsYourPersonalDetailsComponent.TELEPHONE_FIELD)


class YourPasswordComponent:
    """Your password form сonsists two fields to fill password, password confirm."""

    def __init__(self, driver: Remote) -> None:
        """Initialize input fields password field, password confirm field.

        :param driver: Remote
        :return: None
        """
        self._driver = driver
        self.password_field = InputFieldComponent(self._driver, LocatorsYourPasswordComponent.PASSWORD_FIELD)
        self.password_confirm_field = InputFieldComponent(self._driver,
                                                          LocatorsYourPasswordComponent.PASSWORD_CONFIRM_FIELD)


class InputFieldComponent:
    """An input field to fill with data from user."""

    def __init__(self, driver: Remote, input_field_locator: tuple, parent_element: WebElement = None) -> None:
        """Initialize the input field.

        :param driver: Remote
        :param input_field_locator: tuple (example: PASSWORD_FIELD=(By.ID, 'input-password'))
        :return: None
        """
        self._driver = driver
        self.input_field_locator = input_field_locator
        self.parent_element = parent_element
        if self.parent_element:
            self.input_field = self.parent_element.find_element(*self.input_field_locator)
        else:
            self.input_field = self._driver.find_element(*self.input_field_locator)
        self.error_message = ErrorMessageComponent(self._driver, self.input_field_locator)

    def clear_and_fill_input_field(self, data: str) -> None:
        """Clear and fill input field with data.

        :param data: str
        :return: None
        """
        self.input_field = self._driver.find_element(*self.input_field_locator)
        self.input_field.clear()
        self.input_field.send_keys(data)


class RadioButtonComponent:
    """Radio buttons to choose some option and check if required option is chosen."""

    def __init__(self, driver: Remote, radio_buttons_locator: tuple, parent_element: WebElement = None) -> None:
        """Initialize radio buttons.

        :param driver: Remote
        :param radio_buttons_locator: tuple
        :return: None
        """
        self._driver = driver
        self.radio_buttons_locator = radio_buttons_locator
        self.parent_element = parent_element
        if self.parent_element:
            self.radio_buttons_container = self.parent_element.find_element(*self.radio_buttons_locator)
        else:
            self.radio_buttons_container = self._driver.find_element(*self.radio_buttons_locator)
        self.error_message = ErrorMessageComponent(self._driver, self.radio_buttons_locator)

    def option_is_checked(self, data: str) -> bool:
        """Check if required option is chosen.

        :param data: str
        :return: bool
        """
        return self.radio_buttons_container.find_element(By.XPATH, f'//label[contains(.,"{data}")]/input').is_selected()

    def choose_radio_button_option(self, data: str) -> None:
        """Choose some option.

        :param data: str
        :return: None
        """
        self.radio_buttons_container.find_element(By.XPATH, f'//label[contains(.,"{data}")]/input').click()


class CheckboxComponent:
    """Checkbox to choose option and check if required option is chosen."""

    def __init__(self, driver: Remote, checkbox_locator: tuple, parent_element: WebElement = None) -> None:
        """Initialize checkbox.

        :param driver: Remote
        :param checkbox_locator: tuple
        :return: None
        """
        self._driver = driver
        self.checkbox_locator = checkbox_locator
        self.parent_element = parent_element
        if self.parent_element:
            self.checkbox_container = self.parent_element.find_element(*self.checkbox_locator)
        else:
            self.checkbox_container = self._driver.find_element(*self.checkbox_locator)
        self.error_message = ErrorMessageComponent(self._driver, self.checkbox_locator)

    def option_is_checked(self, data: str) -> bool:
        """Check if required option is chosen.

        :param data: str
        :return: bool
        """
        return self.checkbox_container.find_element(By.XPATH, f'//label[contains(.,"{data}")]/input').is_selected()

    def choose_checkbox_option(self, data: str) -> None:
        """Choose some option.

        :param data: str
        :return: None
        """
        self.checkbox_container.find_element(By.XPATH, f'//label[contains(.,"{data}")]/input').click()


class DropdownComponent:
    """Drop-down menu to choose option and check if required option is chosen."""

    def __init__(self, driver: Remote, dropdown_locator: tuple, parent_element: WebElement = None) -> None:
        """Initialize drop-down.

        :param driver: Remote
        :param dropdown_locator: tuple
        :return: None
        """
        self._driver = driver
        self.dropdown_locator = dropdown_locator
        self.parent_element = parent_element
        if self.parent_element:
            self.checkbox_container = Select(self.parent_element.find_element(*self.dropdown_locator))
        else:
            self.checkbox_container = Select(self._driver.find_element(*self.dropdown_locator))
        self.error_message = ErrorMessageComponent(self._driver, self.dropdown_locator)

    def option_is_checked(self, data: str) -> bool:
        """Check if required option is chosen.

        :param data: str
        :return: bool
        """
        word_list_option = self.checkbox_container.first_selected_option.text.split()
        return word_list_option[0] + ' ' + word_list_option[1] == data

    def choose_dropdown_option(self, data: str) -> None:
        """Choose some option.

        :param data: str
        :return: None
        """
        self.checkbox_container.select_by_visible_text(data)


class ErrorMessageComponent:
    """Error message for input fields, radio buttons, checkboxes, drop-down menus."""

    def __init__(self, driver: Remote, element_locator: tuple) -> None:
        """Initialize element locator to find error message for it.

        :param driver: Remote
        :param element_locator: tuple
        :return: None
        """
        self._driver = driver
        self.element_locator = element_locator

    def get_error_message(self) -> str:
        """Get error message.

        :return: str
        """
        error_message_locator = f'{self.element_locator[1]}/following-sibling::div[@class="text-danger"]'
        error_message = WebDriverWait(self._driver, 3).until(
            EC.presence_of_element_located((By.XPATH, error_message_locator))
        )
        return error_message.text


class NewsletterComponent:
    """Two radio buttons to subscribe or unsubscribe to newsletter."""

    def __init__(self, driver: Remote) -> None:
        """Initialize radio buttons.

        :param driver: Remote
        :return: None
        """
        self._driver = driver
        self.subscribe_radio_buttons_locator = LocatorsNewsletterComponent.SUBSCRIBE_RADIO_BUTTONS

    def is_subscribed(self) -> bool:
        """Check user is subscribed or not.

        :return: bool
        """
        self.subscribe_radio_buttons = self._driver.find_elements(*self.subscribe_radio_buttons_locator)
        for button in self.subscribe_radio_buttons:
            if button.get_attribute('checked') == 'true' and button.get_attribute('value') == '1':
                return True
        return False

    def subscribe_to_newsletter(self) -> None:
        """Subscribe to newsletter.

        :return: None
        """
        self.subscribe_to_newsletter_locator = f'[{self.subscribe_radio_buttons_locator[0]}="{self.subscribe_radio_buttons_locator[1]}"][value="1"]'
        self._driver.find_element_by_css_selector(self.subscribe_to_newsletter_locator).click()