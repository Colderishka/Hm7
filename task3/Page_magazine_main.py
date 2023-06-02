#задание 3 
from selenium.webdriver.common.by import By


class MainPage():

    def __init__(self, driver):
        self._driver = driver
    
    def add_item(self, xpath_item1, xpath_item2, xpath_item3):
        self._driver.find_element(By.CSS_SELECTOR, xpath_item1).click()
        self._driver.find_element(By.CSS_SELECTOR, xpath_item2).click()
        self._driver.find_element(By.CSS_SELECTOR, xpath_item3).click()
        self._driver.find_element(By.CSS_SELECTOR, "[class='shopping_cart_link']").click()
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    