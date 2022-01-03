import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://moji.vn/')

driver.set_window_size(1000,1200)
driver.find_element(By.XPATH, '/html/body/header/div[2]/div[1]/div/div[3]/div/ul/li[1]/a').click()

driver.find_element(By.NAME, 'username').send_keys('')
driver.find_element(By.NAME, 'password').send_keys('anh789')
driver.find_element(By.CSS_SELECTOR, '#btnsignin').click()
time.sleep(1)

try:
    driver.find_element(By.NAME, 'address').clear()
    driver.find_element(By.CLASS_NAME, 'btn btn-pink').click()
except NoSuchElementException:
    pass

error = driver.find_element(By.CLASS_NAME, "formErrorContent")
print(error.text)

driver.quit()