from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from speed_bot import InternetSpeedTwitterBot
from twitter_bot import TwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/miyamarinova/Development/chrome-driver.exe"
TWITTER_URL = "https://twitter.com/home"
TWITTER_EMAIL = "miyamarinova@gmail.com"
USERNAME = 'miyamarinova'
TWITTER_PASSWORD = "pa6murdagi"
SPEED_URL = "https://www.speedtest.net/"

#bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
#bot.get_internet_speed(SPEED_URL)
#bot.tweet_at_provider()

t_bot = TwitterBot(CHROME_DRIVER_PATH)
t_bot.log_in(TWITTER_URL, TWITTER_EMAIL, TWITTER_PASSWORD, USERNAME)
time.sleep(2)
