#задание 3 
from selenium.webdriver.common.by import By


class Checkout():

    def __init__(self, driver):
        self._driver = driver
    
    def fill_checkout_information(self, Fname, Lname, code):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(Fname)
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(Lname)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(code)
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()
        
    def res(self): 
        result = self._driver.find_element(By.CSS_SELECTOR, "[class='summary_info_label summary_total_label']")
        return result.text