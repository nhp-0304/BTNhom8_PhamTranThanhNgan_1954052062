import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get("https://moji.vn/")
driver.set_window_size(1050, 708)
driver.find_element(By.LINK_TEXT, "Đăng nhập |").click()
driver.find_element(By.LINK_TEXT, "Quên mật khẩu?").click()
driver.find_element(By.ID, "btnSubmit").click()

driver.find_element(By.ID, "newpassword").clear()
time.sleep(3)

error = driver.find_element(By.CLASS_NAME, "formErrorContent")
print(error.text)
time.sleep(3)

driver.close()

