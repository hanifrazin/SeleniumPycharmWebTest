import unittest

import warnings

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        sv = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=sv)

    def test_success_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, "/html//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "/html//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "/html//input[@id='login-button']").click()
        data = driver.find_element(By.XPATH, "/html//div[@id='header_container']//div[@class='app_logo']").text
        self.assertIn("Swag Labs", data)
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/inventory.html")

    def test_failed_login(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, "/html//input[@id='user-name']").send_keys("locked_out_user")
        driver.find_element(By.XPATH, "/html//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "/html//input[@id='login-button']").click()
        data = driver.find_element(By.XPATH, "//div[@id='login_button_container']//form//h3").text
        self.assertIn("Epic sadface: Sorry, this user has been locked out.", data)

    def tearDown(self):
        self.browser.close()
