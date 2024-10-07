from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://nikomood.com/")

def submit_login_form():
    submit = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/form/div[3]/button[1]')
    submit.click()
    time.sleep(2)  

def fill_form(email, password):
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)

#case 1 (Happy Flow Login)
def happy_flow_login(email, password):
    fill_form(email, password)
    submit_login_form()
    time.sleep(2)

#case 2 (Negative Flow Login)
def negative_flow_login(email, password):
    fill_form(email, password) 
    submit_login_form()
    time.sleep(2)

def go_to_login_page():
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(2)

def logout():
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[1]/div[3]').click()
    driver.find_element(By.XPATH, '//*[@id="radix-:r0:"]/form/div/div[5]/button').click()
    driver.find_element(By.XPATH, '//*[@id="top"]/div/div/div[2]/button[1]').click()
    time.sleep(2)

go_to_login_page()
happy_flow_login("knees@random.com", "Knees.03")
logout()
go_to_login_page()
submit_login_form()
negative_flow_login("knees@random.com", "")
negative_flow_login("", "Knees.03")
negative_flow_login("knees", "Knees.03")
negative_flow_login("knees@random.com", "Knees03")


