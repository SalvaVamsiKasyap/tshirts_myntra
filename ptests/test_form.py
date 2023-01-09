from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObject.Home_Page import Home_Page
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        # service_obj = Service(r"C:\Users\Lenovo\PycharmProjects\SeleniumTest\Browsers\chromedriver.exe")
        # driver: WebDriver = webdriver.Chrome(service=service_obj)
        log = self.get_logger()
        # driver.get("https://rahulshettyacademy.com/angularpractice/")
        home_page = Home_Page(self.driver)
        # self.driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        home_page.Email().send_keys(getData["Email"])
        # self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
        home_page.Password().send_keys(getData["Password"])
        # self.driver.find_element(By.ID, "exampleCheck1").click()
        home_page.Clickable().click()
        # self.driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
        home_page.Radio().click()
        # self.driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Vamsi_Kasyap")
        home_page.Name().send_keys(getData["Name"])

        # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        home_page.Click_1().click()

        # static drop down
        # drop = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        self.select_option_by_text(home_page.Gender_Select(), getData["Gender"],getData["index"])
        drop = Select(home_page.Gender_Select())
        # drop.select_by_visible_text("Female")
        sleep(5)
        # drop.select_by_index(0)
        # dropdown.select_by_value()

        # driver.find_element_by_xpath("//input[@type='submit']").click()
        # message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        message = home_page.Success_Message().text
        log.info(message)
        assert "Success" in message
        self.driver.refresh()

        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello again")
        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
        log.info("-----------------------TEST CASE ENDED--------------------------")

    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param

