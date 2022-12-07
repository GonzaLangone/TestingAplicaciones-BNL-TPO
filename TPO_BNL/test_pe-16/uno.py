# test correcto, con todos los datos correctamen
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



class TestNuevo():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_nuevo(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(647, 620)
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        self.driver.find_element(By.LINK_TEXT, "Register here").click()
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("josemaria@hotmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "form").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("Holacomo_estas123")
        self.driver.find_element(By.ID, "cpassword").click()
        self.driver.find_element(By.ID, "cpassword").send_keys("Holacomo_estas123")
        self.driver.find_element(By.NAME, "firstName").click()
        self.driver.find_element(By.NAME, "firstName").send_keys("Jose Maria")
        self.driver.find_element(By.NAME, "lastName").send_keys("Listorti")
        self.driver.find_element(By.NAME, "address1").send_keys("spiro  21312")
        self.driver.find_element(By.NAME, "zipcode").click()
        self.driver.find_element(By.NAME, "zipcode").send_keys("96749")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("Hawaiii")
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("Estados Unidos")
        self.driver.find_element(By.NAME, "country").click()
        self.driver.find_element(By.NAME, "country").send_keys("Hawaii city")
        self.driver.find_element(By.NAME, "phone").click()
        self.driver.find_element(By.NAME, "phone").send_keys("+1 2014222748")
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(13) > input").click()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()

        
        assert self.driver.current_url != "http://127.0.0.1:5000/register", 'Si levanta error funciona mal el sistema '


# python -m pytest uno.py  