from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://www.desmos.com/scientific#:~:text=A%20beautiful,%20free%20online%20scientific%20calculator")

def input_expression(expression):
    for char in expression:
        if char.isdigit():
            driver.find_element(By.XPATH, f"//span[@aria-label='{char}']").click()
        elif char == '+':
            driver.find_element(By.XPATH, "//span[@aria-label='Plus']").click()
        elif char == '-':
            driver.find_element(By.XPATH, "//span[@aria-label='Minus']").click()
        elif char == '*':
            driver.find_element(By.XPATH, "//span[@aria-label='Times']").click()
        elif char == '/':
            driver.find_element(By.XPATH, "//span[@aria-label='Divide']").click()
        elif char == '=':
            driver.find_element(By.XPATH, "//span[@aria-label='Enter']").click()
        elif char == '^':
            driver.find_element(By.XPATH, "//span[@aria-label='Superscript']").click()
        elif char == '.':
            driver.find_element(By.XPATH, "//span[@aria-label='Decimal']").click()
        elif char == 's':
            driver.find_element(By.XPATH, "//span[@aria-label='Sine']").click()
        elif char == 'c':
            driver.find_element(By.XPATH, "//span[@aria-label='Cosine']").click()
        elif char == 't':
            driver.find_element(By.XPATH, "//span[@aria-label='Tangent']").click()
        elif char == 'l':
            driver.find_element(By.XPATH, "//div[@aria-label='Functions']").click()
            driver.find_element(By.XPATH, "//span[@aria-label='Log']").click()
            driver.find_element(By.XPATH, "//div[@aria-label='main']").click()
        elif char == 'n':
            driver.find_element(By.XPATH, "//div[@aria-label='Functions']").click()
            driver.find_element(By.XPATH, "//span[@aria-label='Natural Log']").click()
            driver.find_element(By.XPATH, "//div[@aria-label='main']").click()
        elif char == 'r':
            driver.find_element(By.XPATH, "//span[@aria-label='Square Root']").click()
        elif char == 'p':
            driver.find_element(By.XPATH, "//span[@aria-label='Pi']").click()
        
        time.sleep(0.1)
        
    equals_button = driver.find_element(By.XPATH, "//span[@aria-label='Enter']")
    equals_button.click()

    time.sleep(0.5)
    btn = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/div[1]/div/div[7]')
    btn.click()
    time.sleep(0.5)

def test_units_operations():
    print("Testing unit operations")
    input_expression("1+1="),
    input_expression("8-7="),

def test_tens_operations():
    print("Testing tens operations")
    input_expression("16+89="),
    input_expression("27*5="),

def test_hundreds_operations():
    print("Testing hundreds operations")
    input_expression("125+478="),
    input_expression("200-150="),

def test_thousands_operations():
    print("Testing thousands operations")
    input_expression("1250+4750="),
    input_expression("7000-2000="),

def test_ten_thousands_operations():
    print("Testing ten thousands operations")
    input_expression("12345+67890="),
    input_expression("50000-20000="),

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

def boundary_value_testing():
    print("Boundary Value Testing")

    input_expression("999999999+1=") 
    input_expression("1000000000-1=")  

    input_expression("0.0000001+1=")  
    input_expression("0.00000001-0.0000001=")  

    input_expression("-999999999-1=") 
    input_expression("-1000000000+1=") 

def breadth_testing():
    print("Breadth Testing")

    input_expression("s30=") 
    input_expression("c60=") 
    input_expression("t45=") 

    input_expression("l100=") 
    input_expression("n2=")  
    input_expression("2^10=") 

    input_expression("r16=")  
    input_expression("p*2=")  

def depth_testing():
    print("Depth Testing")

    angles = [0, 30, 45, 60, 90, 180, 270, 360]
    for angle in angles:
        input_expression(f"s{angle}=")
        input_expression(f"c{angle}=")
        input_expression(f"t{angle}=")

    values = [1, 10, 100, 1000]
    for value in values:
        input_expression(f"l{value}=") 
        input_expression(f"n{value}=")   

    bases = [2, 10, 3]
    exponents = [0, 1, 2, 3, 10, -1]
    for base in bases:
        for exponent in exponents:
            input_expression(f"{base}^{exponent}=")

    input_expression("1000000 + 1=")  
    input_expression("999999999/3=")  
    input_expression("0.0000001 * 10000000=")  

def allpairs():
    input_expression("1+100=")
    input_expression("2-200=")
    input_expression("3*300=")
    input_expression("4/400=")
    input_expression("5+500=")
    input_expression("6-600=")
    input_expression("7*700=")
    input_expression("8/800=")
    input_expression("9+900=")

# equivalent_partitioning()
# monkey()
# gorilla()
# boundary_value_testing()
# breadth_testing()
depth_testing()
# allpairs()

