import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://moji.vn/')

driver.set_window_size(1000,1200)
driver.find_element(By.XPATH, '/html/body/header/div[2]/div[1]/div/div[3]/div/ul/li[1]/a').click()

driver.find_element(By.NAME, 'username').send_keys('trangduong1501@gmail.com')
driver.find_element(By.NAME, 'password').send_keys('ktpmim91')
driver.find_element(By.CSS_SELECTOR, '#btnsignin').click()
time.sleep(1)

driver.find_element(By.XPATH, '/html/body/header/div[2]/div[1]/div/div[3]/div/ul/li[1]/a').click()
city = Select(driver.find_element(By.NAME, 'districtId'))
city.select_by_visible_text('Quận/ Huyện *')
driver.implicitly_wait(5)
a = driver.find_element(By.XPATH, '//*[@id="formAcount"]/div[8]/div/div/button')
driver.execute_script("arguments[0].click();", a)

error = driver.find_element(By.CLASS_NAME, "formErrorContent")
print(error.text)

driver.quit()