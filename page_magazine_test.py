# тест для 3го задания
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Page_magazine_authorization import PageMagazine
from Page_magazine_main import MainPage
from Page_magazine_checkout import Checkout


def test():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    pagemagazine = PageMagazine(driver)
    pagemagazine.authorization()

    pagemain = MainPage(driver)
    pagemain.add_item()

    pagecheckout = Checkout(driver)
    pagecheckout.fill_checkout_information()
    pagecheckout.asserting()
   
    driver.quit()
