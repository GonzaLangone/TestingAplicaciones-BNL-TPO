# cargar mal el mail

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestcuatro():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_testcuatro(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1936, 1048)
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        self.driver.find_element(By.LINK_TEXT, "Register here").click()
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("gonzalo")
        self.driver.find_element(By.ID, "password").send_keys("gonzalo123")
        self.driver.find_element(By.ID, "cpassword").send_keys("gonzalo123")
        self.driver.find_element(By.NAME, "firstName").send_keys("gonzalo")
        self.driver.find_element(By.NAME, "lastName").send_keys("sanchez")
        self.driver.find_element(By.NAME, "address1").send_keys("spiro")
        self.driver.find_element(By.NAME, "zipcode").send_keys("02154")
        self.driver.find_element(By.NAME, "city").send_keys("estados unidos")
        self.driver.find_element(By.NAME, "state").send_keys("new york")
        self.driver.find_element(By.NAME, "country").send_keys("newyorkcity")
        self.driver.find_element(By.NAME, "phone").send_keys("02154689")
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(13) > input").click()
        
        assert self.driver.current_url == "http://127.0.0.1:5000/registerationForm", 'Si levanta error es que toma el mail sin dominio'

        self.driver.find_element(By.NAME, "email").send_keys("gonzalo@hotmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(13) > input").click()
        time.sleep(3)

        assert self.driver.current_url == "http://127.0.0.1:5000/register", 'Si levanta error funciona mal el sistema'
