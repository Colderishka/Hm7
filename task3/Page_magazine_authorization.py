# задание 3
from selenium.webdriver.common.by import By

class PageMagazine():

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://www.saucedemo.com/")

    def authorization(self, user, password):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(user)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

