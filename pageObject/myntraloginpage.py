import time
from time import sleep

from selenium.webdriver.common.by import By


class myntraloginpage:

    def __init__(self, driver):
        self.driver = driver

    number_enter = (By.XPATH, '//input[@type="tel"]')

    continued = (By.XPATH,"//div[@class='submitBottomOption']")

    def enter_number(self):
        return self.driver.find_element(*myntraloginpage.number_enter)

    def con_tinue(self):
        time.sleep(10)
        return self.driver.find_element(*myntraloginpage.continued).click()
