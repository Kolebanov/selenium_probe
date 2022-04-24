from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = os.path.abspath('chromedriver/stable/chromedriver')

# options = Options()
# options.binary_location = '/usr/bin/google-chrome'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--headless")

url = 'https://koronapay.com/transfers/online'
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)


try:
    driver.get(url=url)
    countries_menu = driver.find_element_by_id('changeable-field-select-receivingCountry')
    countries_menu.click()
    print('menu clicked')
    time.sleep(1)
    element_uzbekistan = driver.find_element_by_id("react-select-2-option-1")
    element_uzbekistan.click()
    print('Uzbekistan clicked')
    time.sleep(1)
    amount_field = driver.find_element_by_id("changeable-field-input-amount")
    # element_uzbekistan.click()
    amount_field.send_keys("1")
    print('amount inserted')
    time.sleep(1)
    # rate_of_usd = driver.find_element_by_id("static-text-calculatorExchangeRate")
    rate_of_usd_wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "static-text-calculatorExchangeRate"))
    )
    rate_korona_usd = float(rate_of_usd_wait.text.split(' ')[3].replace(',', '.'))
    print(f'rate finded! {rate_korona_usd}')

    # src = driver.page_source
    # with open('index.html', 'w') as file:
    #     file.write(src)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()