from selenium.webdriver.common.by import By

from pageObject.checkOut import checkOut


class Homepage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.XPATH, "//a[@href='/angularpractice/shop']")

    def shopItems(self):
        self.driver.find_element(*Homepage.shop).click()
        return checkOut(self.driver)
        # driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']")
        # star is placed to deserialize star and to convert to above format basically to treat the shop variable as tuple
        # Need to use * if you have web elements defined in variables and want to call them in to classes
