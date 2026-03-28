# OrangeHRM Selenium Automation Framework

A Page Object Model (POM) automation framework for testing the OrangeHRM demo website using Selenium and Python.

## Features

- Page Object Model design pattern
- Separate locators file for easy maintenance
- Chrome WebDriver with Selenium 4
- Pytest for test execution
- HTML report generation with pytest-html
- Screenshot capture on test failures

## Project Structure

```
OrangeHRM_Automation/
├── pages/
│   ├── locators.py       # All XPaths and locators
│   ├── login_page.py     # Login page object
│   └── dashboard_page.py  # Dashboard page object
├── tests/
│   └── test_login.py     # Test cases
├── utils/
│   └── driver_factory.py # WebDriver setup
├── reports/               # HTML reports
├── conftest.py           # Pytest configuration
└── requirements.txt      # Dependencies
```

## Setup

1. Install Python 3.7+

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests with HTML report:
```bash
pytest tests/test_login.py -v --html=reports/report.html --screenshot=on
```

Run specific test:
```bash
pytest tests/test_login.py::TestLogin::test_valid_login -v
```

## Test Cases

### Login Tests
- `test_valid_login` - Verify successful login with valid credentials
- `test_invalid_login` - Verify error message for invalid password
- `test_empty_credentials` - Verify error for empty fields

### Dashboard Tests
- `test_navigate_to_admin_page` - Navigate to Admin page
- `test_navigate_to_pim_page` - Navigate to PIM page
- `test_navigate_to_leave_page` - Navigate to Leave page
- `test_scroll_dashboard` - Scroll dashboard page
- `test_dashboard_widgets_visible` - Verify widgets are displayed
- `test_verify_dashboard_text` - Verify dashboard heading
- `test_back_to_dashboard` - Navigate back to dashboard

## Test Data

- **URL**: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
- **Username**: Admin
- **Password**: admin123

## Dependencies

- selenium==4.15.0
- pytest==7.4.3
- pytest-html==4.1.1
