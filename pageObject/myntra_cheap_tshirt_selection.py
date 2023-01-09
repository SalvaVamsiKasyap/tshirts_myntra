from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.keys import Keys



class myntra_cheap_tshirt_selection(BaseClass):

    def __init__(self,driver):

        self.driver = driver
        self.A = ActionChains(self.driver)

    sort_option = (By.XPATH,'//div[@class="horizontal-filters-sortContainer"]/div/div')
    select_low_to_up = (By.XPATH,"input[@value='price_asc']")

    def moving_to_sort_option(self):

        sort_op_tion=self.driver.find_element(*myntra_cheap_tshirt_selection.sort_option)
        time.sleep(5)
        recom = self.A.move_to_element(sort_op_tion).click().perform()
        time.sleep(10)
        self.driver.get("https://www.myntra.com/kids?f=Categories%3ATshirts%3A%3AGender%3Aboys%2Cboys%20girls&sort=price_asc")
        time.sleep(10)
