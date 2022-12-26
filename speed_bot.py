from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):

        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.driver.maximize_window()
        time.sleep(2)
        self.up = 0
        self.down = 0

    def get_internet_speed(self, url):
        self.driver.get(url)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(60)
        while True:
            try:
                down_speed_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
                down_speed = self.driver.find_element(By.XPATH, down_speed_xpath).get_attribute("textContent")
                self.down = float(down_speed)

                up_speed_xpath = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
                up_speed = self.driver.find_element(By.XPATH, up_speed_xpath).get_attribute("textContent")
                self.up = float(up_speed)
            except Exception as e:
                print(e)
                time.sleep(2)
            else:
                break

        print(f'Down Speed: {self.down}')
        print(f'Up Speed: {self.up}')

    def tweet_at_provider(self):
        pass

