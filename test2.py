#counnt the number of rows and colums
#read specific row and colums data
#read all the rows and colum data
#read data based on condition

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\Program Files\Drivers\chromedriver\chromedriver.exe"))

driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(5)
driver.maximize_window()

#count the number of columns
column = len(driver.find_elements(By.XPATH,"(//table[@name='BookTable'])[1]//th"))

#count the number of row
row = len(driver.find_elements(By.XPATH,"(//table[@name='BookTable'])[1]//tr"))

#read specific row and column data
rowcoldata1 = driver.find_element(By.XPATH,"(//table[@name='BookTable'])[1]//tr[3]/td[2]").text
rowcoldata2 = driver.find_element(By.XPATH,"(//table[@name='BookTable'])[1]//tr[6]/td[3]").text
rowcoldata3 = driver.find_element(By.XPATH,"(//table[@name='BookTable'])[1]//tr[7]/td[4]").text
rowcoldata4 = driver.find_element(By.XPATH,"(//table[@name='BookTable'])[1]//tr[2]/td[1]").text


#read all the row and column data

for r in range (2,row+1):
    for c in range (1,column+1):
        alldata = driver.find_element(By.XPATH,"(//table[@name='BookTable'])[1]//tr["+str(r)+"]/td["+str(c)+"]").text
        print (alldata)




print ("This is the number of column", column)
print ("This is the number of row", row)
print(rowcoldata1,rowcoldata2,rowcoldata3,rowcoldata4)



