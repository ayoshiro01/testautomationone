import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(service=Service("C:\Program Files\Drivers\chromedriver\chromedriver.exe"))

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.ID,"name").send_keys("Abass")
time.sleep(3)
driver.find_element(By.ID,"email").send_keys("abass4real@gmail.com")
time.sleep(3)
driver.find_element(By.ID,"phone").send_keys("+2348081966755")
time.sleep(3)
driver.find_element(By.ID,"textarea").send_keys("NO 2 Saheed Alim Streest Off Hon Musa Diko Streest, Duste Baupma New Extension,Duste Alhaji Abuja")
time.sleep(3)

driver.find_element(By.XPATH,"//input[@id='male']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='monday']").click()
driver.find_element(By.XPATH,"//input[@id='tuesday']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//select[@id='country']")
dropdown = Select(driver.find_element(By.XPATH,"//select[@id='country']"))
countries = dropdown

countries.select_by_visible_text("Canada")
time.sleep(3)


driver.find_element(By.XPATH,"//select[@id='colors']")
color = Select(driver.find_element(By.XPATH,"//select[@id='colors']"))
colors = color

colors.select_by_visible_text("Blue")
time.sleep(5)

driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("08/10/2023")
time.sleep(5)

driver.close()
