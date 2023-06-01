#задание 3 
from selenium.webdriver.common.by import By


class Checkout():

    def __init__(self, driver):
        self._driver = driver
    
    def fill_checkout_information(self):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Павел")
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Петров")
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("13000")
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()
        
    def asserting(self): 
        result = self._driver.find_element(By.CSS_SELECTOR, "[class='summary_info_label summary_total_label']").text
        assert result == "Total: $58.29"