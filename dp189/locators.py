from selenium.webdriver.common.by import By


class LocatorBasePageSearch:
    """Locator for search field on base page"""

    SEARCH_FIELD = (By.CLASS_NAME, 'input-lg')

class LocatorsBasePageNavBar:
    """Locators for top navbar links on base page"""

    NAVBAR = (By.CLASS_NAME, 'list-inline')
    MY_ACCOUNT = (By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]')
    CURRENCY = (By.CLASS_NAME, 'btn-group')
    USD = (By.XPATH,'.//ul/li[3]/button')
    POUND = (By.XPATH, './/ul/li[2]/button')
    EUR = (By.XPATH, './/ul/li[1]/button')
    CONTACT_US = (By.XPATH, './/li[1]/a')
    LOGIN = (By.XPATH, './/ul/li[2]/a')
    REGISTER = (By.XPATH, './/ul/li[1]/a')
    WISH_LIST = (By.XPATH, './/li[3]/a')
    SHOPPING_CART = (By.XPATH, './/li[4]/a')
    CHECKOUT = (By.XPATH, './/li[5]/a')

class LocatorsBasePageMainMenu:
    """Locators for main menu on base page"""

    DESKTOPS = (By.XPATH, '//a[text()="Desktops"]')
    LAPTOPS_NOTEBOOKS = (By.XPATH, '//a[text()="Laptops & Notebooks"]')
    COMPONENTS = (By.XPATH, '//a[text()="Components"]')
    TABLETS = (By.XPATH, '//a[text()="Tablets"]')
    SOFTWARE = (By.XPATH, '//a[text()="Software"]')
    PHONES_PDAS = (By.XPATH, '//a[text()="Phones & PDAs"]')
    CAMERAS = (By.XPATH, '//a[text()="Cameras"]')
    MP3_PLAYERS = (By.XPATH, '//a[text()="MP3 Players"]')


class LocatorsRightMenuRegisterPage:
    """"Locators for right menu on Register and Login pages"""

    RIGHT_MENU = (By.CLASS_NAME, 'list-group')
    LOGIN = (By.XPATH, './/a[text()="Login"]')
    REGISTER = (By.XPATH, './/a[text()="Register"]')
    FORGOTTEN_PASSWORD = (By.XPATH, './/a[text()="Forgotten Password"]')
    MY_ACCOUNT = (By.XPATH, './/a[text()="My Account"]')
    EDIT_ACCOUNT = (By.XPATH, './/a[text()="Edit Account"]')
    PASSWORD = (By.XPATH, './/a[text()="Password"]')
    ADDRESS_BOOK = (By.XPATH, './/a[text()="Address Book"]')
    WISH_LIST = (By.XPATH, './/a[text()="Wish List"]')
    ORDER_HISTORY = (By.XPATH, './/a[text()="Order History"]')
    DOWNLOADS = (By.XPATH, './/a[text()="Downloads"]')
    RECURRING_PAYMENTS = (By.XPATH, './/a[text()="Recurring payments"]')
    REWARD_POINTS = (By.XPATH, './/a[text()="Reward Points"]')
    RETURNS = (By.XPATH, './/a[text()="Returns"]')
    TRANSACTIONS = (By.XPATH, './/a[text()="Transactions"]')
    NEWSLETTER = (By.XPATH, './/a[text()="Newsletter"]')
    LOGOUT = (By.XPATH, './/a[text()="Logout"]')


class LocatorsShoppingCartButton:
    SHOP_CART_BUTTON = (By.XPATH, '/html/body/header/div/div/div[3]/div/button')
    CART_ITEMS = (By.XPATH, '/html/body/header/div/div/div[3]/div/ul/li[1]/table')


class LocatorYourStoreLink:
    YOUR_STORE = (By.XPATH, '/html/body/header/div/div/div[1]/div/h1/a')


class LocatorsHomePage:
    # TODO correct xpathes
    FEATURED_PRODUCT = (By.CLASS_NAME, 'product-layout')
    CAPTION = (By.XPATH, './/div/div[2]/h4/a')
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[3]/button[1]')


class LocatorsYourPersonalDetailsComponent:
    """Locators fot the 'Your Personal Details' component."""

    FIRST_NAME_FIELD = (By.XPATH, '//*[@id="input-firstname"]')
    LAST_NAME_FIELD = (By.XPATH, '//*[@id="input-lastname"]')
    EMAIL_FIELD = (By.XPATH, '//*[@id="input-email"]')
    TELEPHONE_FIELD = (By.XPATH, '//*[@id="input-telephone"]')


class LocatorsYourPasswordComponent:
    """Locators fot the 'Your Password' component."""

    PASSWORD_FIELD = (By.XPATH, '//*[@id="input-password"]')
    PASSWORD_CONFIRM_FIELD = (By.XPATH, '//*[@id="input-confirm"]')


class LocatorsRegisterPage:
    """Locators fot the 'Register' page."""

    CHECKBOX_PRIVACY_POLICY = (By.NAME, 'agree')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="content"]/form/div/div/input[2]')


class LocatorsNewsletterComponent:
    """Locators fot the 'Newsletter' component."""

    SUBSCRIBE_RADIO_BUTTONS = (By.NAME, 'newsletter')


class LocatorsForgotPasswordPage:
    """Locators fot the 'Forgot password' page."""

    EMAIL_FIELD = (By.ID, "input-email")
    BACK_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@class='btn btn-primary']")
