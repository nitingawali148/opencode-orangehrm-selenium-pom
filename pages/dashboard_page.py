from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import DashboardLocators


class DashboardPage:
    """Dashboard page object with navigation and widget actions."""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def is_dashboard_displayed(self):
        """Check if dashboard is visible."""
        try:
            self.wait.until(EC.visibility_of_element_located(DashboardLocators.DASHBOARD_HEADING))
            return True
        except:
            return False
    
    def get_current_url(self):
        """Get current URL."""
        return self.driver.current_url
    
    def navigate_to_menu(self, menu_name):
        """Navigate to any menu item."""
        locators = {
            "admin": DashboardLocators.MENU_ADMIN,
            "pim": DashboardLocators.MENU_PIM,
            "leave": DashboardLocators.MENU_LEAVE,
            "dashboard": DashboardLocators.MENU_DASHBOARD,
            "recruitment": DashboardLocators.MENU_RECRUITMENT
        }
        element = self.wait.until(EC.element_to_be_clickable(locators.get(menu_name.lower())))
        element.click()
    
    def navigate_to_admin(self):
        """Navigate to Admin page."""
        self.navigate_to_menu("admin")
        self.wait.until(EC.url_contains("admin"))
    
    def navigate_to_pim(self):
        """Navigate to PIM page."""
        self.navigate_to_menu("pim")
        self.wait.until(EC.url_contains("pim"))
    
    def navigate_to_leave(self):
        """Navigate to Leave page."""
        self.navigate_to_menu("leave")
        self.wait.until(EC.url_contains("leave"))
    
    def navigate_to_dashboard(self):
        """Navigate to Dashboard page."""
        self.navigate_to_menu("dashboard")
        self.wait.until(EC.visibility_of_element_located(DashboardLocators.DASHBOARD_HEADING))
    
    def scroll_down(self, pixels=500):
        """Scroll down the page."""
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
    
    def scroll_up(self, pixels=500):
        """Scroll up the page."""
        self.driver.execute_script(f"window.scrollBy(0, -{pixels});")
    
    def is_widget_visible(self, widget_type):
        """Check if a widget is visible."""
        locators = {
            "employee": DashboardLocators.WIDGET_EMPLOYEE,
            "quick_launch": DashboardLocators.WIDGET_QUICK_LAUNCH,
            "time_at_work": DashboardLocators.WIDGET_TIME_AT_WORK
        }
        locator = locators.get(widget_type.lower())
        if locator:
            try:
                self.wait.until(EC.visibility_of_element_located(locator))
                return True
            except:
                return False
        return False
    
    def click_quick_launch_icon(self, index=0):
        """Click a quick launch icon by index."""
        icons = self.wait.until(EC.presence_of_all_elements_located(DashboardLocators.QUICK_LAUNCH_ICONS))
        if len(icons) > index:
            icons[index].click()
    
    def verify_page_contains_text(self, text):
        """Verify text is visible on page."""
        text_locator = (By.XPATH, f"//*[contains(text(),'{text}')]")
        try:
            element = self.wait.until(EC.visibility_of_element_located(text_locator))
            return element.is_displayed()
        except:
            return False
