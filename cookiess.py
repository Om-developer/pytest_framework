from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://pythonbasics.org/selenium-cookies/")
driver.add_cookie({'name' : 'foo', 'value' : 'bar'})

cookie = driver.get_cookies()
for cookies in cookie:
    print(cookies)
