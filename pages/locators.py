from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='orangehrm-login-error']//p")


class DashboardLocators:
    DASHBOARD_HEADING = (By.XPATH, "//h6[text()='Dashboard']")
    PROFILE_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-name")
    
    MENU_ADMIN = (By.XPATH, "//span[text()='Admin']")
    MENU_PIM = (By.XPATH, "//span[text()='PIM']")
    MENU_LEAVE = (By.XPATH, "//span[text()='Leave']")
    MENU_TIME = (By.XPATH, "//span[text()='Time']")
    MENU_RECRUITMENT = (By.XPATH, "//span[text()='Recruitment']")
    MENU_DASHBOARD = (By.XPATH, "//span[text()='Dashboard']")
    
    WIDGET_EMPLOYEE = (By.XPATH, "//div[contains(@class,'chart-legend')]")
    WIDGET_QUICK_LAUNCH = (By.XPATH, "//div[contains(@class,'quick-launch')]")
    WIDGET_TIME_AT_WORK = (By.XPATH, "//div[contains(@class,'time-at-work')]")
    
    QUICK_LAUNCH_ICONS = (By.XPATH, "//div[contains(@class,'quick-launch')]//a")
    
    PAGE_HEADERS = {
        "admin": (By.XPATH, "//h5[contains(text(),'User Management')]"),
        "pim": (By.XPATH, "//h5[contains(text(),'Employee')]"),
        "leave": (By.XPATH, "//h5[contains(text(),'Leave')]"),
        "recruitment": (By.XPATH, "//h5[contains(text(),'Recruitment')]")
    }
