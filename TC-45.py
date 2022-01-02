import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://moji.vn/')

driver.set_window_size(1000,1200)
driver.find_element(By.XPATH, '/html/body/header/div[2]/div[1]/div/div[3]/div/ul/li[1]/a').click()

driver.find_element(By.NAME, 'username').send_keys('trangduong1501@gmail.com')
driver.find_element(By.NAME, 'password').send_keys('ktpmim91')
driver.find_element(By.CSS_SELECTOR, '#btnsignin').click()
time.sleep(1)

try:
    driver.find_element(By.XPATH, '/html/body/header/div[2]/div[1]/div/div[3]/div/ul/li[1]/a').click()
    driver.find_element(By.NAME, 'fullName').clear()
    driver.find_element(By.NAME, 'fullName').send_keys('Minh Trang')
    driver.find_element(By.CLASS_NAME, 'btn btn-pink').click()
except NoSuchElementException:
    pass

profile = driver.find_elements(By.CSS_SELECTOR, 'div.col-md-9.col-sm-12 header')
for p in profile:
    print(p.text)

name = driver.find_element(By.NAME, 'fullName').get_attribute('value')
print('Họ Tên: ', name)
bday = driver.find_element(By.NAME, 'birthday').get_attribute('value')
print('Ngày sinh: ',bday)
dt = driver.find_element(By.NAME, 'mobile').get_attribute('value')
print('Điện thoại: ',dt)
mail = driver.find_element(By.NAME, 'email').get_attribute('value')
print('Email: ',mail)
city = Select(driver.find_element(By.NAME, 'cityId'))
c = city.first_selected_option
print('Tỉnh/Thành phố: ',c.text)
dist = Select(driver.find_element(By.NAME, 'districtId'))
d = dist.first_selected_option
print('Quận/Huyện: ',d.text)
address = driver.find_element(By.NAME, 'address').get_attribute('value')
print('Địa chỉ chi tiết: ',address)

driver.quit()
