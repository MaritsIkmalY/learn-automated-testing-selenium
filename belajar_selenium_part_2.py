from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://www.desmos.com/scientific#:~:text=A%20beautiful,%20free%20online%20scientific%20calculator")

def input_expression(expression):
    print(expression)
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
        time.sleep(2)

    # Press "=" to get the result
    equals_button = driver.find_element(By.XPATH, "//span[@aria-label='Enter']")
    equals_button.click()
    time.sleep(2)

    # Verify the result is displayed
    math_field = driver.find_element(By.XPATH, "//*[@id='main']/div/div/div/div[1]/div[2]/div/div[2]/div/div/span[3]")
    entered_value = math_field.text
    print(entered_value)
    time.sleep(2)
    btn = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/div[1]/div/div[7]')
    btn.click()
    time.sleep(2)
    return entered_value

# Test case for units (satuan) operations
def test_units_operations():
    print("Testing unit operations")
    # input_expression("1+1=")
    assert "2" in input_expression("1+1="), "Expected 2"
    # input_expression("8-7=")
    assert "1" in input_expression("8-7="), "Expected 1"

# Test case for tens (puluhan)
def test_tens_operations():
    print("Testing tens operations")
    # input_expression("16+89=")
    assert "105" in input_expression("16+89="), "Expected 105"
    # input_expression("27*5=")
    assert "135" in input_expression("27*5="), "Expected 135"

# Test case for hundreds (ratusan)
def test_hundreds_operations():
    print("Testing hundreds operations")
    # input_expression("125+478=")
    assert "603" in input_expression("125+478="), "Expected 603"
    # input_expression("200-150=")
    assert "50" in input_expression("200-150="), "Expected 50"

# Test case for thousands (ribuan)
def test_thousands_operations():
    print("Testing thousands operations")
    # input_expression("1250+4750=")
    assert "6000" in input_expression("1250+4750="), "Expected 6000"
    # input_expression("7000-2000=")
    assert "5000" in input_expression("7000-2000="), "Expected 5000"

# Test case for ten thousands (puluh ribuan)
def test_ten_thousands_operations():
    print("Testing ten thousands operations")
    # input_expression("12345+67890=")
    assert "80235" in input_expression("12345+67890="), "Expected 80235"
    # input_expression("50000-20000=")
    assert "30000" in input_expression("50000-20000="), "Expected 30000"

# Test case for hundred thousands (ratus ribuan)
def test_hundred_thousands_operations():
    print("Testing hundred thousands operations")
    # input_expression("123456+654321=")
    assert "777777" in input_expression("123456+654321="), "Expected 777777"
    # input_expression("700000-300000=")
    assert "400000" in input_expression("700000-300000="), "Expected 400000"

# Run all test cases
# test_units_operations()
# test_tens_operations()
# test_hundreds_operations()
# test_thousands_operations()
# test_ten_thousands_operations()
# test_hundred_thousands_operations()
assert "8" in input_expression("2^3=")


