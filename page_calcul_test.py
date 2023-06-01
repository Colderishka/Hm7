#задание 2

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Page_calcul import PageCalcul


def test():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    pagecalcul = PageCalcul(driver)
    pagecalcul.clicker()
    pagecalcul.wait_and_assert()

    driver.quit()
