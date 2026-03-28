import pytest
import os


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure."""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = None
        
        if hasattr(item, "funcargs"):
            if "driver" in item.funcargs:
                driver = item.funcargs["driver"]
            elif "login_page" in item.funcargs:
                driver = item.funcargs["login_page"].driver
        
        if driver:
            screenshot_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
            os.makedirs(screenshot_dir, exist_ok=True)
            
            screenshot_name = f"{item.nodeid.replace('::', '_').replace('/', '_').replace('tests_', '')}_failed.png"
            driver.save_screenshot(os.path.join(screenshot_dir, screenshot_name))
