#задание 2

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Page_calcul import PageCalcul


def test():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    pagecalcul = PageCalcul(driver)
    pagecalcul.clicker(45, '//*[@id="calculator"]//span[contains(text(), 8)]', '//*[@id="calculator"]//span[contains(text(), "+")]', '//*[@id="calculator"]//span[contains(text(), 7)]')
    pagecalcul.wait()
    assert pagecalcul.res() == "15" 

    driver.quit()
