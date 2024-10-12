from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Edge()

driver.get("https://www.desmos.com/scientific#:~:text=A%20beautiful,%20free%20online%20scientific%20calculator")

def input_expression(expression):
    character = 0
    for char in expression:
        if char.isdigit():
            driver.find_element(By.XPATH, f"//span[@aria-label='{char}']").click()
        elif char == '+':
            if(character != 0):
                driver.find_element(By.XPATH, "//span[@aria-label='Right Parenthesis']").click()
                character -= 1
            driver.find_element(By.XPATH, "//span[@aria-label='Plus']").click()
        elif char == '-':
            if(character != 0):
                driver.find_element(By.XPATH, "//span[@aria-label='Right Parenthesis']").click()
                character -= 1
            driver.find_element(By.XPATH, "//span[@aria-label='Minus']").click()
        elif char == '*':
            if(character != 0):
                driver.find_element(By.XPATH, "//span[@aria-label='Right Parenthesis']").click()
                character -= 1
            driver.find_element(By.XPATH, "//span[@aria-label='Times']").click()
        elif char == '/':
            if(character != 0):
                driver.find_element(By.XPATH, "//span[@aria-label='Right Parenthesis']").click()
                character -= 1
            driver.find_element(By.XPATH, "//span[@aria-label='Divide']").click()
        elif char == '=':
            driver.find_element(By.XPATH, "//span[@aria-label='Enter']").click()
        elif char == '^':
            driver.find_element(By.XPATH, "//span[@aria-label='Superscript']").click()
        elif char == '.':
            driver.find_element(By.XPATH, "//span[@aria-label='Decimal']").click()
        elif char == 's':
            character +=1
            driver.find_element(By.XPATH, "//span[@aria-label='Sine']").click()
        elif char == 'c':
            character +=1
            driver.find_element(By.XPATH, "//span[@aria-label='Cosine']").click()
        elif char == 't':
            character +=1
            driver.find_element(By.XPATH, "//span[@aria-label='Tangent']").click()
        elif char == 'l':
            character +=1
            driver.find_element(By.XPATH, "//div[@aria-label='Functions']").click()
            driver.find_element(By.XPATH, "//span[@aria-label='Log']").click()
            driver.find_element(By.XPATH, "//div[@aria-label='main']").click()
        elif char == 'n':
            character +=1
            driver.find_element(By.XPATH, "//div[@aria-label='Functions']").click()
            driver.find_element(By.XPATH, "//span[@aria-label='Natural Log']").click()
            driver.find_element(By.XPATH, "//div[@aria-label='main']").click()
        elif char == 'r':
            driver.find_element(By.XPATH, "//span[@aria-label='Square Root']").click()
        elif char == 'p':
            driver.find_element(By.XPATH, "//span[@aria-label='Pi']").click()
        elif char == '(':
            driver.find_element(By.XPATH, "//span[@aria-label='Left Parenthesis']").click()
        elif char == ')':
            driver.find_element(By.XPATH, "//span[@aria-label='Right Parenthesis']").click()
            element = driver.find_element(By.XPATH, "//span[@aria-hidden='true']")
            driver.execute_script("arguments[0].click();", element)
            
        time.sleep(1)
    
        
    # equals_button = driver.find_element(By.XPATH, "//span[@aria-label='Enter']")
    # equals_button.click()

    time.sleep(0.75)
    btn = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/div[1]/div/div[7]')
    btn.click()

def test_units_operations():
    input_expression("1+9=")

def test_tens_operations():
    input_expression("11-87=")

def test_hundreds_operations():
    input_expression("100*278=")

def test_thousands_operations():
    input_expression("1500/8000=")

def sanity_testing():
    sanity_values = [
        "1+2=", "1-2=", "1*2=", "1/2=", "r81="
    ]
    
    for value in sanity_values:
        input_expression(value)

def equivalent_partitioning():
    test_units_operations()
    test_tens_operations()
    test_hundreds_operations()
    test_thousands_operations()

def monkey():
    invalid_test_cases = [
        "1--=",     
        "1/0=",     
        "++++=",    
        "*/2=",     
        "2**2=",    
        "(2+2))=",  
        "((2+2)=",  
        "2+/2=",    
        "0/0=",     
        "(1+2)*=",  
        "1.2.3+2=", 
        "1^^2=",    
        "2/=",      
        "l(0)=",  
        "s(90)+=",
        "r(-1)=",
        "999999999999999999+1=", 
        "2//2=",    
        "pp+2=",    
    ]
    
    for case in invalid_test_cases:
        print(f"Testing expression: {case}")
        input_expression(case)

def gorilla():
    loop_numbers = [5 for _ in range(50)]
    
    expression = "*".join(map(str, loop_numbers)) + "="
    
    input_expression(expression)

def boundary_value_testing():
    input_expression("9999999999999999999 - -9999999999999999999*9999999999999999999=") 

def breadth_testing():
    breadth_values = [
        "s30+c30=", "c60+60=", "t45+l100=", "l100*2^5=", "2^10+(2*3)=", "r16*r25=", "p*2+8=",
    ]
    
    for value in breadth_values:
        input_expression(value)
    
def depth_testing():
    input_expression("((1000000 + 1) * l1000) - (tp + s30 - c60))/ (n2 + r9^1.5)=")    

def allpairs():
    test_cases = [
    "1+10=", "2-15=", "3*20=", "4/30=", "5+40=", "6-50=", "7*60=", "8/70=", "9+80=",
    "1-99=", "2*25=", "3/35=", "4+45=", "5-55=", "6*65=", "7/75=", "8+85=", "9-95=",
    "1*12=", "2/22="
    ]
    
    for case in test_cases:
        input_expression(case)

#integration testing
# sanity_testing()
# boundary_value_testing()
breadth_testing()
# equivalent_partitioning()

# depth_testing()
# allpairs()
# monkey()
# gorilla()