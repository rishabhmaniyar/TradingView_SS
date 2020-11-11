from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import requests
import os

driver = webdriver.Chrome(r"C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.tradingview.com/#signin')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span').click()
username=''
password=''
driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div/div/div/div/div/form/div[1]/div[1]/input').send_keys(username)
driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div/div/div/div/div/form/div[2]/div[1]/input').send_keys(password)
driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div/div/div/div/div/form/div[4]/div[2]/button/span[2]').click()
time.sleep(5)
driver.find_element_by_link_text('Chart').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[16]/div/span').click()
time.sleep(3)
link = driver.find_element_by_class_name("textInput-3WRWEmm7").get_attribute('value')
print(link)
driver.quit()

