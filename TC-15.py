import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')

driver.get('https://moji.vn/')

driver.implicitly_wait(15)
driver.set_window_size(1296, 696)
driver.find_element(By.NAME, "q").click()
driver.find_element(By.NAME, "q").send_keys("MSP324")
driver.find_element(By.CSS_SELECTOR, ".head-col-center .fa").click()


time.sleep(2)
driver.quit()