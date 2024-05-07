from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver = webdriver.Firefox()
# Open the webpage to url
driver.get(url)
driver.implicitly_wait(time_to_wait=10)


username = 'Admin'
password = 'admin123'
    # Locators for Login
username_locator = 'username'
password_locator = 'password'

submitButton_locator = '//button[@type="submit"]'

webelemnt_of_username = driver.find_element(By.NAME,username_locator)
webelemnt_of_password = driver.find_element(By.NAME,password_locator)
webelemnt_of_submitButton= driver.find_element(By.XPATH,submitButton_locator)


webelemnt_of_username.send_keys(username)
webelemnt_of_password.send_keys(password)
webelemnt_of_submitButton.click()



Pim_menu_option_xpath = '//a[@href="/web/index.php/pim/viewPimModule"]'
Pim_menu_option_element = driver.find_element(By.XPATH, Pim_menu_option_xpath)

Pim_menu_option_element.click()

#Click the Add Button

addbutton_elemnt = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
addbutton_elemnt.click()

#Enter the First name and last name

firstname_webelemnt= driver.find_element(By.NAME,value="firstName")
firstname_webelemnt.send_keys("MahendraSingh")
lastname_webelemnt= driver.find_element(By.NAME,value="lastName")
lastname_webelemnt.send_keys("Dhoni")

#Click save button

savebutton_elemnt = driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
savebutton_elemnt.click()


