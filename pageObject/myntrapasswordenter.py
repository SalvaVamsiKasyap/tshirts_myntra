from selenium.webdriver.common.by import By


class myntrapasswordenter:

    def __init__(self,driver):

        self.driver=driver

    enter_password=(By.XPATH,"//input[@type='password']")

    def enterpassword(self):

        return self.driver.find_element(*myntrapasswordenter.enter_password)