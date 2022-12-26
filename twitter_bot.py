from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.driver.maximize_window()
        time.sleep(2)

    def log_in(self, url, email, pasword, username):
        self.driver.get(url)
        sign = self.driver.find_element(By.XPATH, '//input[@autocomplete="username"]')
        sign.send_keys(email)
        sign.send_keys(Keys.ENTER)
        time.sleep(3)
        enter_username = self.driver.find_element(By.XPATH, "//input[@name='text']")
        enter_username.send_keys(username)
        enter_username.send_keys(Keys.ENTER)
        password = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        password.send_keys(pasword)
        time.sleep(10)
        password.send_keys(Keys.ENTER)

        self.tweet = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
        self.tweet.send_keys(
            f'Hey')
        self.button = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]').click()
        time.sleep(10)

