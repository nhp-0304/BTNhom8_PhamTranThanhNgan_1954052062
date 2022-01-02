import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://moji.vn/')

driver.set_window_size(1280,880)
driver.find_element(By.LINK_TEXT, 'TẤT CẢ').click()
driver.get('https://moji.vn/product?price=200000:300000#')

articles = driver.find_elements(By.CSS_SELECTOR, 'div.product-item')
for item in articles:
    try:
        title = item.find_element(By.TAG_NAME, 'h3')
        price = item.find_element(By.CSS_SELECTOR, 'div.product-price>span')
        link = item.find_element(By.CSS_SELECTOR, 'h3.name>a')
        print(title.text)
        print(price.text)
        print(link.get_attribute('href'))
        print('__________')
    except NoSuchElementException:
        pass
time.sleep(3)
driver.close()

