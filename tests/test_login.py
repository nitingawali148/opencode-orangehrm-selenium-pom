import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
VALID_USER = "Admin"
VALID_PASS = "admin123"
INVALID_PASS = "wrongpassword"


@pytest.fixture(scope="function")
def driver():
    """Setup and teardown driver."""
    drv = get_driver()
    yield drv
    drv.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    """Return LoginPage instance."""
    driver.get(BASE_URL)
    return LoginPage(driver)


@pytest.fixture(scope="function")
def logged_in_dashboard(driver):
    """Login and return DashboardPage instance."""
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(VALID_USER, VALID_PASS)
    return DashboardPage(driver)


class TestLogin:
    """Test cases for OrangeHRM login."""
    
    def test_valid_login(self, login_page):
        """Test successful login."""
        login_page.login(VALID_USER, VALID_PASS)
        dashboard = DashboardPage(login_page.driver)
        assert dashboard.is_dashboard_displayed()
        assert "dashboard" in dashboard.get_current_url().lower()
    
    def test_invalid_login(self, login_page):
        """Test login with wrong password."""
        login_page.login(VALID_USER, INVALID_PASS)
        error = login_page.get_error_message()
        assert "invalid" in error.lower()
    
    def test_empty_credentials(self, login_page):
        """Test login with empty fields."""
        login_page.click_login()
        error = login_page.get_error_message()
        assert len(error) > 0


class TestDashboard:
    """Test cases for Dashboard actions."""
    
    def test_navigate_to_admin_page(self, logged_in_dashboard):
        """Test navigation to Admin page."""
        dashboard = logged_in_dashboard
        dashboard.navigate_to_admin()
        assert "admin" in dashboard.get_current_url().lower()
    
    def test_navigate_to_pim_page(self, logged_in_dashboard):
        """Test navigation to PIM page."""
        dashboard = logged_in_dashboard
        dashboard.navigate_to_pim()
        assert "pim" in dashboard.get_current_url().lower()
    
    def test_navigate_to_leave_page(self, logged_in_dashboard):
        """Test navigation to Leave page."""
        dashboard = logged_in_dashboard
        dashboard.navigate_to_leave()
        assert "leave" in dashboard.get_current_url().lower()
    
    def test_scroll_dashboard(self, logged_in_dashboard):
        """Test scrolling the dashboard page."""
        dashboard = logged_in_dashboard
        dashboard.scroll_down(500)
        dashboard.scroll_up(500)
        assert dashboard.is_dashboard_displayed()
    
    def test_dashboard_widgets_visible(self, logged_in_dashboard):
        """Test that dashboard widgets are visible."""
        dashboard = logged_in_dashboard
        dashboard.scroll_down(300)
        assert dashboard.is_widget_visible("quick_launch") or dashboard.is_widget_visible("employee")
    
    def test_verify_dashboard_text(self, logged_in_dashboard):
        """Test verifying dashboard heading is displayed."""
        dashboard = logged_in_dashboard
        assert dashboard.is_dashboard_displayed()
    
    def test_back_to_dashboard(self, logged_in_dashboard):
        """Test navigating back to dashboard."""
        dashboard = logged_in_dashboard
        dashboard.navigate_to_pim()
        dashboard.navigate_to_dashboard()
        assert dashboard.is_dashboard_displayed()
