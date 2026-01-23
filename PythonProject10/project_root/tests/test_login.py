
# tests/test_login.py
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # или другой драйвер
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get("https://example.com/login")
    login_page = LoginPage(driver)

    login_page.enter_username("user")
    login_page.enter_password("pass")
    login_page.click_login()

    assert "dashboard" in driver.current_url
