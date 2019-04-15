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

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(3)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        
        #search for hashtag link
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print(hashtag + " photos: " + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_link_text("Vind ik leuk").click()
                time.sleep(18)
            except Exception as e:
                time.sleep(2)


rensIG = instagramBot("theworldofnirvana", "qWeQSWTL")
rensIG.login()
rensIG.like_photo('kurtcobain')

#hashtags = ['kurtcobain', 'nirvana']
#[rensIG.like_photo(tag) for tag in hashtags]

# "/accounts/login/?source=auth_switcher"