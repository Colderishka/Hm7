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
    pagemagazine.authorization("standard_user", "secret_sauce")

    pagemain = MainPage(driver)
    pagemain.add_item('#add-to-cart-sauce-labs-backpack', '#add-to-cart-sauce-labs-bolt-t-shirt', '#add-to-cart-sauce-labs-onesie')

    pagecheckout = Checkout(driver)
    pagecheckout.fill_checkout_information("Павел", "Петров", "13000")
    pagecheckout.res()
    assert pagecheckout.res() == "Total: $58.29"
    driver.quit()
  
