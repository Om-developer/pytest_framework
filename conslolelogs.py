import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = {'browser': 'ALL'}
console_error = []
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=dc)
driver.get("https://www.tutorialspoint.com/getting-console-log-output-from-chrome-with-selenium-python-api-bindings")
time.sleep(5)
logs = driver.get_log('browser')
for log in logs:
    if log['level'] == "SEVERE":
        console_error.append(log["message"])

print(console_error)