#задание 2 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageCalcul():

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.waiter = WebDriverWait(driver, 50)
    
    def clicker(self, settime, xpath_key, xpath_key2, xpath_key3):
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(settime)
        self._driver.find_element(By.XPATH, xpath_key).click()
        self._driver.find_element(By.XPATH, xpath_key2).click()
        self._driver.find_element(By.XPATH, xpath_key3).click()
        self._driver.find_element(By.CSS_SELECTOR, "[class='btn btn-outline-warning']").click()

    def wait(self):
        self.waiter.until(EC.text_to_be_present_in_element( (By.CSS_SELECTOR, "[class='screen']"), '15'))
        
    def res(self):
        result = self._driver.find_element(By.CSS_SELECTOR, "[class='screen']")
        return result.text
