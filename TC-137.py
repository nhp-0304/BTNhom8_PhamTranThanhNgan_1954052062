from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://moji.vn/')

driver.set_window_size(1280,680)
driver.find_element(By.LINK_TEXT, 'TẤT CẢ').click()
driver.find_element(By.LINK_TEXT, 'Phụ kiện thời trang').click()
driver.find_element(By.CSS_SELECTOR, 'li:nth-child(2) > .drop').click()

articles = driver.find_elements(By.ID, 'c-362859')
for item in articles:
    try:
        title = item.find_element(By.CSS_SELECTOR, 'li')
        link = item.find_element(By.CSS_SELECTOR, 'li>a')
        print(title.text)
        print(link.get_attribute('href'))
        print('__________')
    except NoSuchElementException:
        pass

driver.close()