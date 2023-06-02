# тест для 1го задания
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Page_for_autofill import PageAutofil


def test():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    PageForAutofill = PageAutofil(driver)
   
    PageForAutofill.autofill("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
    PageForAutofill.click_on_button()
    
    green_css = 'rgba(15, 81, 50, 1)'
    assert PageForAutofill.unfilledcss() == 'rgba(132, 32, 41, 1)'
    assert PageForAutofill.get1_cssfilled() == green_css
    assert PageForAutofill.get2_cssfilled() == green_css
    assert PageForAutofill.get3_cssfilled() == green_css
    assert PageForAutofill.get4_cssfilled() == green_css
    assert PageForAutofill.get5_cssfilled() == green_css
    assert PageForAutofill.get6_cssfilled() == green_css
    assert PageForAutofill.get7_cssfilled() == green_css
    assert PageForAutofill.get8_cssfilled() == green_css
    assert PageForAutofill.get9_cssfilled() == green_css
    
    driver.quit()

            