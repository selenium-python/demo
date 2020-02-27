from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

 


driver=webdriver.Chrome("C:\Chrome driver\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/fetchcat.htm")
window_before1 = driver.window_handles[0]

 

time.sleep(4)
aboutus = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/ul/li[3]/a/span")
time.sleep(2)
office = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/ul/li[3]/ul/li/a/span")
time.sleep(2)
chennai = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/ul/li[3]/ul/li/ul/li[1]/a/span")

 

actions = ActionChains(driver)
actions.move_to_element(aboutus).move_to_element(office).move_to_element(chennai).click(chennai).perform()
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
driver.switch_to_frame("main_page")

 

contact = driver.find_element_by_id("demo3").text

 

print(contact)
