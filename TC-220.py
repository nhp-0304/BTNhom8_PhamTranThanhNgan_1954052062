from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import TimeoutException
import time
driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')

driver.get('https://moji.vn/')
driver.set_window_size(1296, 696)
driver.find_element(By.LINK_TEXT, "TẤT CẢ").click()
driver.find_element(By.CSS_SELECTOR, ".widget_price_filter").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".js-fil-bar").click()
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