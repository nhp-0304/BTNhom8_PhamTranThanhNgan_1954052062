from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://moji.vn/')

driver.set_window_size(1280,680)
driver.find_element(By.CSS_SELECTOR, 'a').click()
driver.find_element(By.LINK_TEXT, 'Phụ kiện thời trang').click()

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

driver.close()