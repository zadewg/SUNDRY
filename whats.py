from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

#config
number_of_times = 10
name = 'minombre' #exactamenre como me tengas agregado.
message = 'TestTestTest'

driver = None

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

def web_driver_load():
	global driver
	driver = webdriver.Firefox()

def web_driver_quit():
	driver.quit()
	quit()

def whatsapp_login():
	driver.get('https://web.whatsapp.com/');
	while True:
		time.sleep(1)
		try:
			appLoad = driver.find_element_by_xpath("//div[@class='app two']")
			if appLoad:
				gotoChathead(name)
		except NoSuchElementException:
			pass
		finally:
			print('Login Checked')

def sendMessage(msg='Hi!'):
	web_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
	web_obj.send_keys(msg)
	web_obj.send_keys(Keys.RETURN)

def gotoChathead(name):
	recentList = driver.find_elements_by_xpath("//span[@class='emojitext ellipsify']")
	for head in recentList:
		if head.text == name:
			head.click()
			break



if __name__ == "__main__":
	web_driver_load()
	whatsapp_login()
	for i in range(number_of_times):
		sendMessage(message)
		wait()
	print("Process complete successfully")
        web_driver_quit()
