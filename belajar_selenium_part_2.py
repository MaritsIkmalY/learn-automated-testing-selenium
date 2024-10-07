from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://www.desmos.com/scientific#:~:text=A%20beautiful,%20free%20online%20scientific%20calculator")

def input_expression(expression):
    for char in expression:
        if char.isdigit():
            button = driver.find_element(By.XPATH, f"//span[@aria-label='{char}']")
        elif char == '+':
            button = driver.find_element(By.XPATH, "//span[@aria-label='Plus']")
        elif char == '-':
            button = driver.find_element(By.XPATH, "//span[@aria-label='Minus']")
        elif char == '*':
            button = driver.find_element(By.XPATH, "//span[@aria-label='Times']")
        elif char == '/':
            button = driver.find_element(By.XPATH, "//span[@aria-label='Divide']")
        elif char == '=':
            button = driver.find_element(By.XPATH, "//span[@aria-label='Enter']")
        elif char == '^':
            button = driver.find_element(By.XPATH, "//span[@aria-label='Superscript']")
        button.click()
        time.sleep(0.5)

    # equals_button = driver.find_element(By.XPATH, "//span[@aria-label='Enter']")
    # equals_button.click()

    time.sleep(0.5)
    btn = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/div[1]/div/div[7]')
    btn.click()
    time.sleep(0.5)

# Test case for units (satuan) operations
def test_units_operations():
    print("Testing unit operations")
    input_expression("1+1="),
    input_expression("8-7="),

# Test case for tens (puluhan)
def test_tens_operations():
    print("Testing tens operations")
    input_expression("16+89="),
    input_expression("27*5="),

# Test case for hundreds (ratusan)
def test_hundreds_operations():
    print("Testing hundreds operations")
    input_expression("125+478="),
    input_expression("200-150="),

# Test case for thousands (ribuan)
def test_thousands_operations():
    print("Testing thousands operations")
    input_expression("1250+4750="),
    input_expression("7000-2000="),

# Test case for ten thousands (puluh ribuan)
def test_ten_thousands_operations():
    print("Testing ten thousands operations")
    input_expression("12345+67890="),
    input_expression("50000-20000="),

# Test case for hundred thousands (ratus ribuan)
def test_hundred_thousands_operations():
    print("Testing hundred thousands operations")
    input_expression("123456+654321="),
    input_expression("700000-300000="),



def equivalent_partitioning():
    test_units_operations()
    test_tens_operations()
    test_hundreds_operations()
    test_thousands_operations()
    test_ten_thousands_operations()
    test_hundred_thousands_operations()

def monkey():
    input_expression("1--=")
    input_expression("1/0=")

def gorilla():
    for i in range(100):
        driver.find_element(By.XPATH,"//span[@aria-label='1']").click()

equivalent_partitioning()
monkey()
gorilla()


