from selenium import webdriver
'''from selenium.webdriver.common.keys import Keys'''
from select  import select
import time


driver=webdriver.Chrome("C:\Chrome driver\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/index.php")

driver.find_element_by_link_text("REGISTER").click()
'''driver.find_element_by_name("userName").send_keys("Nebhit")'''
driver.find_element_by_name("firstName").send_keys("Neha")

driver.find_element_by_name("lastName").send_keys("Gupta")
driver.find_element_by_xpath("//input[@value='Female']").click()

select=select(driver.find_element_by_name('securityQuestion'))
select.select_by_visible_text('What is your favour color?')
time.sleep(2)
select.select_by_value("411012")

