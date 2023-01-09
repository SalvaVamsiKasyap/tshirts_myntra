from selenium.webdriver.common.by import By


class confirm:

    def __init__(self,driver):

        self.driver = driver

    country_input = (By.ID,"country")
    countires = (By.XPATH, "//div[@class='suggestions']//ul//li//a")
    terms_conditions = (By.XPATH, "//label[@for='checkbox2']//a")
    close = (By.XPATH, "//button[text()='Close']")
    purchase = (By.XPATH, "//input[@value='Purchase']")
    success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def country_inp(self):

        return self.driver.find_element(*confirm.country_input)

    def countriess(self):

        return self.driver.find_elements(*confirm.countires)

    def term_conditon(self):

        return self.driver.find_element(*confirm.terms_conditions)

    def pop_up(self):

        return self.driver.find_element(*confirm.close)

    def purch_ase(self):

        return self.driver.find_element(*confirm.purchase)

    def final_message(self):

        return self.driver.find_element(*confirm.success_message)
