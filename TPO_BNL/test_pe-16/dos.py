# probando con datos incorrectos (de otros paises)

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

class TestPrueba():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
      
    def teardown_method(self, method):
        self.driver.quit()
      
    def test_prueba(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(647, 620)
        self.driver.find_element(By.LINK_TEXT, "Sign In").click()
        self.driver.find_element(By.LINK_TEXT, "Register here").click()
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("gojav1234@hotmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "form").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("juancarlos")
        self.driver.find_element(By.CSS_SELECTOR, "form").click()
        self.driver.find_element(By.ID, "cpassword").click()
        self.driver.find_element(By.ID, "cpassword").send_keys("juancarlos")
        self.driver.find_element(By.NAME, "firstName").click()
        self.driver.find_element(By.NAME, "firstName").send_keys("carlos")
        self.driver.find_element(By.NAME, "lastName").send_keys("juan")
        self.driver.find_element(By.NAME, "address1").send_keys("spiro 1233")
        self.driver.find_element(By.NAME, "zipcode").send_keys("7167")
        self.driver.find_element(By.NAME, "city").send_keys("pinamar")
        self.driver.find_element(By.NAME, "state").send_keys("valeria")
        self.driver.find_element(By.NAME, "country").send_keys("valeria del mar")
        self.driver.find_element(By.NAME, "phone").send_keys("2254530025")
        self.driver.find_element(By.CSS_SELECTOR, "form").click()
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(13) > input").click()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()

        assert self.driver.current_url == "http://127.0.0.1:5000/register", 'Datos incorrectos tienen que ser de EEUU  '
        