import pytest
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait






class Testmyntrakid():

    def test_cheapest_kids_tshirt(self):

        service_obj = Service(r"C:\Users\Lenovo\PycharmProjects\SeleniumTest\Browsers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        # driver.get("https://rahulshettyacademy.com/angularpractice/")
        A = ActionChains(driver)
        driver.get("https://www.myntra.com/")
        driver.maximize_window()
        # user_title = driver.find_element(By.CLASS_NAME, 'desktop-userTitle')
        # A.move_to_element(user_title).perform()
        # login_button = driver.find_element(By.XPATH,"//a[@href='/login?referer=https://www.myntra.com/']")
        # A.move_to_element(login_button).click().perform()
        # input_number = driver.find_element(By.XPATH, '//input[@type="tel"]')
        # input_number.send_keys('7416416647')
        # input_number.send_keys(Keys.ENTER)
        # time.sleep(50)
        # input_number.send_keys(Keys.ENTER)
        # wait = WebDriverWait(driver,50)
        # wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='bottomeLink']/span")))
        # choose_password = driver.find_element(By.XPATH,"//div[@class='bottomeLink']/span")
        # choose_password.click()
        # enter_password = driver.find_element(By.XPATH,"//input[@type='password']")
        # enter_password.send_keys("Build@234")
        # enter_password.send_keys(Keys.ENTER)
        wait = WebDriverWait(driver, 50)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@data-reactid='334']/a")))
        hover_kid = driver.find_element(By.XPATH, "//div[@data-reactid='334']/a")
        A.move_to_element(hover_kid).perform()
        kid_categories = driver.find_elements(By.XPATH,'//div[@data-group="kids"]//a[@class="desktop-categoryName"]')
        for category in kid_categories:
            print(category.text)
        click_tshirt = driver.find_element(By.XPATH, "//li[@data-reactid='344']/a")
        A.move_to_element(click_tshirt).click().perform()
        driver.get(
            "https://www.myntra.com/kids?f=Categories%3ATshirts%3A%3AGender%3Aboys%2Cboys%20girls&sort=price_asc")
        product_links = driver.find_elements(By.XPATH, '//li[@class="product-base"]/a')

        counter = 0
        before_cart = []
        for item in product_links:

            item.click()
            Windows_opened = driver.window_handles
            #print(len(Windows_opened))
            driver.switch_to.window(Windows_opened[len(Windows_opened) - 1])
            #print(f"list of open windows second{Windows_opened}")
            #print(driver.current_url)
            # try:
            # self.verify_element_clickable("/div[@class ='size-buttons-size-buttons']/div/div/button")
            # except TimeoutException:
            # continue
            no_Stock = driver.find_elements(By.XPATH, "//div[text()='This product is currently sold out']")
            if len(no_Stock) > 0:
                driver.switch_to.window(Windows_opened[0])
            else:
                size = driver.find_element(By.XPATH,
                                           '//button[@class="size-buttons-size-button size-buttons-size-button-default size-buttons-big-size"]')
                A.move_to_element(size).click().perform()
                time.sleep(5)
                product_name = driver.find_element(By.XPATH, "//h1[@class='pdp-name']")
                before_cart.append(product_name.text)
                cart_adding = driver.find_element(By.XPATH,
                                                  '//span[@class="myntraweb-sprite pdp-whiteBag sprites-whiteBag pdp-flex pdp-center"]')
                A.move_to_element(cart_adding).click().perform()
                if counter != 4:
                    driver.switch_to.window(Windows_opened[0])
                #print(f" last url:{driver.current_url}")
                #print(f"list of open windows{Windows_opened}")
            counter += 1
            if counter == 5:
                break

        wait = WebDriverWait(driver, 50)
        wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, '//div[@class ="desktop-actions"]/a[@href="/checkout/cart"]')))
        driver.refresh()
        time.sleep(5)
        check_out_to_cart = driver.find_element(By.XPATH, "//a[@href='/checkout/cart']")
        A.move_to_element(check_out_to_cart).click().perform()
        # driver.find_element(By.XPATH,'//div[@class ="desktop-actions"]/a[@href="/checkout/cart"]').click()
        wait = WebDriverWait(driver, 50)
        wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//a[@class='itemContainer-base-itemLink']")))

        cart_items = driver.find_elements(By.XPATH, "//a[@class='itemContainer-base-itemLink']")

        for item, product in zip(cart_items, before_cart):
            assert item.text == product
            print(item.text)

        driver.close()


