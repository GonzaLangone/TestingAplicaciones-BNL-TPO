# Generated by Selenium IDE

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

def test_dos():
    # Test, deja ingresar cuando cargamos datos de otros paises, Error su validacion!
    pass
        
def test_uno():
    # test correct 
    pass
  
def test_cuatro():
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
        self.driver.find_element(By.NAME, "email").send_keys("gonzalo@hotmail.com")
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(13) > input").click()
  



      
def main():
    while True:
        print('1. Test 01 datos correctos!')
        print('2. Test 02 carga datos incorrectos')
        print('2. Test 03 carga edad menor')
        print('2. Test 04 carga mail sin dominio')
        print('0. Exit')
        opc = input('Ingrese la opcion: ')
        if opc == '0':
            break
        elif opc == '1':
            test_uno()
        elif opc == '2':
            test_dos()
        elif opc == '3':
            print('No hay campo para la edad!.')
            break
        elif opc == '4':
            test_cuatro()
        