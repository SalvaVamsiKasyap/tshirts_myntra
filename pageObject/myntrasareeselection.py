import time

from selenium.webdriver.common.by import By


class myntrasareeselection:

    def __init__(self,driver):

        self.driver = driver

    click_on_item = (By.XPATH,'//a[@href="sarees/united-liberty/united-liberty-teal-blue--golden-zari-art-silk'
                              '-banarasi-saree/17703594/buy"]')
    add_to_cart = (By.XPATH,'//span[@class="myntraweb-sprite pdp-whiteBag sprites-whiteBag pdp-flex pdp-center"]')

    added_to_cart=(By.XPATH,"//a[@href='/checkout/cart']/span[text()='GO TO BAG']")

    def clickonitem(self):

        self.driver.find_element(*myntrasareeselection.click_on_item).click()

    def addtocart(self):
        Windows_opened = self.driver.window_handles
        self.driver.switch_to.window(Windows_opened[1])
        get_title = self.driver.title
        print(get_title)
        #time.sleep(25)
        self.driver.find_element(*myntrasareeselection.add_to_cart).click()
        time.sleep(5)
        return self.driver.find_element(*myntrasareeselection.added_to_cart).click()

