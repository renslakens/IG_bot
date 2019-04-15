from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class instagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        login_button = driver.find_element_by_xpath("//*[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(5)

        username_element = driver.find_element_by_xpath("//input[@name='username']")
        username_element.clear()
        username_element.send_keys(self.username)

        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)

        not_now_app_element = driver.find_element_by_xpath("//*[@href='/']")
        not_now_app_element.click()
        time.sleep(3)

        not_now_message_element = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
        not_now_message_element.click()
        time.sleep(3)


rensIG = instagramBot("theworldofnirvana", "qWeQSWTL")
rensIG.login()

# "/accounts/login/?source=auth_switcher"