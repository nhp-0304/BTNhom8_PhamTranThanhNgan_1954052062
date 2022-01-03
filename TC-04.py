from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time

driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')

driver.get('https://moji.vn/')

driver.set_window_size(1050, 708)
driver.find_element(By.LINK_TEXT, "Đăng ký").click()
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys("kakimanh")
driver.find_element(By.ID, "fullName").click()
driver.find_element(By.ID, "fullName").send_keys("Ka kim ánh")
driver.find_element(By.ID, "mobile").send_keys("0934627703")
driver.find_element(By.ID, "email").send_keys("ngan1@gmail.com")
articles = driver.find_element(By.ID, "cityId")
driver.find_element(By.XPATH, "//option[. = 'Thừa Thiên Huế']").click()
driver.find_element(By.ID, "address").send_keys("127A lê lư")
driver.find_element(By.ID, "birthday").click()
driver.find_element(By.ID, "birthday").send_keys("")
driver.find_element(By.ID, "districtId").click()
driver.find_element(By.ID, "districtId").send_keys("Huyện Phú Lộc")
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("anh789")
driver.find_element(By.ID, "rePassword").click()
driver.find_element(By.ID, "rePassword").send_keys("anh789")

try:
    driver.find_element(By.NAME, 'birthday').clear()
    driver.find_element(By.CLASS_NAME, 'btn btn-pink').click()
except NoSuchElementException:
    pass

error = driver.find_element(By.CLASS_NAME, "formErrorContent")
print(error.text)

time.sleep(2)
driver.quit()

