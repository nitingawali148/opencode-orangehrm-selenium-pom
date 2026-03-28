from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import LoginLocators


class LoginPage:
    """Login page object with element actions."""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def enter_username(self, username):
        """Enter username."""
        element = self.wait.until(EC.visibility_of_element_located(LoginLocators.USERNAME))
        element.clear()
        element.send_keys(username)
    
    def enter_password(self, password):
        """Enter password."""
        element = self.wait.until(EC.visibility_of_element_located(LoginLocators.PASSWORD))
        element.clear()
        element.send_keys(password)
    
    def click_login(self):
        """Click login button."""
        element = self.wait.until(EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON))
        element.click()
    
    def login(self, username, password):
        """Perform login."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self):
        """Get error message text."""
        element = self.wait.until(EC.visibility_of_element_located(LoginLocators.ERROR_MESSAGE))
        return element.text
