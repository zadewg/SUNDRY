import time
from selenium import webdriver

driver = webdriver.Firefox()
while True:
	try:
		button = driver.find_element_by_class_name('qr-button')
		print " [*] Idle detected, Reloading QR code image..."
		button._execute(webdriver.remote.command.Command.CLICK_ELEMENT)
		time.sleep(5)
	except:
		pass

	try:
		img = driver.find_elements_by_tag_name('img')[0]
		src = img.get_attribute('src').replace("data:image/png;base64,","")
		print " [*] QR code image detected !"
		print " [*] Downloading the image..."
		binary_data = a2b_base64(src)
		qr = open("tmp.png","wb")
		qr.write(binary_data)
		print " [*] Saved To tmp.png"
		qr.close()
		time.sleep(5)
		continue
	except:
		break
