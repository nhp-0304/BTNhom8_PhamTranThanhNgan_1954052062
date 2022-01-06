import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://moji.vn/')

driver.set_window_size(1000,1200)
driver.find_element(By.XPATH, '/html/body/header/div[2]/div[1]/div/div[3]/div/ul/li[1]/a').click()

driver.find_element(By.NAME, 'username').send_keys('trangduong1501@gmail.com')
driver.find_element(By.NAME, 'password').send_keys('ktpmim91')
driver.find_element(By.CSS_SELECTOR, '#btnsignin').click()
time.sleep(1)

driver.set_window_size(1382, 744)

driver.find_element(By.CSS_SELECTOR, 'h3 a').click()
driver.find_element(By.ID, 'addToCart').click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, '#modalAbandoned > div > div > div.modal-body > button').click()

driver.find_element(By.CSS_SELECTOR, ".count-cart").click()
driver.find_element(By.CSS_SELECTOR, ".count-cart-icon").click()
driver.find_element(By.LINK_TEXT, "Xem giỏ hàng").click()
driver.find_element(By.LINK_TEXT, "Thanh toán").click()

driver.find_element(By.NAME, "paymentMethod").click()
time.sleep(3)

print(driver.find_element(By.CSS_SELECTOR, "#formCheckOut > div > div.col-checkout.col-center.col-xl-3.col-lg-6.col-12 > div:nth-child(2) > label > div").text)
print('----------')
print(driver.find_element(By.CSS_SELECTOR,"#p-online > p").text)
print('-------------------')
print(driver.find_element(By.CSS_SELECTOR, "#formCheckOut > div > div.col-checkout.col-center.col-xl-3.col-lg-6.col-12 > div:nth-child(3) > label > div").text)
print('----------')
print(driver.find_element(By.CSS_SELECTOR,"#p-cod > p:nth-child(1) > span > span").text)
print('----------')
print(driver.find_element(By.CSS_SELECTOR,"#p-cod > p:nth-child(2)").text)
print('----------')
print(driver.find_element(By.CSS_SELECTOR,"#p-cod > p:nth-child(3)").text)

time.sleep(3)

driver.close()