#задание 1
from selenium.webdriver.common.by import By

class PageAutofil():

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def autofill(self, Fname, Lname, address, email, phone, city, country, jposition, company):
        self.path_Fname = '[name="first-name"]'
        self.Fname = self._driver.find_element(By.CSS_SELECTOR, self.path_Fname).send_keys(Fname)
        
        self.path_Lname = '[name="last-name"]'
        self.Lname = self._driver.find_element(By.CSS_SELECTOR, self.path_Lname).send_keys(Lname)

        self.path_address = '[name="address"]'
        self.address = self._driver.find_element(By.CSS_SELECTOR, self.path_address).send_keys(address)

        self.path_mail = '[name="e-mail"]'
        self.email = self._driver.find_element(By.CSS_SELECTOR, self.path_mail).send_keys(email)

        self.path_phone = '[name="phone"]'
        self.phone = self._driver.find_element(By.CSS_SELECTOR, self.path_phone).send_keys(phone)

        self.path_city = '[name="city"]'
        self.city = self._driver.find_element(By.CSS_SELECTOR, self.path_city).send_keys(city)

        self.path_country = '[name="country"]'
        self.country = self._driver.find_element(By.CSS_SELECTOR, self.path_country).send_keys(country)

        self.path_job_possion = '[name="job-position"]'
        self.jposition = self._driver.find_element(By.CSS_SELECTOR, self.path_job_possion).send_keys(jposition)

        self.path_company = '[name="company"]'
        self.company = self._driver.find_element(By.CSS_SELECTOR, self.path_company).send_keys(company)
        
    def click_on_button(self):   
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        
    def unfilledcss(self):
        unfilled = self._driver.find_element(By.CSS_SELECTOR, '[class="alert py-2 alert-danger"]').value_of_css_property("color")
        return unfilled
    
    def get1_cssfilled(self):
        filled1_css = self._driver.find_element(By.CSS_SELECTOR, '[id="first-name"]').value_of_css_property("color")
        return filled1_css
    
    def get2_cssfilled(self):
        filled2_css = self._driver.find_element(By.CSS_SELECTOR, '[id="last-name"]').value_of_css_property("color")
        return filled2_css

    def get3_cssfilled(self):
        filled3_css = self._driver.find_element(By.CSS_SELECTOR, '[id="address"]').value_of_css_property("color")
        return filled3_css

    def get4_cssfilled(self):
        filled4_css = self._driver.find_element(By.CSS_SELECTOR, '[id="e-mail"]').value_of_css_property("color") 
        return filled4_css

    def get5_cssfilled(self):
        filled5_css = self._driver.find_element(By.CSS_SELECTOR, '[id="phone"]').value_of_css_property("color")
        return filled5_css
    
    def get6_cssfilled(self):
        filled6_css = self._driver.find_element(By.CSS_SELECTOR, '[id="city"]').value_of_css_property("color")   
        return filled6_css

    def get7_cssfilled(self):
        filled7_css = self._driver.find_element(By.CSS_SELECTOR, '[id="country"]').value_of_css_property("color")
        return filled7_css

    def get8_cssfilled(self):
        filled8_css = self._driver.find_element(By.CSS_SELECTOR, '[id="job-position"]').value_of_css_property("color")
        return filled8_css

    def get9_cssfilled(self):
        self.filled9_css = self._driver.find_element(By.CSS_SELECTOR, '[id="company"]').value_of_css_property("color")
        return self.filled9_css
    