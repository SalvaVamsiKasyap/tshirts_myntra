from selenium.webdriver.common.by import By

from pageObject.confirm import confirm


class checkOut:

    def __init__(self,driver):

        self.driver = driver

    models = (By.XPATH,"//h4/a")
    Add_to_cart = (By.XPATH,"//button[@class='btn btn-info']")
    check_out = (By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']")
    But = (By.CSS_SELECTOR,"button[class='btn btn-success']")

    def title(self):

        return self.driver.find_elements(*checkOut.models)#, self.driver.find_elements(*checkOut.Add_to_cart), self.driver.find_element(checkOut.check_out)


    def cart(self):

        return self.driver.find_elements(*checkOut.Add_to_cart)

    def Click(self):

        return self.driver.find_element(*checkOut.check_out)

    def Button(self):

        self.driver.find_element(*checkOut.But).click()
        return confirm(self.driver)


