from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://www.desmos.com/scientific#:~:text=A%20beautiful,%20free%20online%20scientific%20calculator")

time.sleep(2)
squared_button = driver.find_element(By.XPATH, "//span[@aria-label='Squared']")
squared_button.click()

superscript_button = driver.find_element(By.XPATH, "//span[@aria-label='Superscript']")
superscript_button.click()
time.sleep(1)

seven_button = driver.find_element(By.XPATH, "//span[@aria-label='7']")
seven_button.click()
time.sleep(1)

math_field = driver.find_element(By.CSS_SELECTOR, ".dcg-mq-root-block")
entered_value = math_field.text
