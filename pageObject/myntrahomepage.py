from selenium.webdriver.common.by import By


class myntrahomepage:

    def __init__(self, driver):
        self.driver = driver

    profil = (By.CLASS_NAME, 'desktop-userTitle')

    login_button = (By.XPATH, "//a[@href='/login?referer=https://www.myntra.com/']")

    def profile_login(self):
        return self.driver.find_element(*myntrahomepage.profil)

    def login_b(self):
        return self.driver.find_element(*myntrahomepage.login_button)
