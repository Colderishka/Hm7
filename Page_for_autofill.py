#задание 1
from selenium.webdriver.common.by import By


class PageAutofil():

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def autofill(self):
        path_Fname = '[name="first-name"]'
        self._driver.find_element(By.CSS_SELECTOR, path_Fname).send_keys("Иван")
        self.filled1_css = self._driver.find_element(By.CSS_SELECTOR, path_Fname).value_of_css_property("color")

        path_Lname = '[name="last-name"]'
        self._driver.find_element(By.CSS_SELECTOR, path_Lname).send_keys("Петров")
        self.filled2_css = self._driver.find_element(By.CSS_SELECTOR, path_Lname).value_of_css_property("color")

        path_address = '[name="address"]'
        self._driver.find_element(By.CSS_SELECTOR, path_address).send_keys("Ленина, 55-3")
        self.filled3_css = self._driver.find_element(By.CSS_SELECTOR, path_address).value_of_css_property("color")

        path_mail = '[name="e-mail"]'
        self._driver.find_element(By.CSS_SELECTOR, path_mail).send_keys("test@skypro.com")
        self.filled4_css = self._driver.find_element(By.CSS_SELECTOR, path_mail).value_of_css_property("color")

        path_phone = '[name="phone"]'
        self._driver.find_element(By.CSS_SELECTOR, path_phone).send_keys("+7985899998787")
        self.filled5_css = self._driver.find_element(By.CSS_SELECTOR, path_phone).value_of_css_property("color")

        path_city = '[name="city"]'
        self._driver.find_element(By.CSS_SELECTOR, path_city).send_keys("Москва")
        self.filled6_css = self._driver.find_element(By.CSS_SELECTOR, path_city).value_of_css_property("color")

        path_country = '[name="country"]'
        self._driver.find_element(By.CSS_SELECTOR, path_country).send_keys("Россия")
        self.filled7_css = self._driver.find_element(By.CSS_SELECTOR, path_country).value_of_css_property("color")

        path_job_possion = '[name="job-position"]'
        self._driver.find_element(By.CSS_SELECTOR, path_job_possion).send_keys("QA")
        self.filled8_css = self._driver.find_element(By.CSS_SELECTOR, path_job_possion).value_of_css_property("color")

        path_company = '[name="company"]'
        self._driver.find_element(By.CSS_SELECTOR, path_company).send_keys("SkyPro")
        self.filled9_css = self._driver.find_element(By.CSS_SELECTOR, path_company).value_of_css_property("color")
        
    def click_on_button(self):   
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    
    def compare(self):
        unfilled_css = self._driver.find_element(By.CSS_SELECTOR, '[class="alert py-2 alert-danger"]').value_of_css_property("color")
        green_css = 'rgba(33, 37, 41, 1)'
        assert unfilled_css == 'rgba(132, 32, 41, 1)'
        assert green_css == self.filled1_css
        assert green_css == self.filled2_css
        assert green_css == self.filled3_css
        assert green_css == self.filled4_css
        assert green_css == self.filled5_css
        assert green_css == self.filled6_css
        assert green_css == self.filled7_css
        assert green_css == self.filled8_css
        assert green_css == self.filled9_css
            
    