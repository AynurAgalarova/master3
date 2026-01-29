
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_loaded(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.ID, "inventory_container"))
        )

    def is_inventory_displayed(self):
        return self.driver.find_element(By.ID, "inventory_container").is_displayed()
