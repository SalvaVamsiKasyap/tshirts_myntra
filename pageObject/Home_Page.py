from selenium.webdriver.common.by import By


class Home_Page:

    def __init__(self,driver):

        self.driver = driver

    Email1 = (By.NAME,"email")
    Password1 = (By.ID,"exampleInputPassword1")
    Clickable1 = (By.ID, "exampleCheck1")
    Radio1 = (By.CSS_SELECTOR, "#inlineRadio1")
    Name1 = (By.CSS_SELECTOR, "input[name='name']")
    Click_11 = (By.XPATH, "//input[@type='submit']")
    Gender_select1 = (By.ID, "exampleFormControlSelect1")
    Success_Message1 = (By.CLASS_NAME, "alert-success")

    def Email(self):

        return self.driver.find_element(*Home_Page.Email1)

    def Password(self):

        return self.driver.find_element(*Home_Page.Password1)

    def Clickable(self):
        return self.driver.find_element(*Home_Page.Clickable1)

    def Radio(self):
        return self.driver.find_element(*Home_Page.Radio1)

    def Name(self):
        return self.driver.find_element(*Home_Page.Name1)

    def Click_1(self):
        return self.driver.find_element(*Home_Page.Click_11)

    def Gender_Select(self):
        return self.driver.find_element(*Home_Page.Gender_select1)

    def Success_Message(self):
        return self.driver.find_element(*Home_Page.Success_Message1)