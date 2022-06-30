from secret import Secret
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time


secret = Secret()


INSTAGRAM_URL = 'https://www.instagram.com/'
INSTA_ID = secret.insta_id
INSTA_PASS = secret.insta_pass

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(INSTA_ID)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(INSTA_PASS)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(Keys.ENTER)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]').click()
    
    def find_followers(self):
        search = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys('League of Legends')
        time.sleep(3)
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div/span').click()
        time.sleep(10)
        modal = self.driver.find_element(By.CSS_SELECTOR, '.isgrP')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        follow_btn = self.driver.find_elements(By.CSS_SELECTOR, ".isgrP button")
        for button in follow_btn:
            try:
                button.click()
                time.sleep(1)
            except selenium.common.exceptions.ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel.click()
                continue
            except selenium.common.exceptions.NoSuchElementException:
                continue
            

