from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_driver():
    """Initialize Chrome WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    return driver
