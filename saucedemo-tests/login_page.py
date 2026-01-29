
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def input_username(self, username):
        self.driver.find_element(By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def input_password(self, password):
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()

    def get_error_message(self):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        except:
            return ""

    def is_login_button_enabled(self):
        return self.driver.find_element(By.ID, "login-button").is_enabled()
