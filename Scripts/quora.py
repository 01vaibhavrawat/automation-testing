from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import sys
import json
from time import sleep

PROXY = "12.345.678.910:8080"


driver = webdriver.Chrome()
driver.delete_all_cookies()
def send_requests(url="https://www.quora.com/partners", max_wait=10, total_requests=25):

	driver.get('https://www.quora.com/')

	sleep(5)


	try:
	   email = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[1]/input')
	   email.send_keys('vaibhrawat@yandex.com')

	   password = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[2]/input')
	   password.send_keys('randompass9412A')

	   wait = WebDriverWait(driver, 10, poll_frequency=5, ignored_exceptions=[ElementClickInterceptedException])
	   element = wait.until(EC.element_to_be_clickable((By.XPATH, "html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[3]/input")))

	   sleep(3)
	   login = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[3]/input')
	   login.click()
	except:
	   email = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/input')
	   email.send_keys('vaibhrawat@yandex.com')

	   password = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/input')
	   password.send_keys('randompass9412A')

	   wait = WebDriverWait(driver, 10, poll_frequency=5, ignored_exceptions=[ElementClickInterceptedException])
	   element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[4]/span/button")))

	   try:
	        login = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[4]/span/button/div/div/div/div/div')
	        login.click()
	   except:
	        login = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[3]/input')
	        login.click()

	    
	#login


	sleep(5)
	wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
	element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/span/button/div/div/div")))


	driver.get('https://www.quora.com/As-a-programmer-do-you-think-that-the-right-arrow-key-should-be-more-close-to-the-fingers-in-the-keyboard-because-it-is-used-so-much')

	try:
		wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
		element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div/div[1]/div[1]/div/div[3]/div/div[1]/div[3]/div/div[2]/div/div/div")))
	except:
		try:
			wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
			element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div/div[1]/div[1]/div/div[3]/div/div[1]/div[3]/div/div[2]/div/div/div")))
		except:
			try:
				wait = WebDriverWait(driver, 30, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
				element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div/div[1]/div[1]/div/div[3]/div/div[1]/div[3]/div/div[2]/div/div/div")))
			except:
				driver.refresh()
				wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
				element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div/div[1]/div[1]/div/div[3]/div/div[1]/div[3]/div/div[2]/div/div/div")))
			

	sleep(3)
	request = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div/div[1]/div[1]/div/div[3]/div/div[1]/div[3]/div/div[2]/div/div/div')
	request.click()

	sleep(10)



	request_buttons = driver.find_elements_by_css_selector('#root > div > div:nth-child(1) > div > div > div > div > div.q-flex.modal_content_inner.qu-flexDirection--column.qu-bg--white.qu-overflowY--auto.qu-borderAll.qu-alignSelf--center > div > div > div.q-box.qu-overflowY--auto > div.q-flex.qu-pt--small > div.q-relative.qu-flex--auto.qu-ml--medium.qu-overflowY--auto > div.q-box > div > div:nth-child(2) > div > div > div.q-box.qu-flex--none.qu-display--inline-flex.qu-ml--medium > div > div > div > span > span > svg > g > circle')

	for each_writer in range(total_requests):
		each_writer.click()
		send_request = all_writers[each_writer].find_element_by_css_selector("#root > div > div:nth-child(1) > div > div > div > div > div.q-flex.modal_content_inner.qu-flexDirection--column.qu-bg--white.qu-overflowY--auto.qu-borderAll.qu-alignSelf--center > div > div > div.q-box.qu-overflowY--auto > div.q-flex.qu-pt--small > div.q-relative.qu-flex--auto.qu-ml--medium.qu-overflowY--auto > div.q-box > div > div:nth-child(2) > div > div > div.q-box.qu-flex--none.qu-display--inline-flex.qu-ml--medium > div > div > div > span > span > svg > g > circle")
		send_request.click()
		driver.execute_script("window.scrollTo(0, 5)")


	driver.delete_all_cookies()
send_requests(max_wait=10)
