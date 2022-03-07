from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.select import Select 
from selenium.webdriver import ActionChains as A
from selenium.webdriver.common.keys import Keys as K
from selenium.webdriver.common.keys import Keys
	
driver = webdriver.Chrome()
driver.get('https://temp-mail.org/en/')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/form/div[2]/button')))

copy = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/form/div[2]/button')
copy.click()


driver.execute_script("window.open('https://www.facebook.com')")
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])


create_new_account = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a')
create_new_account.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.NAME,'firstname')))






first_name = driver.find_element_by_name('firstname')
first_name.send_keys('john')

surname = driver.find_element_by_name('lastname')
surname.send_keys('cena')

email = driver.find_element_by_name('reg_email__')
email.send_keys('laset40057@ermailo.com')


confirm_email = driver.find_element_by_name('reg_email_confirmation__')
confirm_email.send_keys('laset40057@ermailo.com')

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.NAME,'reg_email_confirmation__')))

password = driver.find_element_by_name('reg_passwd__')
password.send_keys('randompassworj3095r34')

day = Select(driver.find_element_by_name("birthday_day")) 
day.select_by_index(10)

month = Select(driver.find_element_by_name("birthday_month")) 
month.select_by_index(10)

Year = Select(driver.find_element_by_name("birthday_year")) 
Year.select_by_index(20)

gender = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/label')
gender.click()

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.select import Select 
import time

driver = webdriver.Chrome()



driver.get('https://temp-mail.org/en/')


wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/form/div[2]/button'))       




copy = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/form/div[2]/button')
copy.click()


driver.execute_script("window.open()")
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])

driver.get('https://www.facebook.com')

create_new_account = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a')
create_new_account.click()




driver = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.ID, "u_1_b")) 
    ) 

first_name = driver.find_element_by_name('First name')
first_name.send_keys('john')

surname = driver.find_element_by_name('lastname')
surname.send_keys('cena')

email = driver.find_element_by_name('reg_email__')
email.send_keys(Keys.CONTROL, 'v')

password = driver.find_element_by_name('reg_passwd__')
password.send_keys('randompassworj3095r34')

day = Select(driver.find_element_by_name("birthday_day")) 
day.select_by_index(10)

month = Select(driver.find_element_by_name("birthday_month")) 
month.select_by_index(10)

Year = Select(driver.find_element_by_name("birthday_year")) 
Year.select_by_index(20)

gender = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/label')
gender.click()

import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

driver.execute_script()
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
equest = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div/div[1]/div[1]/div/div[3]/div/div[1]/div[3]/div/div[2]/div/div/div')


d5
