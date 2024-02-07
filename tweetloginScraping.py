import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import configparser
from constants.constants import website_url, sleep_time

# Get information from config.ini file
config = configparser.ConfigParser()
config.read("config.ini")
username = config.get("credentials", "username")
password = config.get("credentials", "password")

# Create a test class
class TestTwitter(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # Select chrome browser and start your webdriver (maximized)
        cls.options = webdriver.ChromeOptions()
        cls.options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(cls.options)

    # Create test function
    def test_login(self):
        # Go to url adress
        self.driver.get(website_url)
        time.sleep(sleep_time)

        # Find the username input field (Name locator strategy used)
        name_input = self.driver.find_element(By.NAME, "text")
        # Enter your username and press enter
        name_input.send_keys(username, Keys.ENTER)
        time.sleep(sleep_time)

        # Find the password entry field (Name locator strategy)
        pass_input = self.driver.find_element(By.NAME, "password")
        # Enter your password and press enter
        pass_input.send_keys(password, Keys.ENTER)
        time.sleep(sleep_time)

    # After the test is over
    @classmethod
    def tearDown(cls):
        # Close the browser
        cls.driver.quit()

