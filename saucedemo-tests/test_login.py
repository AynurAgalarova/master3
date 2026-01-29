
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure



@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


class LoginPage:
    pass


class InventoryPage:
    pass


@allure.feature("Авторизация")
@allure.story("Успешный логин")
def test_successful_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.wait_until_loaded()
    assert "inventory.html" in driver.current_url, "Перевели на страницу товаров"
    assert inventory_page.is_inventory_displayed(), "Инвентори отображается"

@allure.feature("Авторизация"
)
@allure.story("Логин с неверным паролем")
def test_wrong_password(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "wrong_password")

    assert "inventory.html" not in driver.current_url
    assert "Username and password do not match" in login_page.get_error_message()

@allure.feature("Авторизация")
@allure.story("Логин заблокированного пользователя")
def test_locked_out_user(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    assert "inventory.html" not in driver.current_url
    assert "locked out" in login_page.get_error_message().lower()

@allure.feature("Авторизация")
@allure.story("Логин с пустыми полями")
def test_empty_fields(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("", "")

    # Проверяем, что кнопка логина активна, но при клике появится ошибка
    assert login_page.is_login_button_enabled()
    assert login_page.get_error_message() == ""  # Сообщение может появиться после клика, но пока пустое

    # Чтобы сгенерировать ошибку, кликаем
    login_page.click_login()
    assert "Username is required" in login_page.get_error_message()

@allure.feature("Авторизация")
@allure.story("Логин пользователя performance_glitch_user")
def test_performance_glitch_user(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("performance_glitch_user", "secret_sauce")

    inventory_page.wait_until_loaded(timeout=20)  # Увеличенный таймаут из-за задержек

    assert "inventory.html" in driver.current_url
    assert inventory_page.is_inventory_displayed()