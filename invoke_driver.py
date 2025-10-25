from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
txt = driver.find_element(By.XPATH,"//div[contains(text(),'Swag Labs')]")
print(txt.text)

products = driver.find_elements(By.XPATH,"//div[@class='inventory_item_name ']")
for product in products:
    print(product.text)
# print("***************")
driver.find_element(By.XPATH,"//select[@class='product_sort_container']").click()
driver.find_element(By.XPATH,"//option[contains(text(),'Name (Z to A)')]").click()
products = driver.find_elements(By.XPATH,"//div[@class='inventory_item_name ']")
for product in products:
    print(product.text)
driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']").click()
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
# driver.find_element(By.XPATH,"//button[@name='checkout']").click()
# driver.find_element(By.XPATH,"//input[@id='first-name']").send_keys("firstname")
# driver.find_element(By.XPATH,"//input[@id='last-name']").send_keys("lastname")
# driver.find_element(By.XPATH,"//input[@id='postal-code']").send_keys("431608")
# driver.find_element(By.XPATH,"//input[@id='continue']").click()
# driver.find_element(By.XPATH,"//button[contains(text(),'Finish')]").click()
# text_msg =driver.find_element(By.XPATH,"//h2[contains(text(),'Thank you for your order!')]").text
# print(text_msg)
# time.sleep(3)
