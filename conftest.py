import pytest
import os
from datetime import datetime


def pytest_configure(config):
    """Configure HTML report with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"reports/report_{timestamp}.html"
    config.option.self_contained_html = True
