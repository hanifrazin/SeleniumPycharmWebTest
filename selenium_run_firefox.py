from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

# untuk menjalankan browser di firefox silahkan import library ini
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service

# hal ini dilakukan untuk get binary firefox
ops = options()
ops.binary_location = '/usr/bin/firefox'

# hal ini dilakukan untuk get binary dari geckodriver
service = Service('/usr/local/bin/geckodriver')

# variabel service dan ops wajib di pass di Firefox() dan ini hanya berlaku di pycharm
driver = webdriver.Firefox(service=service, options=ops)

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("bootcampTAK")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
