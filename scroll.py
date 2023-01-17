import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://mdbootstrap.com/docs/standard/methods/lazy-loading/")
driver.maximize_window()
""" to scroll anywhere on page"""

# driver.execute_script("window.scrollTo(0,3400)")


""" to scroll till end of page"""
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

""" to scroll with the help of For loop on page"""
# y = 1000
# for step in range(0,6):
#     driver.execute_script("window.scrollTo(0,"+str(y)+")")
#     y += 1000
""" to scroll with the help of For loop on page"""



""" to scroll with the help specific element on page"""
img = driver.find_element(By.XPATH, "(//img[@alt='Small Apartment'])[3]")
driver.execute_script("arguments[0].scrollIntoView();", img)
""" to scroll with the help of For loop on page"""



time.sleep(2)
img_url = driver.find_element(By.XPATH, "(//img[@alt='Small Apartment'])[3]").get_attribute("src")
driver.execute_script("window.scrollTo(0,0)")

print(img_url)

