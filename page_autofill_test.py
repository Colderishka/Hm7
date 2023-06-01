# тест для 1го задания
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Page_for_autofill import PageAutofil


def test():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    PageForAutofill = PageAutofil(driver)
    PageForAutofill.autofill()
    PageForAutofill.click_on_button()
    PageForAutofill.compare()

    driver.quit()
