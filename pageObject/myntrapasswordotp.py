from selenium.webdriver.common.by import By


class myntrapasswordotp:

    def __init__(self,driver):

        self.driver=driver

    choose_password = (By.XPATH,"//div[@class='bottomeLink']/span")

    def password_option(self):

        return self.driver.find_element(*myntrapasswordotp.choose_password).click()