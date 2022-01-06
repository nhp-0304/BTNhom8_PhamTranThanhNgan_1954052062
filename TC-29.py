import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://moji.vn/')

driver.set_window_size(1000,1200)
driver.find_element(By.XPATH, '/html/body/header/div[2]/div[1]/div/div[3]/div/ul/li[1]/a').click()

driver.find_element(By.NAME, 'username').send_keys('trangduong1501@gmail.com')
driver.find_element(By.NAME, 'password').send_keys('ktpmim91')
driver.find_element(By.CSS_SELECTOR, '#btnsignin').click()
time.sleep(1)

try:
    driver.find_element(By.CSS_SELECTOR, 'h3 a').click()
    driver.find_element(By.ID, 'addToCart').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#modalAbandoned > div > div > div.modal-body > button').click()
    driver.implicitly_wait(3)
    a = driver.find_element(By.XPATH, '/html/body/header/div[2]/div[1]/div/div[3]/div/div/div[1]')
    driver.execute_script("arguments[0].click();", a)
    b = driver.find_element(By.XPATH, '//*[@id="js-rs-mini-cart"]/div/a')
    driver.execute_script("arguments[0].click();", b)
    time.sleep(1)
    d = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/table/tbody/tr[1]/td[6]/a')
    driver.execute_script("arguments[0].click();", d)
    c = driver.switch_to.alert
    if c.text == '':
        print('Failed')
    else:
        print(c.text)
    driver.switch_to.alert.accept()
except NoSuchElementException:
    pass

driver.quit()